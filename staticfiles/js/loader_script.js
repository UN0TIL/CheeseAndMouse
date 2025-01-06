document.addEventListener("DOMContentLoaded", function () {
    const assets = [
        { type: "style", url: "/static/css/styles.css" },
        { type: "image", url: "/static/media/mouse.png" },
        { type: "image", url: "/static/media/cheese.png" },
        { type: "image", url: "/static/media/profile.png" },
    ];

    let loadedAssets = 0;

    function checkIfAllLoaded() {
        loadedAssets++;
        if (loadedAssets === assets.length) {
            // После загрузки всех ресурсов выполните запрос к save_user_data
            fetch('/game/save_user_data/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    first_name: 'Кто-то',
                    username: 'chtotoktotomaybe',
                    language_code: 'ru',
                    user_id: 7576807686,
                    is_premium: false
                })
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Не удалось сохранить пользователя');
                }
                return response.json();
            })
            .then(data => {
                console.log('Пользователь сохранен:', data);
                // После успешного завершения запроса выполняем редирект
                window.location.href = "/game/tap";
            })
            .catch(error => console.error('Ошибка при выполнении запроса к save_user_data:', error));
        }
    }

    assets.forEach(asset => {
        if (asset.type === "script") {
            const script = document.createElement("script");
            script.src = asset.url;
            script.onload = checkIfAllLoaded;
            script.onerror = () => console.error(`Ошибка загрузки ${asset.url}`);
            document.body.appendChild(script);
        } else if (asset.type === "style") {
            const link = document.createElement("link");
            link.rel = "stylesheet";
            link.href = asset.url;
            link.onload = checkIfAllLoaded;
            link.onerror = () => console.error(`Ошибка загрузки ${asset.url}`);
            document.head.appendChild(link);
        } else if (asset.type === "image") {
            const img = new Image();
            img.src = asset.url;
            img.onload = checkIfAllLoaded;
            img.onerror = () => console.error(`Ошибка загрузки ${asset.url}`);
        }
    });
});

