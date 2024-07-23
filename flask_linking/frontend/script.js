const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
const imageLoader = document.getElementById('imageLoader');

let clickCount = 0;
let startX, startY, endX, endY;
let image = new Image();

imageLoader.addEventListener('change', handleImage, false);
canvas.addEventListener('click', handleCanvasClick, false);

function handleImage(e) {
    const reader = new FileReader();
    reader.onload = function(event) {
        image.onload = function() {
            canvas.width = image.width;
            canvas.height = image.height;
            ctx.drawImage(image, 0, 0);
        }
        image.src = event.target.result;
    }
    reader.readAsDataURL(e.target.files[0]);
}

function handleCanvasClick(e) {
    if (clickCount === 0) {
        startX = e.offsetX;
        startY = e.offsetY;
        clickCount = 1;
    } else {
        endX = e.offsetX;
        endY = e.offsetY;

        const width = endX - startX;
        const height = endY - startY;

        ctx.drawImage(image, 0, 0); 
        ctx.beginPath();
        ctx.rect(startX, startY, width, height);
        ctx.strokeStyle = 'teal';
        ctx.lineWidth = 2;
        ctx.stroke();
        sendVar(startX,startY,endX,endY);
        clickCount = 0; 
    }
}
function sendVar(startX, startY, endX, endY) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/storeinfile", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    var data = JSON.stringify({ startX: startX, startY: startY, endX: endX, endY: endY });
    xhr.send(data);
}