// Начальное количество сыра
let cheeseCount = 5;

// Обновление отображения счетчика
function updateCheeseCount() {
    document.getElementById("cheese-count").textContent = cheeseCount;
}

// Функция добавления очков
function addPoints(points) {
    // Обновляем количество очков (если это необходимо)
    // cheeseCount += points;
    // updateCheeseCount();
    // alert(`+${points} Cheese!`);

    // Переместим обработчик события вне функции addPoints
    document.getElementById("task-icon").addEventListener("click", () => {
        const numberToSend = points; // Используем переданное значение points

        // Запрос к серверу
        fetch('/increment/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ number: numberToSend }) // Передаем число в теле запроса
        })
        .then(response => {
            if (response.redirected) {
                // Если сервер отправляет редирект, перенаправляем на новый URL
                window.location.href = response.url;
            } else {
                return response.json(); // Обрабатываем ответ, если нет редиректа
            }
        })
        .then(data => {
            console.log(data); // Обрабатываем данные, если нужно
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
    });
}


// Инициализация
updateCheeseCount();


// Что-то новое

