
// Логика кнопки для обновления счётчика и отправки запроса
document.getElementById("tap-btn").addEventListener("click", () => {

    // Запрос к серверу
    // fetch('increment/', {
    fetch('/game/increment/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.redirect) {
            window.location.href = data.redirect;
            }
        // Обновляем счёт на основе ответа сервера, если он существует
        else if (data.count !== undefined) {
            document.getElementById('count').textContent = data.count;
        }
    })
    .catch(error => console.error('Ошибка:', error));
});
