
// document.getElementById("menu-btn").addEventListener("click", function () {
//     var sidebar = document.getElementById("sidebar");
//     if (sidebar.style.left === "0px") {
//         sidebar.style.left = "-300px"; // Скрыть боковую панель
//     } else {
//         sidebar.style.left = "0px"; // Показать боковую панель
//     }
// });



const loginForm = document.getElementById('login-form');

loginForm.addEventListener('submit', handleLoginFormSubmit);

async function handleLoginFormSubmit(e) {
    e.preventDefault();

    try {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        const response = await fetch('http://127.0.0.1:8000/auth/jwt/create/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        if (!response.ok) {
            // Если ответ не успешный, выбросить ошибку с текстом статуса
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data);  // Логируем полный ответ для проверки

        if (data.access && data.refresh) {
            localStorage.setItem('access', data.access);
            localStorage.setItem('refresh', data.refresh);
            window.location.href = '../templates/profile.html';
        } else {
            console.error('Expected tokens not found in response:', data);
        }
    } catch (error) {
        console.error('Login failed:', error.message);
    }
}
