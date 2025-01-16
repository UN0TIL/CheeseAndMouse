README (Українська версія)

🌈 Опис

Це мій маленький pet-проєкт, у якому я спробував відтворити механіки популярних клікерів у Telegram.
Якщо ви хочете використати код для власних потреб, беріть без проблем. Єдине, мені було б приємно, якби ви згадали мене.

🔧 Налаштування

Якщо у вас немає виділеного сервера, але хочеться спробувати проєкт, завантажте і скористайтеся утилітою ngrok. Налаштування дуже просте:

Завантажте ngrok і запустіть його. Ви отримаєте адресу сайту для підключення до вашого проєкту звідки завгодно через HTTPS (це обов'язкова умова для Web Apps Telegram).

Скопіюйте адресу, надану ngrok, у поле CSRF_TRUSTED_ORIGINS у settings.py (рядок 51).

Створіть Web App у Telegram через Bot Father. Додайте посилання, надане ngrok, у налаштування бота.

Запустіть проєкт за допомогою python manage.py runserver.

🌟 Функції

Користувач: Аутентифікація користувача.

Клікер: Основний ігровий елемент.

Множник: Буст, що збільшує кількість очок за одне натискання.

Завдання: Створюються через панель адміністратора. Завдання з'являються в окремій вкладці "Tasks".

🧑‍💻 СуперКористувач

Логін: user

Пароль: 111


|============================================================================|


README (English Version)

🌈 Description

This is my small pet project where I tried to replicate the mechanics of popular clicker games on Telegram.
If you'd like to use the code for your own purposes, feel free to do so. The only thing I ask is to give me credit.

🔧 Setup

If you don't have a dedicated server but want to try the project, download and use the ngrok utility. Setup is very simple:

Download ngrok and run it. You'll receive a site address that allows you to connect to your project from anywhere via HTTPS (a mandatory requirement for Telegram Web Apps).

Copy the address provided by ngrok into the CSRF_TRUSTED_ORIGINS field in settings.py (line 51).

Create a Web App in Telegram using Bot Father. Add the link provided by ngrok to your bot's settings.

Start the project with python manage.py runserver.

🌟 Features

User: User authentication.

Clicker: The main gameplay element.

Multiplier: Boosts that increase the number of points per click.

Tasks: Created via the admin panel. Tasks appear in the separate "Tasks" tab.

🧑‍💻 SuperUser

Login: user

Password: 111


|============================================================================|


README

🌈 Описание

Это мой маленький pet-проект, в котором я постарался повторить механики нашумевших кликеров в Telegram.
Если вдруг вы хотите воспользоваться кодом для собственных нужд, берите без проблем. Единственное, мне было бы приятно, если бы вы упомянули меня.

🔧 Настройка

Если у вас нет выделенного сервера, но хочется попробовать проект, скачайте и воспользуйтесь утилитой ngrok. Настройка очень простая:

Скачайте ngrok и запустите его. Вы получите адрес сайта для подключения к вашему проекту откуда угодно по HTTPS (это обязательное условие для Web Apps Telegram).

Адрес, выделенный ngrok, скопируйте в поле CSRF_TRUSTED_ORIGINS в settings.py (строка 51).

Создайте Web App в Telegram через Bot Father. Добавьте ссылку, выданную ngrok, в настройки бота.

Запустите проект через python manage.py runserver.

🌟 Рабочие функции

Пользователь: Аутентификация пользователя.

Кликер: Самый важный геймплейный элемент.

Множитель: При покупке буста увеличивает кол-во очков за одно нажатие.

Задания: Создаются через панель администратора. Задания появляются в отдельной вкладке Tasks.

🧑‍💻 СуперПользователь

Логин: user

Пароль: 111



