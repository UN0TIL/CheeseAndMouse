document.getElementById('clickButton').addEventListener('click', function () {
    fetch('/increment/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.count !== undefined) {
            document.getElementById('count').textContent = data.count;
        }
    })
    .catch(error => console.error('Ошибка:', error));
});