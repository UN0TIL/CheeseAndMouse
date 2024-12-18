// Ждём загрузки DOM
document.addEventListener('DOMContentLoaded', () => {
    // Находим элементы
    const counterElement = document.getElementById('counter');
    const clickerButton = document.getElementById('clickerButton');

    // Счётчик кликов
    let clicks = 0;

    // Добавляем обработчик события
    clickerButton.addEventListener('click', () => {
        clicks++;
        counterElement.textContent = `Clicks: ${clicks}`;
    });
});