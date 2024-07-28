const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
const imageLoader = document.getElementById('imageLoader');

let clickCount = 0;
let startX, startY, endX, endY;
let image = new Image();

imageLoader.addEventListener('change', handleImage, false);
canvas.addEventListener('click', handleCanvasClick, false);


export default function handleCanvasClick(e) {
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

        clickCount = 0; 
    }
}
