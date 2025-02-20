from flask import Flask, request, send_file, jsonify
from flask_cors import CORS  # Import CORS
import cv2
import numpy as np
import os
import zipfile
from werkzeug.utils import secure_filename
from openCV_text_addition.certificate_openCv import add_name

names = ["Krishna", "Nandan", "Mounica", "Rishi"]

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_certificate():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    return jsonify({"message": "File uploaded successfully", "filename": filename})

@app.route("/generate", methods=["POST"])
def generate_certificates():
    data = request.json
    filename = data.get("filename")
    startX, startY = data.get("startX"), data.get("startY")
    endX, endY = data.get("endX"), data.get("endY")

    if not filename or startX is None or startY is None or endX is None or endY is None:
        return jsonify({"error": "Missing parameters"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(filepath):
        return jsonify({"error": "File not found"}), 404

    generated_files = []
    for name in names:
        img = cv2.imread(filepath)
        add_name(img, name, startX, startY, endX, endY)
        output_filename = f"{name}.jpg"
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)
        cv2.imwrite(output_path, img)
        generated_files.append(output_path)
    
    return jsonify({"message": "Certificates generated", "files": generated_files})

@app.route("/download-all", methods=["GET"])
def download_all():
    zip_filename = "certificates.zip"
    zip_path = os.path.join(OUTPUT_FOLDER, zip_filename)
    
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in os.listdir(OUTPUT_FOLDER):
            file_path = os.path.join(OUTPUT_FOLDER, file)
            zipf.write(file_path, os.path.basename(file_path))
    
    return send_file(zip_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
