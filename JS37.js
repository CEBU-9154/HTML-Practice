var c = prompt("Welcome to the Area Calculator! \n Plese choose an option. \n a. Area of Rectangle \n b. Area of Triangle \n c. Area of Circle \n d. Area of Pararellogram")

if (c=='a') {
    var l=prompt("Enter the length")
    var b = prompt("Enter the breadth")
    var result=Number(l) * Number(b)
    alert('The Area is '+ result)
}

if (c == 'b') {
    var h = prompt("Enter the height")
    var b = prompt("Enter the base")
    var result = Number(h) * Number(b) /2
    alert('The Area is ' + result)
}

if (c == 'c') {
    var r = prompt("Enter the radius")
    var result =3.14*Number(r)*Number(r)
    alert('The Area is ' + result)
}

if (c == 'd') {
    var h = prompt("Enter the height")
    var cb = prompt("Enter the corroesponding base")
    var result = Number(h) * Number(cb)
    alert('The Area is ' + result)
}