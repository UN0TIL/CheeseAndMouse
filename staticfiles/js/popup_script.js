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
    document.getElementById('popup-confirm').addEventListener('click', () => {
        alert('Буст активирован!');
        hidePopup();
    });

    document.getElementById('popup-cancel').addEventListener('click', () => {
        hidePopup();
    });
});