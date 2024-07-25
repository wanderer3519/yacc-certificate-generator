const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
const imageLoader = document.getElementById('imageLoader');

let clickCount = 0;
let nameStartX, nameStartY, nameEndX, nameEndY;
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
    if ((clickCount & 1) == 0) {
        nameStartX = e.offsetX;
        nameStartY = e.offsetY;
        clickCount++;
    } else {
        nameEndX = e.offsetX;
        nameEndY = e.offsetY;

        const width = nameEndX - nameStartX;
        const height = nameEndY - nameStartY;

        ctx.drawImage(image, 0, 0); 
        ctx.beginPath();
        ctx.rect(nameStartX, nameStartY, width, height);
        ctx.strokeStyle = 'teal';
        ctx.lineWidth = 2;
        ctx.stroke();

        clickCount++; 
    }

    console.log(nameStartX, nameStartY, nameEndX, nameEndY, clickCount);
}
