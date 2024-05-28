const registrationForm = document.getElementById('registration-form');

registrationForm.addEventListener('submit', handleRegisterFormSubmit);

async function handleRegisterFormSubmit(event) {
    event.preventDefault();

    try {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        const first_name = document.getElementById('first_name').value;
        const last_name = document.getElementById('last_name').value;
        const email = document.getElementById('email').value;

        const response = await fetch('http://127.0.0.1:8000/users/users/',
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, password, first_name, last_name, email })
            }
        )
        console.log(JSON.stringify({ username, password, first_name, last_name, email }))
        if (response.ok) {
            window.location.href = '../templates/login.html';
        }
        else {
            const errorData = await response.json();
            console.error('HTTP error:', errorData);
            throw new Error(`HTTP errror! status: ${response.status}`);
        }

    }
    catch (error) {
        console.error('Registration failed:', error.message);
    }
}


