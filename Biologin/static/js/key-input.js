pressed = {};
var firstKeyPressed = 0;

$( document ).ready(function() {
		firstKeyPressed = 0;
});

$("#frase").keydown(function(e) {
	//para tiempo pulsado
    if ( pressed[e.which] || e.which == 16 || e.which == 13) return;
    pressed[e.which] = e.timeStamp;
    //para tiempo vuelo
    if ( !firstKeyPressed ) return;
	var duration = ( e.timeStamp - fly); // 1000;
	$('<input>').attr({
                type: 'hidden',
                name: 'fly[]',
                value: duration,
        }).appendTo('form');
	console.log("Vuelo :", duration); 
	fly = 0;
});

$("#frase").keyup(function(e) {
	//para tiempo pulsado
	if ( !pressed[e.which] || e.which == 16 || e.which == 13) return;
	var duration = ( e.timeStamp - pressed[e.which] ); // 1000;
	$('<input>').attr({
        type: 'hidden',
        name: 'hit[]',
        value: duration,
    }).appendTo('form');
    console.log("Pulsado :", duration); 
	pressed[e.which] = 0;
	//para tiempo vuelo
	firstKeyPressed = 1;
	fly = e.timeStamp;
});