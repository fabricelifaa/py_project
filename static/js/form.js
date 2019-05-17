$(document).ready(function(){
	
	$('form').on('submit', function(event){
		var recu = $('input').val();
		
		if(recu > -1000){
			$.ajax({
				data: {
					recherche: $('input').val()
				},
				url: 'numbersearch',
				type: 'GET'
			}).done(function(resp){
				$('#content-result').append(resp.result);
				$('#content-div').show('slow');
				$('#btnclose').on('click', function(){
					$('#content-div').hide('slow');
					$('#content-result').empty();
				});
			})}
			else{
				$.ajax({
				data: {
					recherche: $('input').val()
				},
				url: '/stringsearch',
				type: 'GET'
			}).done(function(resp){
				$('#content-result').append(resp.result);
				$('#content-div').show('slow');
				$('#btnclose').on('click', function(){
					$('#content-div').hide('slow');
					$('#content-result').empty();
				});
			})
			};
		event.preventDefault();
	});
});