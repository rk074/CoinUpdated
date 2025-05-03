function updateTime() {
    const noCacheUrl = '/coinprice?ts=' + new Date().getTime();  // cache buster

    fetch(noCacheUrl)
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById('coin_data');
            html_data = "";
            for(coin of data){
                html_data += `<li>${coin[0]}: ${coin[1]}</li>`
            }

            list.innerHTML = html_data;
        });
}

updateTime();
setInterval(updateTime, 500);