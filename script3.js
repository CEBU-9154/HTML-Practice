function validate(e) {
    const user = document.getElementById("user").value;
    e.preventDefault();
    const email = document.getElementById("email").value;
    const pass = document.getElementById("password").value;
    const age = document.getElementById("age").value;
    const gender = document.getElementById("gender").value;
    const birth = document.getElementById("birthday").value;
    const msgBox = document.getElementById("message");
    let message = '';
    if (user === '') {
        message = 'user should be 3 characters or more.'
        msgBox.style.color = 'red'}
    else if (email === '') {
        message = 'please enter an email.'
        msgBox.style.color = 'red'
    }
    else if (pass === '') {
        message = 'password must be atleast 8 characters.'
        msgBox.style.color = 'red'
    }
    else if (age === '') {
        message = 'please enter your age.'
        msgBox.style.color = 'red'
    }
    else if (gender === '') {
        message = 'please choose a gender.'
        msgBox.style.color = 'red'
    }
    else if (birth === '') {
        message = 'please enter your birthday.'
        msgBox.style.color = 'red'
    }
    else {
        message = 'Account made.';
        msgBox.style.color = 'green';
    }
    msgBox.innerText = message;
}