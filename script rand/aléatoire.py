import time
import mysql.connector
import random
#importations des modules a utilise

print("___capteurs___|___Valeurs___\n")

i = 1
#boucle sans fin
while i < 11:
	if i != 10:
		#connexion a la base de donne
		cnx = mysql.connector.connect(user='root', password='laisse-le-pc', host='localhost', database='donne_rcp' )
		#lancement du curseur
		cursor = cnx.cursor()
		#initialisation de la graine
		seed = int(time.time())
		a = -50-i
		m = 70
		i += 1
		#formule de generation aleatoire pour capteur 1
		varrandom = (a*seed)%m
		#varalea = random.rand(-50, 150)

		#requete sql capteur1
		dd = "INSERT INTO donnee_capteur (donnee, temps, capteurs_id_capteur, capteurs_zone_id_zone) VALUES (%(alea1)s, now(), %(capteurid)s, %(zoneid)s)"
		donne = {

		'alea1': varrandom,
		'capteurid': 101,
		'zoneid': 298018
		}
		#execution de la requete
		cursor.execute(dd, donne)
		cnx.commit()
		
		#generation de data pour le capteur2
		varrand2 = random.randint(-20, 50)
		#requete sql capteur2
		dd2 = "INSERT INTO donnee_capteur (donnee, temps, capteurs_id_capteur, capteurs_zone_id_zone) VALUES (%(alea2)s, now(), %(capteurid2)s, %(zoneid2)s)"
		donne2 = {

		'alea2': varrand2,
		'capteurid2': 105,
		'zoneid2': 3143
		}
		#execution de la requete
		cursor.execute(dd2, donne2)
		cnx.commit()

		#generation de data pour le capteur3
		varrand3 = random.randint(-10, 100)
		#requete sql capteur3
		dd3 = "INSERT INTO donnee_capteur (donnee, temps, capteurs_id_capteur, capteurs_zone_id_zone) VALUES (%(alea3)s, now(), %(capteurid3)s, %(zoneid3)s)"
		donne3 = {

		'alea3': varrand3,
		'capteurid3': 102,
		'zoneid3': 298018
		}
		#execution de la requete
		cursor.execute(dd3, donne3)
		cnx.commit()

		#generation de data pour le capteur4
		varrand4 = random.randint(0, 90)
		#requete sql capteur4
		dd4 = "INSERT INTO donnee_capteur (donnee, temps, capteurs_id_capteur, capteurs_zone_id_zone) VALUES (%(alea4)s, now(), %(capteurid4)s, %(zoneid4)s)"
		donne4 = {
		'alea4': varrand4,
		'capteurid4': 103,
		'zoneid4': 3
		}
		#execution de la requete
		cursor.execute(dd4, donne4)
		cnx.commit()

		#generation de data pour le capteur5
		varrand5 = random.randint(20, 70)
		#requete sql capteur5
		dd5 = "INSERT INTO donnee_capteur (donnee, temps, capteurs_id_capteur, capteurs_zone_id_zone) VALUES (%(alea5)s, now(), %(capteurid5)s, %(zoneid5)s)"
		donne5 = {
		'alea5': varrand5,
		'capteurid5': 104,
		'zoneid5': 4133
		}
		#execution de la requete
		cursor.execute(dd5, donne5)

		cnx.commit()
		cursor.close()
		cnx.close()

		print("   capteur1   :   {}   \n   capteur2   :   {}   \n   capteur3   :   {}   \n   capteur4   :   {}   \n   capteur5   :   {}  ".format(varrandom, varrand2, varrand3, varrand4, varrand5))
		time.sleep(100)
		


	else:
		i = i-9
				
