let tg = window.Telegram.WebApp; // Получаем объект webapp телеграма

tg.expand(); // Расширяем на все окно

let usercard = document.getElementById("name"); // Блок usercard

let profName = document.createElement('p'); // Создаем параграф
profName.innerText = `${tg.initDataUnsafe.user.first_name}
${tg.initDataUnsafe.user.last_name}`
// ${tg.initDataUnsafe.user.username} // (${tg.initDataUnsafe.user.language_code})`;
usercard.appendChild(profName); // Добавляем параграф


let userid = document.createElement('p'); // Создаем еще параграф
userid.innerText = `${tg.initDataUnsafe.user.id}`; // Показываем user_id
usercard.appendChild(userid); // Добавляем параграф

