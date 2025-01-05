
document.addEventListener("DOMContentLoaded", function () {
  const assets = [
    // { type: "script", url: "/static/js/authentication_script.js" },
//     { type: "script", url: "/static/js/main_script.js" },
//     { type: "script", url: "/static/js/task_script.js" },
    { type: "style", url: "/static/css/styles.css" },
    { type: "image", url: "/static/media/mouse.png" },
    { type: "image", url: "/static/media/cheese.png" },
    { type: "image", url: "/static/media/profile.png" },
  ];

  let loadedAssets = 0;

  function checkIfAllLoaded() {
    loadedAssets++;
    if (loadedAssets === assets.length) {
      // document.body.innerHTML = '<h1>Добро пожаловать!</h1>';
      //   window.location.href = "/save_user_data/";
        window.location.href = "/game/tap";
    }
  }

  assets.forEach((asset) => {
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


const progressBar = document.createElement("div");
progressBar.style.width = "0%";
progressBar.style.height = "5px";
progressBar.style.backgroundColor = "#000";
progressBar.style.position = "fixed";
progressBar.style.top = "0";
progressBar.style.left = "0";
progressBar.style.zIndex = "1000";
document.body.appendChild(progressBar);

function updateProgress() {
  const progress = Math.round((loadedAssets / assets.length) * 100);
  progressBar.style.width = `${progress}%`;
}

function checkIfAllLoaded() {
  loadedAssets++;
  updateProgress();
  if (loadedAssets === assets.length) {
    setTimeout(() => {
      document.body.innerHTML = '<h1>Добро пожаловать!</h1>';
    }, 300);
  }
}
