import React, { useState, useRef, useEffect } from "react";

function ImageUpload1() {
    const [file, setFile] = useState(null);
    const [resizeWidth, setResizeWidth] = useState(200);
    const [resizeHeight, setResizeHeight] = useState(200);
    const [imageLoaded, setImageLoaded] = useState(false);
    const canvasRef = useRef(null);
    const imgRef = useRef(null);

    useEffect(() => {
        const canvas = canvasRef.current;
        if (canvas) {
            const ctx = canvas.getContext("2d");
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            if (file) {
                const img = new Image();
                img.onload = () => {
                    setImageLoaded(true);

                    const canvasAspectRatio = canvas.width / canvas.height;
                    const imageAspectRatio = img.width / img.height;

                    let drawWidth, drawHeight, offsetX, offsetY;

                    if (imageAspectRatio > canvasAspectRatio) {
                        drawWidth = canvas.width;
                        drawHeight = drawWidth / imageAspectRatio;
                    } else {
                        drawHeight = canvas.height;
                        drawWidth = drawHeight * imageAspectRatio;
                    }

                    offsetX = (canvas.width - drawWidth) / 2;
                    offsetY = (canvas.height - drawHeight) / 2;

                    ctx.drawImage(img, 0, 0, img.width, img.height, offsetX, offsetY, drawWidth, drawHeight);
                    imgRef.current = img;
                };

                img.src = file;
            }
        }
    }, [file]);

    function handleChange(e) {
        setFile(URL.createObjectURL(e.target.files[0]));
    }

    function resizeImage() {
        if (!imageLoaded) return;

        const canvas = canvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext("2d");
        const img = imgRef.current;

        const aspectRatio = img.width / img.height;

        let newWidth = resizeWidth;
        let newHeight = resizeHeight;

        if (!newWidth && !newHeight) {
            newWidth = img.width;
            newHeight = img.height;
        } else if (!newWidth) {
            newWidth = resizeHeight * aspectRatio;
        } else if (!newHeight) {
            newHeight = resizeWidth / aspectRatio;
        }

        canvas.width = newWidth;
        canvas.height = newHeight;

        ctx.drawImage(img, 0, 0, img.width, img.height, 0, 0, newWidth, newHeight);
    }

    return (
        <div className="ImageUpload">
            {
                file ? (
                    <div className="d-flex justify-content-center m-5">
                        <canvas
                            ref={canvasRef}
                            style={{ border: "1px solid black" }}
                        />
                    </div>
                ) : (
                    <div>
                        <div className="m-2">
                            <strong>Please upload your file</strong>
                        </div>
                        <input type="file" className="form-control" onChange={handleChange} />
                    </div>
                )
            }
            {
                imageLoaded && (
                    <div>
                        <div className="mb-2">
                            <label htmlFor="resizeWidth">Resize Width:</label>
                            <input
                                type="number"
                                id="resizeWidth"
                                className="form-control"
                                value={resizeWidth}
                                onChange={(e) => setResizeWidth(parseInt(e.target.value))}
                            />
                        </div>
                        <div className="mb-2">
                            <label htmlFor="resizeHeight">Resize Height:</label>
                            <input
                                type="number"
                                id="resizeHeight"
                                className="form-control"
                                value={resizeHeight}
                                onChange={(e) => setResizeHeight(parseInt(e.target.value))}
                            />
                        </div>
                        <button onClick={resizeImage} className="btn btn-primary mt-3">
                            Resize Image
                        </button>
                    </div>
                )
            }
        </div>
    );
}

export default ImageUpload1;
