window.onload=function () {
    var seconds = 00 ; 
    var milliseconds = 00;
    var appendmilleseconds=document.getElementById("milliseconds");
    var appendSeconds = document.getElementById("seconds");
    var buttonStart = document.getElementById("button-start");
    var buttonStop = document.getElementById("button-stop");
    var buttonReset = document.getElementById("button-reset");
    var Interval;

    buttonStart.onclick=function(){
        clearInterval(Interval);
        Interval=setInterval(startTime, 10);
    }

    buttonStop.onclick=function(){
        clearInterval(Interval);
        Interval=setInterval(startTimer, 10);
    }

    buttonReset.onclick=function(){
        clearInterval(Interval);
        var seconds = 0;
        var milliseconds = 0;
        appendmilleseconds.innerHTML=milliseconds;
        appendSeconds.innerHTML=seconds;
    }

    function startTime() {
        milliseconds++;

        if(milliseconds <= 9) {
            appendmilleseconds.innerHTML="0"+milliseconds;
        }
        if(milliseconds>9){
            appendmilleseconds.innerHTML=milliseconds;
        }
        if (milliseconds > 99) {
            seconds++;
            appendSeconds.innerHTML="0" +seconds;
            milliseconds=0;
            appendmilleseconds.innerHTML=seconds;
        }
    }
}
startTime()