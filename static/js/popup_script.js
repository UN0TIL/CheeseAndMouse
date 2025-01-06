function showPopup(message) {
    const popup = document.getElementById('popup');
    const popupText = document.querySelector('.popup-text');
    document.getElementById("popup").classList.remove("hidden");
    popupText.textContent = message;
    popup.classList.remove('hidden');
}

function hidePopup() {
    const popup = document.getElementById('popup');
    popup.classList.add('hidden');
}

document.addEventListener('DOMContentLoaded', () => {
    // document.getElementById('popup-confirm').addEventListener('click', () => {
    //     alert('Буст активирован!');
    //     hidePopup();
    // });

    // Слушатель для кнопки подтверждения в попапе
    document.getElementById('popup-confirm').addEventListener('click', () => {
        alert('Буст активирован!');
        hidePopup();

        // Выполнение запроса после подтверждения
        fetch('/game/multiplier/', {
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



    document.getElementById('popup-cancel').addEventListener('click', () => {
        hidePopup();
    });
});