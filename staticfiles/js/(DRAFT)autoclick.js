// Функция для получения CSRF-токена из cookies
function getCSRFToken() {
    const name = 'csrftoken';
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        let [key, value] = cookie.trim().split('=');
        if (key === name) return value;
    }
    return '';
}

// Функция для отправки POST-запроса на сервер
function sendAutoClickRequest() {
    fetch('/autoclick/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCSRFToken(), // Получаем CSRF-токен
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        // Обновляем счётчик на странице
        if (data.count !== undefined) {
            document.getElementById('count').textContent = data.count;
        }
    })
    .catch(error => console.error('Ошибка при автоклике:', error));
}

// Функция для запуска автоклика с заданным интервалом
function startAutoClick(interval = 1000) {
    // Проверяем, чтобы автоклик не запускался повторно
    if (!window.autoClickInterval) {
        window.autoClickInterval = setInterval(() => {
            sendAutoClickRequest();
        }, interval); // Интервал в миллисекундах
        console.log('Автоклик запущен');
    }
}

// Привязываем запуск автоклика к кнопке
document.getElementById('startAutoClick').addEventListener('click', () => {
    startAutoClick(); // Запускаем автоклик
});
