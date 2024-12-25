
    document.addEventListener("DOMContentLoaded", function () {
        const firstNameElement = document.getElementById("user-first-name");
        const countElement = document.getElementById("count");

        // Функция для обновления данных
        function updateUserData() {
            fetch('/api/user-data/')
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    if (data.error) {
                        console.error("Error fetching user data:", data.error);
                    } else {
                        // Обновляем значения на странице
                        firstNameElement.textContent = data.first_name;
                        countElement.textContent = data.count;
                    }
                })
                .catch(error => console.error("Fetch error:", error));
        }

        // Первоначальная загрузка данных
        updateUserData();

        // Пример: автоматическое обновление каждые 10 секунд
        setInterval(updateUserData, 10000);
    });
