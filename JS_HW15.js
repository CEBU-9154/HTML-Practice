function showDate() {
var date = new Date();
var d = date.getDate();
var m = date.getMonth();
var y = date.getFullYear();
var d1 = date.getDay();

var time = d + ":" + m + ":" + y + ":" + d1 + ":";
document.getElementById("showDate").innerText = time;
}

showDate()