#/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import OpenSSL
import json
import datetime
from passlib.hash import sha256_crypt
from flaskext.mysql import MySQL
import mysql.connector
import time
import flask_mail
from flask import Flask ,render_template, request, url_for, redirect, make_response, jsonify, session

app = Flask(__name__)
app.debug = True
db = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'laisse-le-pc'
app.config['MYSQL_DATABASE_DB'] = 'donne_rcp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mail_setting = {
	"MAIL_SERVER": 'stmp.gmail.com',
	"MAIL_PORT": 465,
	"MAIL_USE_TLS": False,
	"MAIL_USE_SSL": True,
	"MAIL_USERNAME": 'fabfly95',
	"MAIL_PASSWORD": 'dgdgdjfytryruu'
}
app.config.update(mail_setting)
db.init_app(app)
app.secret_key = 'd66HR8dç"f_-àgjYYic*dh'

def connexiondb():
	try:
		#curseur initialiser
		cursor = db.connect().cursor()
	except Exception, e:
		return str(e)
	return cursor
def connectordb():
	cnx = mysql.connector.connect(user='root', password='laisse-le-pc', host='localhost', database='donne_rcp' )
	return cnx

def global_name(string1, string2):
	Gname= str(string1)+" "+str(string2)
	return Gname

def convertdate(rows):
	dateconvert = json.dumps(time.mktime(rows[2].timetuple())*1000)
	return dateconvert

def controleur(verifie, curseur):
	curseur.execute("SELECT email FROM Administrateur WHERE email=%s", (verifie))
	x= len(curseur.fetchall())
	curseur.close()
	return x

@app.route("/", methods=['GET', 'POST'])
def connexion():
	cursor = connexiondb()
	error=''
	try:
		if session.get('log_in') != True :
			if request.method == "POST":
				mail = request.form['mail']
				passd = request.form['password']
				cursor.execute("SELECT * FROM Administrateur WHERE email=%s", (mail))
				data = cursor.fetchall()
				if len(data) == 1:
					dat = data[0]
					if sha256_crypt.verify(passd, dat[4]):
						session['log_in']= True
						session['username']= global_name(dat[1], dat[2])
						session.permanent = True
						return redirect(url_for('index'))
					else:
						error="mail ou mot de passe incorrect!" 
				else:
					error="mail ou mot de passe incorrect!"
		else:
			return redirect(url_for('index'))
		
	except Exception, e:
		return str(e)

	return render_template('login.html', error=error)
	
@app.route('/deconnexion')
def deconnexion():
	session.pop('log_in', None)
	return redirect(url_for('connexion'))

@app.route('/resetpass', methods=['GET', 'POST'])
def resetpass():
	cursor = connexiondb();
	msg=''
	try:
		if request.method == "POST":
			rmail = request.form['Resetmail']
			cursor.execute("SELECT * FROM Administrateur WHERE Email=%s", (rmail))
			requet = cursor.fetchall()
			if len(requet) == 1:

				envoi = flask_mail.Message(subject='hello',
					sender=app.config.get('MAIL_USERNAME'),
					body='hallo hello flask test')
				envoi.add_recipient(rmail)
				flask_mail.Mail().send(envoi)
				msg= 'mail envoyer'
			else:
				msg= 'mail incorrect'
	except Exception, e:
		return str(e)
	return render_template('resetpass.html', msg=msg)

@app.route('/add_admin', methods=['GET', 'POST'])
def addadmin():
	try:
		cursor = connexiondb()
		cnx = connectordb()
		addmsg = ''
		if session.get('log_in') == True:
			if request.method == 'POST':
				if request.form['addpass'] == request.form['vpass']:
					addprenom = request.form['Prenom']
					addnom = request.form['Nom']
					addmail = request.form['mailadd']
					addpass = request.form['addpass']
					raddpass = sha256_crypt.encrypt(addpass)
					control = controleur(addmail, cursor)
					if control == 0:
						cnx.cursor().execute("INSERT INTO Administrateur (nom, Prenom, email, password) VALUES (%s, %s, %s, %s)", (addnom, addprenom, addmail, raddpass))
						cnx.commit()
						cnx.cursor().close()
						cnx.close()
						addmsg = 'Administrateur bien enregistrer'

					else:
						addmsg='cet utilsateur existe déjà changer vérifier votre email et réessayer'

				else:
					addmsg = 'Les deux mot de passe ne sont pas identique !'
					


		else:
			return redirect(url_for('connexion'))
		
	except Exception, e:
		return str(e)
	return render_template('addadmin.html', addmsg=addmsg)

