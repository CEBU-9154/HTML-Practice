var c = prompt("Welcome to the Perimeter Calculator! \n Plese choose an option. \n a. Perimeter of Rectangle \n b. Perimer of Square \n c. Area of Circle \n d. Area of Kite")

if (c == 'a') {
    var s = prompt("Enter the side")
    var b = prompt("Enter the breadth")
    var result = 2 * Number(l) * Number(b)
    alert('The Perimeter is ' + result)
}

if (c == 'b') {
    var s = prompt("Enter the side")
    var result = Number(s) * 4
    alert('The Perimeter is ' + result)
}

if (c == 'c') {
    var d = prompt("Enter the diameter")
    var result = 3.14 * Number(d)
    alert('The Perimeter is ' + result)
}

if (c == 'd') {
    var s1 = prompt("Enter side 1")
    var s2 = prompt("Enter side 2")
    var result = Number(s1) + Number(s2) * 2
    alert('The Perimeter is ' + result)
}