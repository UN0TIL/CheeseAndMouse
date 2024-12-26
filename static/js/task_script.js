// Начальное количество сыра
let cheeseCount = 5;

// Обновление отображения счетчика
// function updateCheeseCount() {
//     document.getElementById("cheese-count").textContent = cheeseCount;
// }

// Функция добавления очков
function addPoints(points) {
    // Запрос к серверу
    fetch('/mission/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ points: [points] })
    })
    .then(response => response.json())
    .then(data => {
        if (data.count !== undefined) {
            document.getElementById('count').textContent = data.count;
        }
    })
    .catch(error => console.error('Ошибка:', error));
}



// Инициализация
updateCheeseCount();


// Что-то новое

