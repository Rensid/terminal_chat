
// получаем форму со страницы по ее id 
const registrationForm = document.getElementById('registration-form');


// добавляем ожидание события нажатия на кнопку
registrationForm.addEventListener('submit', handleRegisterFormSubmit);

async function handleRegisterFormSubmit(event) {
    event.preventDefault();
    
    try {
        // получаем все значения с формы. не забывать дописывать .value
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        const first_name = document.getElementById('first_name').value;
        const last_name = document.getElementById('last_name').value;
        const email = document.getElementById('email').value;


        // отправляет POST запрос на эндпоинт для создания пользователя передавая все собранные с формы данные
        const response = await fetch('http://127.0.0.1:8000/users/users/',
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, password, first_name, last_name, email })
            }
        )
        // для проверки, что все данные собраны корректно
        console.log(JSON.stringify({ username, password, first_name, last_name, email }))
        
        
        // переадресация на страницу авторизации в случае успешное регистрации
        // TODO: нужно потом попробовать сделать так, чтобы сразу же после регистрации создавался токен
        // TODO: и переадресовывал на профиль
        if (response.ok) {
            window.location.href = '../templates/login.html';
        }
        // если запрос вернулся с ошибкой, то конвертируем ответ в json и вытаскиваем из него ошибку
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


