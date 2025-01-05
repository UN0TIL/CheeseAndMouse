// // Функция добавления очков
//
// document.addEventListener('DOMContentLoaded', () => {
//     document.querySelectorAll('.task-item').forEach(item => {
//         item.addEventListener('click', () => {
//             const points = item.dataset.points;
//             const id = item.dataset.id;
//             if (points && id) {
//                 addPoints(points, id);
//             } else {
//                 console.error("Некорректные данные задачи", { points, id });
//             }
//         });
//     });
// });


function addPoints(point, id) {
    // Запрос к серверу

    // fetch('/mission/', {
    fetch('/game/mission/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            'Content-Type': 'application/json',
        },

        body: JSON.stringify({ point: [point], id: [id] })
    })
    .then(response => response.json())
    .then(data => {
        if (data.count !== undefined) {
            document.getElementById('count').textContent = data.count;
        }
    })
    .catch(error => console.error('Ошибка:', error));
}