document.getElementById('multiplier_button').addEventListener('click', function () {
    fetch('/multiplier/', {
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
        if (data.multiplier !== undefined) {
            document.getElementById('multiplier').textContent = data.multiplier;
        }
    })
    .catch(error => console.error('Ошибка:', error));
});