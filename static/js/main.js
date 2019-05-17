$(document.body).ready(function(){
		$("#capteur2").hide("fast");
		$("#capteur3").hide("fast");
		$("#capteur4").hide("fast");
		$("#capteur5").hide("fast");
		$("#Line-Chart-Capteur2").hide("fast");
		$("#Line-Chart-Capteur3").hide("fast");
		$("#Line-Chart-Capteur4").hide("fast");
		$("#Line-Chart-Capteur5").hide("fast");

		$("li.btn1").on('click', function(){
			$("#capteur3").hide("slow").delay(3000);
			$("#capteur4").hide("slow").delay(3000);
			$("#capteur2").hide("slow").delay(3000);
			$("#capteur5").hide("slow").delay(3000);
			$("#Line-Chart-Capteur3").hide("slow").delay(3000);
			$("#Line-Chart-Capteur4").hide("slow").delay(3000);
			$("#Line-Chart-Capteur2").hide("slow").delay(3000);
			$("#Line-Chart-Capteur5").hide("slow").delay(3000);
			$("#Line-Chart-Capteur1").show("slow");
			$("#zoomreset").attr('onclick', 'resetZoom()');
			$("#capteur1").show("slow");

		});
		$("li.btn2").on('click', function(){
			if ($("#capteur1").not(':hidden') && $("#capteur5").not(':hidden') && $("#capteur3").not(':hidden') && $("#capteur4").not(':hidden') && $("#Line-Chart-Capteur1").not(':hidden') && $("#Line-Chart-Capteur3").not(':hidden') && $("#Line-Chart-Capteur4").not(':hidden') && $("#Line-Chart-Capteur5").not(':hidden')) {
				$("#capteur1").hide("slow").delay(3000);
				$("#capteur3").hide("slow").delay(3000);
				$("#capteur4").hide("slow").delay(3000);
				$("#capteur5").hide("slow").delay(3000);
				$("#Line-Chart-Capteur1").hide("slow").delay(3000);
				$("#Line-Chart-Capteur3").hide("slow").delay(3000);
				$("#Line-Chart-Capteur4").hide("slow").delay(3000);
				$("#Line-Chart-Capteur5").hide("slow").delay(3000);

			}
			$("#Line-Chart-Capteur2").show("slow");
			$("#zoomreset").attr('onclick', 'resetZoom2()');
			$("#capteur2").show("slow");
		});
		$("li.btn3").on('click', function(){
			if ($("#capteur1").not(':hidden') && $("#capteur5").not(':hidden') && $("#capteur2").not(':hidden') && $("#capteur4").not(':hidden') && $("#Line-Chart-Capteur1").not(':hidden') && $("#Line-Chart-Capteur2").not(':hidden') && $("#Line-Chart-Capteur4").not(':hidden') && $("#Line-Chart-Capteur5").not(':hidden')) {
				$("#capteur1").hide("slow").delay(3000);
				$("#capteur2").hide("slow").delay(3000);
				$("#capteur4").hide("slow").delay(3000);
				$("#capteur5").hide("slow").delay(3000);
				$("#Line-Chart-Capteur1").hide("slow").delay(3000);
				$("#Line-Chart-Capteur2").hide("slow").delay(3000);
				$("#Line-Chart-Capteur4").hide("slow").delay(3000);
				$("#Line-Chart-Capteur5").hide("slow").delay(3000);

			}
			$("#Line-Chart-Capteur3").show("slow");
			$("#zoomreset").attr('onclick', 'resetZoom3()');
			$("#capteur3").show("slow");
		});
		$("li.btn4").on('click', function(){
			if ($("#capteur1").not(':hidden') && $("#capteur5").not(':hidden') && $("#capteur3").not(':hidden') && $("#capteur2").not(':hidden') && $("#Line-Chart-Capteur1").not(':hidden') && $("#Line-Chart-Capteur2").not(':hidden') && $("#Line-Chart-Capteur3").not(':hidden') && $("#Line-Chart-Capteur5").not(':hidden')) {
				$("#capteur1").hide("slow").delay(3000);
				$("#capteur3").hide("slow").delay(3000);
				$("#capteur2").hide("slow").delay(3000);
				$("#capteur5").hide("slow").delay(3000);
				$("#Line-Chart-Capteur1").hide("slow").delay(3000);
				$("#Line-Chart-Capteur2").hide("slow").delay(3000);
				$("#Line-Chart-Capteur3").hide("slow").delay(3000);
				$("#Line-Chart-Capteur5").hide("slow").delay(3000);

			}
			$("#Line-Chart-Capteur4").show("slow");
			$("#zoomreset").attr('onclick', 'resetZoom4()');
			$("#capteur4").show("slow");
		});
		$("li.btn5").on('click', function(){
			if ($("#capteur1").not(':hidden') && $("#capteur2").not(':hidden') && $("#capteur3").not(':hidden') && $("#capteur4").not(':hidden') && $("#Line-Chart-Capteur1").not(':hidden') && $("#Line-Chart-Capteur2").not(':hidden') && $("#Line-Chart-Capteur3").not(':hidden') && $("#Line-Chart-Capteur4").not(':hidden')) {
				$("#capteur1").hide("slow").delay(3000);
				$("#capteur3").hide("slow").delay(3000);
				$("#capteur4").hide("slow").delay(3000);
				$("#capteur2").hide("slow").delay(3000);
				$("#Line-Chart-Capteur1").hide("slow").delay(3000);
				$("#Line-Chart-Capteur2").hide("slow").delay(3000);
				$("#Line-Chart-Capteur3").hide("slow").delay(3000);
				$("#Line-Chart-Capteur4").hide("slow").delay(3000);

			}
			$("#Line-Chart-Capteur5").show("slow");
			$("#zoomreset").attr('onclick', 'resetZoom5()');
			$("#capteur5").show("slow");
		});

	});