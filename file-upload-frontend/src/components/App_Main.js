import React, { useState, useRef } from 'react';
import './App.css';

function App() {
  const [image, setImage] = useState(null);
  const [clickCount, setClickCount] = useState(0);
  
  const [startX, setStartX] = useState(0);
  const [startY, setStartY] = useState(0);
  
  const canvasRef = useRef(null);
  const ctxRef = useRef(null);
  const imageRef = useRef(new Image());

  const handleImageUpload = (e) => {
    const reader = new FileReader();
    reader.onload = (event) => {
      const img = new Image();
      img.onload = () => {
        const canvas = canvasRef.current;
        const ctx = canvas.getContext('2d');
        canvas.width = img.width;
        canvas.height = img.height;
        ctx.drawImage(img, 0, 0);
        ctxRef.current = ctx;
        imageRef.current = img;
      };
      img.src = event.target.result;
      setImage(event.target.result);
    };
    reader.readAsDataURL(e.target.files[0]);
  };

  const handleCanvasClick = (e) => {
    const canvas = canvasRef.current;
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    console.log(x, y);

    if (clickCount === 0) {
      setStartX(x);
      setStartY(y);
      setClickCount(1);
    } else {
      const ctx = ctxRef.current;
      const width = x - startX;
      const height = y - startY;

      ctx.drawImage(imageRef.current, 0, 0);
      ctx.beginPath();
      ctx.rect(startX, startY, width, height);
      ctx.strokeStyle = 'red';
      ctx.lineWidth = 2;
      ctx.stroke();

      setClickCount(0);
    }
  };

  return (
    <div className="m-2 align-items-center">
    
      <input type="file" accept="image/*" onChange={handleImageUpload} />
    
      <div className='m-2'>
        <canvas ref={canvasRef} onClick={handleCanvasClick} />
      </div>
    </div>
  );
}

export default App;
