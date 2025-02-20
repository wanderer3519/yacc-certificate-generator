import React, { useState } from "react";
import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:5000"; // Change if using a different backend URL

const CertificateGenerator = () => {
  const [file, setFile] = useState(null);
  const [coordinates, setCoordinates] = useState([]);

  const [filename, setFilename] = useState("");
  
  const handleFileChange = (e) => setFile(e.target.files[0]);
  
  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);
    
    const res = await axios.post(`${API_BASE_URL}/upload`, formData);
    setFilename(res.data.filename);
  };
  
  const handleImageClick = (e) => {
    if (coordinates.length < 2) {
      setCoordinates([...coordinates, { x: e.nativeEvent.offsetX, y: e.nativeEvent.offsetY }]);
    }
    console.log(coordinates);
  };
  
  const handleGenerate = async () => {
    console.log("SHIT", filename);
    if (coordinates.length < 2 || !filename) return;
    
    await axios.post(`${API_BASE_URL}/generate`, {
      filename,

      startX: coordinates[0].x,
      startY: coordinates[0].y,
      endX: coordinates[1].x,
      endY: coordinates[1].y,
    });
  };

  // const handleDownloadAll = async () => {
  //   console.log(filename);
  //   window.location.href = `${API_BASE_URL}/download-all`;
  // };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      <br />
      
      <br />
      {file && (
        <img
          src={URL.createObjectURL(file)}
          alt="Certificate"
          onClick={handleImageClick}
          style={{ cursor: "crosshair", maxWidth: "500px" }}
        />
      )}
      <br />
      <button onClick={handleGenerate} disabled={coordinates.length < 2}>
        Generate Certificates
      </button>
      {/* <button onClick={handleDownloadAll}>Download All Certificates</button> */}
    </div>
  );
};

export default CertificateGenerator;
