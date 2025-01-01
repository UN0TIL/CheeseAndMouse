const tg = window.Telegram.WebApp; // Telegram WebApp API

tg.expand()


// Получаем данные пользователя
const userData = {
    first_name: tg.initDataUnsafe.user.first_name || '',
    username: tg.initDataUnsafe.user.username || '',
    language_code: tg.initDataUnsafe.user.language_code || '',
    user_id: tg.initDataUnsafe.user.id || '',
    is_premium: tg.initDataUnsafe.user.is_premium || false
};


// Отправляем данные на Django backend
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value; // Получаем CSRF-токен из шаблона

fetch('/save_user_data/', { // Укажите правильный URL для вашего Django вью
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken
    },
    body: JSON.stringify(userData) // Передаем данные в формате JSON
})
    .then((response) => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then((data) => {
        console.log('User data successfully sent to backend:', data);
    })
    .catch((error) => {
        console.error('Error sending user data:', error);
    });