@app.route('/del_admin', methods=['GET', 'POST'])
def del_admin():
	cursor = connexiondb()

	cnx = connectordb()
	delmsg = ''
	try:
		
		if session.get('log_in') == True:
				if request.method == "POST":
					deletemail = request.form['delmail']
					controll = controleur(deletemail, cursor)
					if controll == 1:
						cursor.execute("SELECT id_admin, email FROM Administrateur WHERE email=%s", (deletemail))
						re = cursor.fetchone()[1]
						cursor.close()
						cursor.execute("DELETE FROM Administrateur WHERE id_admin=%s", (re))
						cnx.commit()
						cursor.close()
						delmsg = 'Compte supprimer !!'+ str(re)
					else:
						delmsg = "le compte n'existe pas"
					
		else:
			return redirect(url_for('connexion'))				
	except Exception, e:
		return str(e)
	return render_template('deleteadmin.html', delmsg= delmsg)
	

@app.route('/index')
def index():
	if session.get('log_in') == True:
		cursor= connexiondb()
		cursor.execute("SELECT * FROM donnee_capteur where capteurs_id_capteur = %s", (101))
		#donne du 1er capteur
		retour1 = cursor.fetchall()
		maxic1 = len(retour1)
		db1c1 = maxic1-19
		data1c1 = retour1[db1c1]
		data2c1 =  retour1[db1c1+1]
		data3c1 = retour1[db1c1+2]
		data4c1 = retour1[db1c1+3]
		data5c1 = retour1[db1c1+4]
		data6c1 = retour1[db1c1+5]
		data7c1 = retour1[db1c1+6]
		data8c1 = retour1[db1c1+7]
		data9c1 = retour1[db1c1+8]
		data10c1 = retour1[db1c1+9]
		data11c1 = retour1[db1c1+10]
		data12c1 = retour1[db1c1+11]
		data13c1 = retour1[db1c1+12]
		data14c1 = retour1[db1c1+13]
		data15c1 = retour1[db1c1+14]
		data16c1 = retour1[db1c1+15]
		data17c1 = retour1[db1c1+16]
		data18c1 = retour1[db1c1+17]
		data19c1 = retour1[db1c1+18]
		
		#conversion des temps en format interprétable par javascript
		db_temps1c1 = convertdate(data1c1)
		db_temps2c1 = convertdate(data2c1)
		db_temps3c1 = convertdate(data3c1)
		db_temps4c1 = convertdate(data4c1)
		db_temps5c1 = convertdate(data5c1)
		db_temps6c1 = convertdate(data6c1)
		db_temps7c1 = convertdate(data7c1)
		db_temps8c1 = convertdate(data8c1)
		db_temps9c1 = convertdate(data9c1)
		db_temps10c1 = convertdate(data10c1)
		db_temps11c1 = convertdate(data11c1)
		db_temps12c1 = convertdate(data12c1)
		db_temps13c1 = convertdate(data13c1)
		db_temps14c1 = convertdate(data14c1)
		db_temps15c1 = convertdate(data15c1)
		db_temps16c1 = convertdate(data16c1)
		db_temps17c1 = convertdate(data17c1)
		db_temps18c1 = convertdate(data18c1)
		db_temps19c1 = convertdate(data19c1)

		#donne du 2e capteur
		cursor.execute("SELECT * FROM donnee_capteur where capteurs_id_capteur = %s", (105))
		retour2 = cursor.fetchall()
		maxic2 = len(retour2)
		db1c2 = maxic2-19
		data1c2 = retour2[db1c2]
		data2c2 =  retour2[db1c2+1]
		data3c2 = retour2[db1c2+2]
		data4c2 = retour2[db1c2+3]
		data5c2 = retour2[db1c2+4]
		data6c2 = retour2[db1c2+5]
		data7c2 = retour2[db1c2+6]
		data8c2 = retour2[db1c2+7]
		data9c2 = retour2[db1c2+8]
		data10c2 = retour2[db1c2+9]
		data11c2 = retour2[db1c2+10]
		data12c2 = retour2[db1c2+11]
		data13c2 = retour2[db1c2+12]
		data14c2 = retour2[db1c2+13]
		data15c2 = retour2[db1c2+14]
		data16c2 = retour2[db1c2+15]
		data17c2 = retour2[db1c2+16]
		data18c2 = retour2[db1c2+17]
		data19c2 = retour2[db1c2+18]
		
		#conversion des temps en format interprétable par javascript
		db_temps1c2 = convertdate(data1c2)		
		db_temps2c2 = convertdate(data2c2)
		db_temps3c2 = convertdate(data3c2)
		db_temps4c2 = convertdate(data4c2)
		db_temps5c2 = convertdate(data5c2)
		db_temps6c2 = convertdate(data6c2)
		db_temps7c2 = convertdate(data7c2)
		db_temps8c2 = convertdate(data8c2)
		db_temps9c2 = convertdate(data9c2)
		db_temps10c2 = convertdate(data10c2)
		db_temps11c2 = convertdate(data11c2)
		db_temps12c2 = convertdate(data12c2)
		db_temps13c2 = convertdate(data13c2)
		db_temps14c2 = convertdate(data14c2)
		db_temps15c2 = convertdate(data15c2)
		db_temps16c2 = convertdate(data16c2)
		db_temps17c2 = convertdate(data17c2)
		db_temps18c2 = convertdate(data18c2)
		db_temps19c2 = convertdate(data19c2)

		#donne 3e capteur
		cursor.execute("SELECT * FROM donnee_capteur where capteurs_id_capteur = %s", (102))
		retour3 = cursor.fetchall()
		maxic3 = len(retour3)
		db1c3 = maxic3-19
		data1c3 = retour3[db1c3]
		data2c3 =  retour3[db1c3+1]
		data3c3 = retour3[db1c3+2]
		data4c3 = retour3[db1c3+3]
		data5c3 = retour3[db1c3+4]
		data6c3 = retour3[db1c3+5]
		data7c3 = retour3[db1c3+6]
		data8c3 = retour3[db1c3+7]
		data9c3 = retour3[db1c3+8]
		data10c3 = retour3[db1c3+9]
		data11c3 = retour3[db1c3+10]
		data12c3 = retour3[db1c3+11]
		data13c3 = retour3[db1c3+12]
		data14c3 = retour3[db1c3+13]
		data15c3 = retour3[db1c3+14]
		data16c3 = retour3[db1c3+15]
		data17c3 = retour3[db1c3+16]
		data18c3 = retour3[db1c3+17]
		data19c3 = retour3[db1c3+18]
		
		#conversion des temps en format interprétable par javascript
		db_temps1c3 = convertdate(data1c3)
		db_temps2c3 = convertdate(data2c3)
		db_temps3c3 = convertdate(data3c3)
		db_temps4c3 = convertdate(data4c3)
		db_temps5c3 = convertdate(data5c3)
		db_temps6c3 = convertdate(data6c3)
		db_temps7c3 = convertdate(data7c3)
		db_temps8c3 = convertdate(data8c3)
		db_temps9c3 = convertdate(data9c3)
		db_temps10c3 = convertdate(data10c3)
		db_temps11c3 = convertdate(data11c3)
		db_temps12c3 = convertdate(data12c3)
		db_temps13c3 = convertdate(data13c3)
		db_temps14c3 = convertdate(data14c3)
		db_temps15c3 = convertdate(data15c3)
		db_temps16c3 = convertdate(data16c3)
		db_temps17c3 = convertdate(data17c3)
		db_temps18c3 = convertdate(data18c3)
		db_temps19c3 = convertdate(data19c3)

		#donne 4e capteur
		cursor.execute("SELECT * FROM donnee_capteur where capteurs_id_capteur = %s", (104))
		retour4 = cursor.fetchall()
		maxic4 = len(retour4)
		data1c4 = retour4[-19]
		data2c4 =  retour4[-18]
		data3c4 = retour4[-17]
		data4c4 = retour4[-16]
		data5c4 = retour4[-15]
		data6c4 = retour4[-14]
		data7c4 = retour4[-13]
		data8c4 = retour4[-12]
		data9c4 = retour4[-11]
		data10c4 = retour4[-10]
		data11c4 = retour4[-9]
		data12c4 = retour4[-8]
		data13c4 = retour4[-7]
		data14c4 = retour4[-6]
		data15c4 = retour4[-5]
		data16c4 = retour4[-4]
		data17c4 = retour4[-3]
		data18c4 = retour4[-2]
		data19c4 = retour4[-1]
		
		#conversion des temps en format interprétable par javascript
		db_temps1c4 = convertdate(data1c4)
		db_temps2c4 = convertdate(data2c4)
		db_temps3c4 = convertdate(data3c4)
		db_temps4c4 = convertdate(data4c4)
		db_temps5c4 = convertdate(data5c4)
		db_temps6c4 = convertdate(data6c4)
		db_temps7c4 = convertdate(data7c4)
		db_temps8c4 = convertdate(data8c4)
		db_temps9c4 = convertdate(data9c4)
		db_temps10c4 = convertdate(data10c4)
		db_temps11c4 = convertdate(data11c4)
		db_temps12c4 = convertdate(data12c4)
		db_temps13c4 = convertdate(data13c4)
		db_temps14c4 = convertdate(data14c4)
		db_temps15c4 = convertdate(data15c4)
		db_temps16c4 = convertdate(data16c4)
		db_temps17c4 = convertdate(data17c4)
		db_temps18c4 = convertdate(data18c4)
		db_temps19c4 = convertdate(data19c4)

		#donne 5e capteur
		cursor.execute("SELECT * FROM donnee_capteur where capteurs_id_capteur = %s", (103))
		retour5 = cursor.fetchall()
		maxic5 = len(retour5)
		data1c5 = retour5[-19]
		data2c5 =  retour5[-18]
		data3c5 = retour5[-17]
		data4c5 = retour5[-16]
		data5c5 = retour5[-15]
		data6c5 = retour5[-14]
		data7c5 = retour5[-13]
		data8c5 = retour5[-12]
		data9c5 = retour5[-11]
		data10c5 = retour5[-10]
		data11c5 = retour5[-9]
		data12c5 = retour5[-8]
		data13c5 = retour5[-7]
		data14c5 = retour5[-6]
		data15c5 = retour5[-5]
		data16c5 = retour5[-4]
		data17c5 = retour5[-3]
		data18c5 = retour5[-2]
		data19c5 = retour5[-1]

		#conversion des temps en format interprétable par javascript
		db_temps1c5 = convertdate(data1c5)
		db_temps2c5 = convertdate(data2c5)
		db_temps3c5 = convertdate(data3c5)
		db_temps4c5 = convertdate(data4c5)
		db_temps5c5 = convertdate(data5c5)
		db_temps6c5 = convertdate(data6c5)
		db_temps7c5 = convertdate(data7c5)
		db_temps8c5 = convertdate(data8c5)
		db_temps9c5 = convertdate(data9c5)
		db_temps10c5 = convertdate(data10c5)
		db_temps11c5 = convertdate(data11c5)
		db_temps12c5 = convertdate(data12c5)
		db_temps13c5 = convertdate(data13c5)
		db_temps14c5 = convertdate(data14c5)
		db_temps15c5 = convertdate(data15c5)
		db_temps16c5 = convertdate(data16c5)
		db_temps17c5 = convertdate(data17c5)
		db_temps18c5 = convertdate(data18c5)
		db_temps19c5 = convertdate(data19c5)
		
		cursor.close()
		#envoi des donnee vers la page html
		return render_template('index.html', 
			rowsc1= retour1, 
			data1c1=data1c1[1], 
			data2c1=data2c1[1], 
			data3c1=data3c1[1], 
			data4c1=data4c1[1], 
			data5c1=data5c1[1],
			data6c1=data6c1[1],
			data7c1=data7c1[1],
			data8c1=data8c1[1],
			data9c1=data9c1[1],
			data10c1=data10c1[1],
			data11c1=data11c1[1],
			data12c1=data12c1[1],
			data13c1=data13c1[1],
			data14c1=data14c1[1],
			data15c1=data15c1[1],
			data16c1=data16c1[1],
			data17c1=data17c1[1],
			data18c1=data18c1[1],
			data19c1=data19c1[1],
			my_temps1c1=db_temps1c1,
			my_temps2c1=db_temps2c1,
			my_temps3c1=db_temps3c1,
			my_temps4c1=db_temps4c1,
			my_temps5c1=db_temps5c1,
			my_temps6c1=db_temps6c1,
			my_temps7c1=db_temps7c1,
			my_temps8c1=db_temps8c1,
			my_temps9c1=db_temps9c1,
			my_temps10c1=db_temps10c1,
			my_temps11c1=db_temps11c1,
			my_temps12c1=db_temps12c1,
			my_temps13c1=db_temps13c1,
			my_temps14c1=db_temps14c1,
			my_temps15c1=db_temps15c1,
			my_temps16c1=db_temps16c1,
			my_temps17c1=db_temps17c1,
			my_temps18c1=db_temps18c1,
			my_temps19c1=db_temps19c1,
			rowsc2= retour2,
			data1c2=data1c2[1], 
			data2c2=data2c2[1], 
			data3c2=data3c2[1], 
			data4c2=data4c2[1], 
			data5c2=data5c2[1],
			data6c2=data6c2[1],
			data7c2=data7c2[1],
			data8c2=data8c2[1],
			data9c2=data9c2[1],
			data10c2=data10c2[1],
			data11c2=data11c2[1],
			data12c2=data12c2[1],
			data13c2=data13c2[1],
			data14c2=data14c2[1],
			data15c2=data15c2[1],
			data16c2=data16c2[1],
			data17c2=data17c2[1],
			data18c2=data18c2[1],
			data19c2=data19c2[1],
			my_temps1c2=db_temps1c2,
			my_temps2c2=db_temps2c2,
			my_temps3c2=db_temps3c2,
			my_temps4c2=db_temps4c2,
			my_temps5c2=db_temps5c2,
			my_temps6c2=db_temps6c2,
			my_temps7c2=db_temps7c2,
			my_temps8c2=db_temps8c2,
			my_temps9c2=db_temps9c2,
			my_temps10c2=db_temps10c2,
			my_temps11c2=db_temps11c2,
			my_temps12c2=db_temps12c2,
			my_temps13c2=db_temps13c2,
			my_temps14c2=db_temps14c2,
			my_temps15c2=db_temps15c2,
			my_temps16c2=db_temps16c2,
			my_temps17c2=db_temps17c2,
			my_temps18c2=db_temps18c2,
			my_temps19c2=db_temps19c2,
			rowsc3= retour3,
			data1c3=data1c3[1], 
			data2c3=data2c3[1], 
			data3c3=data3c3[1], 
			data4c3=data4c3[1], 
			data5c3=data5c3[1],
			data6c3=data6c3[1],
			data7c3=data7c3[1],
			data8c3=data8c3[1],
			data9c3=data9c3[1],
			data10c3=data10c3[1],
			data11c3=data11c3[1],
			data12c3=data12c3[1],
			data13c3=data13c3[1],
			data14c3=data14c3[1],
			data15c3=data15c3[1],
			data16c3=data16c3[1],
			data17c3=data17c3[1],
			data18c3=data18c3[1],
			data19c3=data19c3[1],
			my_temps1c3=db_temps1c3,
			my_temps2c3=db_temps2c3,
			my_temps3c3=db_temps3c3,
			my_temps4c3=db_temps4c3,
			my_temps5c3=db_temps5c3,
			my_temps6c3=db_temps6c3,
			my_temps7c3=db_temps7c3,
			my_temps8c3=db_temps8c3,
			my_temps9c3=db_temps9c3,
			my_temps10c3=db_temps10c3,
			my_temps11c3=db_temps11c3,
			my_temps12c3=db_temps12c3,
			my_temps13c3=db_temps13c3,
			my_temps14c3=db_temps14c3,
			my_temps15c3=db_temps15c3,
			my_temps16c3=db_temps16c3,
			my_temps17c3=db_temps17c3,
			my_temps18c3=db_temps18c3,
			my_temps19c3=db_temps19c3,
			rowsc4= retour4,
			data1c4=data1c4[1], 
			data2c4=data2c4[1], 
			data3c4=data3c4[1], 
			data4c4=data4c4[1], 
			data5c4=data5c4[1],
			data6c4=data6c4[1],
			data7c4=data7c4[1],
			data8c4=data8c4[1],
			data9c4=data9c4[1],
			data10c4=data10c4[1],
			data11c4=data11c4[1],
			data12c4=data12c4[1],
			data13c4=data13c4[1],
			data14c4=data14c4[1],
			data15c4=data15c4[1],
			data16c4=data16c4[1],
			data17c4=data17c4[1],
			data18c4=data18c4[1],
			data19c4=data19c4[1],
			my_temps1c4=db_temps1c4,
			my_temps2c4=db_temps2c4,
			my_temps3c4=db_temps3c4,
			my_temps4c4=db_temps4c4,
			my_temps5c4=db_temps5c4,
			my_temps6c4=db_temps6c4,
			my_temps7c4=db_temps7c4,
			my_temps8c4=db_temps8c4,
			my_temps9c4=db_temps9c4,
			my_temps10c4=db_temps10c4,
			my_temps11c4=db_temps11c4,
			my_temps12c4=db_temps12c4,
			my_temps13c4=db_temps13c4,
			my_temps14c4=db_temps14c4,
			my_temps15c4=db_temps15c4,
			my_temps16c4=db_temps16c4,
			my_temps17c4=db_temps17c4,
			my_temps18c4=db_temps18c4,
			my_temps19c4=db_temps19c4,
			rowsc5= retour5, 
			data1c5=data1c5[1], 
			data2c5=data2c5[1], 
			data3c5=data3c5[1], 
			data4c5=data4c5[1], 
			data5c5=data5c5[1],
			data6c5=data6c5[1],
			data7c5=data7c5[1],
			data8c5=data8c5[1],
			data9c5=data9c5[1],
			data10c5=data10c5[1],
			data11c5=data11c5[1],
			data12c5=data12c5[1],
			data13c5=data13c5[1],
			data14c5=data14c5[1],
			data15c5=data15c5[1],
			data16c5=data16c5[1],
			data17c5=data17c5[1],
			data18c5=data18c5[1],
			data19c5=data19c5[1],
			my_temps1c5=db_temps1c5,
			my_temps2c5=db_temps2c5,
			my_temps3c5=db_temps3c5,
			my_temps4c5=db_temps4c5,
			my_temps5c5=db_temps5c5,
			my_temps6c5=db_temps6c5,
			my_temps7c5=db_temps7c5,
			my_temps8c5=db_temps8c5,
			my_temps9c5=db_temps9c5,
			my_temps10c5=db_temps10c5,
			my_temps11c5=db_temps11c5,
			my_temps12c5=db_temps12c5,
			my_temps13c5=db_temps13c5,
			my_temps14c5=db_temps14c5,
			my_temps15c5=db_temps15c5,
			my_temps16c5=db_temps16c5,
			my_temps17c5=db_temps17c5,
			my_temps18c5=db_temps18c5,
			my_temps19c5=db_temps19c5,
			global_name=session.get('username'))
	else:
		return redirect(url_for('connexion'))

