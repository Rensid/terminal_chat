import { auth_token } from "./auth/token.js";
const url = 'http://localhost:8000/users/profile';

// // Функция для получения данных пользователя с сервера
async function getUserData() {
    try {
        const response = await fetch('http://127.0.0.1:8000/users/profile/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
            // Дополнительные настройки запроса, если необходимо
        });
        if (response.ok) {
            // Если ответ успешный, получаем данные пользователя
            const userData = await response.json();
            // Здесь можно обработать полученные данные и отобразить на странице
            displayUserData(userData);
        } else {
            // Если ответ не успешный, обрабатываем ошибку
            console.error('Ошибка при получении данных пользователя:', response.statusText);
        }
    } catch (error) {
        // Если произошла ошибка при выполнении запроса
        console.error('Ошибка при выполнении запроса:', error);
    }
}


window.onload = async function () {
    const access = localStorage.getItem('access');
    const refresh = localStorage.getItem('refresh');
    const response = await (await auth_token(access, url)).json()
    const { first_name, last_name, username, email } = response.data;
    console.log(response)

    document.querySelector('#first_name').value = first_name;
    document.querySelector('#last_name').value = last_name;
    document.querySelector('#username').value = username;
    document.querySelector('#email').value = email;
}

