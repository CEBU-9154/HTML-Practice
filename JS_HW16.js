window.onload = function () {
    var count = 0;
    var display=document.getElementById("counter")
    var buttonAdd = document.getElementById("button-add");
    var buttonSub = document.getElementById("button-sub");
    var buttonReset = document.getElementById("button-reset");

    buttonAdd.onclick = function () {
        count++;
        updateDisplay();
    }

    buttonSub.onclick = function () {
        count--;
        updateDisplay();
    }

    buttonReset.onclick = function () {
        count=0;
        updateDisplay();
    }

    function updateDisplay() {
        display.innerHTML=count < 10 ? "0" + count: count;
    }
    updateDisplay()
};