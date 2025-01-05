// Удаление задания и обновление страницы или интерфейса
function deleteTask(taskId) {
    // Выполняем POST-запрос на сервер для удаления задания
    fetch('/mission/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id: [taskId], point: [0] }) // Передаём ID задачи
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            console.log(data.message); // Логируем успешное удаление
        }
        // Обновляем интерфейс: удаляем строку задания из таблицы
        const taskRow = document.querySelector(`[data-task-id="${taskId}"]`);
        if (taskRow) {
            taskRow.remove(); // Удаляем элемент из DOM
        }
    })
    .catch(error => console.error('Ошибка при удалении задания:', error));
}

// Добавление очков
function addPoints(points) {
    // Выполняем запрос к серверу
    fetch('/mission/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ points: [points] }) // Передаём очки
    })
    .then(response => response.json())
    .then(data => {
        if (data.count !== undefined) {
            document.getElementById('count').textContent = data.count; // Обновляем значение счётчика на странице
        }
    })
    .catch(error => console.error('Ошибка:', error));
}

// Привязка событий к кнопкам удаления после загрузки страницы
document.addEventListener('DOMContentLoaded', () => {
    const deleteButtons = document.querySelectorAll('.delete-button');
    deleteButtons.forEach(button => {
        button.addEventListener('click', event => {
            const taskId = button.getAttribute('data-task-id'); // Получаем ID задачи
            deleteTask(taskId); // Вызываем функцию удаления задачи
        });
    });

    // Инициализация обновления счётчика (это будет ваш метод из текущего кода)
    updateCheeseCount();
});