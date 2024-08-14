function plantCrop() {
    fetch('/plant', {
        method: 'POST'
    }).then(response => response.json())
    .then(data => {
        document.getElementById("status").innerText = data.message;
    });
}

function waterCrop() {
    fetch('/water', {
        method: 'POST'
    }).then(response => response.json())
    .then(data => {
        document.getElementById("status").innerText = data.message;
    });
}

function harvestCrop() {
    fetch('/harvest', {
        method: 'POST'
    }).then(response => response.json())
    .then(data => {
        document.getElementById("status").innerText = data.message;
    });
}
