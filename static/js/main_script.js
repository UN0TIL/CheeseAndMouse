// Счетчик сыра
// let cheeseCount = 5;

// Таймер для Boost
let timer = 3 * 60 + 15; // В секундах: 3 минуты и 15 секунд

// Обновление счетчика сыра и таймера
// const cheeseCounter = document.getElementById("count");
const timerDisplay = document.getElementById("timer");


function updateTimer() {
    const minutes = Math.floor(timer / 60);
    const seconds = timer % 60;
    timerDisplay.textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
}

// Таймер обратного отсчета
// setInterval(() => {
//     if (timer > 0) {
//         timer--;
//         updateTimer();
//     }
// }, 1000);

// Логика кнопки для обновления счётчика и отправки запроса
document.getElementById("tap-btn").addEventListener("click", () => {


    // Локальное обновление счётчика
    // cheeseCount++;
    // cheeseCounter.textContent = cheeseCount;

    // Запрос к серверу
    fetch('/increment/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        // Обновляем счёт на основе ответа сервера, если он существует
        if (data.count !== undefined) {
            document.getElementById('count').textContent = data.count;
        }
    })
    .catch(error => console.error('Ошибка:', error));
});

// Инициализация таймера
updateTimer();
