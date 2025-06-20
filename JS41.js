var dice;
var dices=['&#9856;', '&#9857;', '&#9858;', '&#0860;', '&#9861;'];
var stopped=true;
var t;

function change() {
    var random=Math.floor(Math.random()*6);
    dice.innerHTML=dices[random];
}