@app.route('/numbersearch', methods=['GET'])
def rnumber():
	cursor= connexiondb()
	try:
		if request.method == 'GET':
			rechercher = request.args.get('recherche')
			cursor.execute("SELECT donnee_capteur.temps, capteurs.libelle, capteurs.types, zone.nom_zone FROM capteurs, donnee_capteur, zone where donnee_capteur.capteurs_id_capteur = capteurs.id_capteur and capteurs.zone_id_zone = zone.id_zone and donnee = %s ", (rechercher))
			rows = cursor.fetchall()
			if len(rows) != 0:

				return jsonify({'result': render_template('searcher.html', serror=rechercher, rows=rows)})
			else:

				serror = "valeur non trouver"
				return jsonify({'result': render_template('searchererror.html', serror=serror)})
	except Exception, e:
		return str(e)

	return jsonify({'result': 'donnée perdu'})

@app.route('/stringsearch', methods=['GET'])
def rstring():
	cursor= connexiondb()
	try:
		if request.method == 'GET':
			rechercher = request.args.get('recherche')
			cursor.execute("SELECT capteurs.libelle, donnee_capteur.donnee, donnee_capteur.temps, capteurs.types FROM capteurs, donnee_capteur, zone where donnee_capteur.capteurs_id_capteur = capteurs.id_capteur and capteurs.zone_id_zone = zone.id_zone and nom_zone = %s", (rechercher))
			resultat1 = cursor.fetchall()
			cursor.execute("SELECT donnee_capteur.donnee, donnee_capteur.temps, capteurs.libelle, zone.nom_zone FROM capteurs, donnee_capteur, zone where donnee_capteur.capteurs_id_capteur = capteurs.id_capteur and capteurs.zone_id_zone = zone.id_zone and types = %s", (rechercher))
			resultat2 = cursor.fetchall()
			if len(resultat1) == 0 and len(resultat2) == 0:
				serror = "valeur non trouver"
				return jsonify({'result': render_template('searchererror.html', serror=serror)})
			if len(resultat1) != 0 and len(resultat2) ==0:
				return jsonify({'result':render_template('searcher.html', rows=resultat1, serror=rechercher)})
			else:
				return jsonify({'result':render_template('searcher.html', rows=resultat2, serror=rechercher)})
	except Exception, e:
		return str(e)

	return jsonify({'result': 'donnée perdu'})		

@app.route('/essai')
def delete():
	cnx = connectordb()
	cursor = cnx.cursor()
	deletemail = 'fabfly95@gmail.com'
	cnx.cursor().execute("DELETE FROM Administrateur WHERE email={};".format(thwart(deletemail)))
	delmsg = 'Compte supprimer !!'
	return str(delmsg)
if __name__ == '__main__':
	app.run(ssl_context=())

