# import sys
# import os
# import pandas as pd

# from flask import Flask, render_template, request, redirect  
# from main import main as processfn
# from read_csv.Names import Names

# data_path = '../Assets/Data-for-Certificate.xlsx'
# image = '../Assets/Certificate.jpeg'
# app = Flask(__name__, template_folder="frontend")

# i = 0
# startX = startY = 0
# endX = endY = 0

# @app.route("/")
# def home():
#     return render_template('rectangle.html')

# @app.route("/storefile", methods=['POST'])
# def storefile():
#     global i
    
#     file = request.files['imageLoader']
#     image_filename = f"image{i}.jpeg"
#     image_dir = "uploads"  
#     os.makedirs(image_dir, exist_ok=True)  
    
#     image_path = os.path.join(image_dir, image_filename)  
#     i += 1
#     file.save(image_path)

#     with open("frontend_data.txt", "a") as fh:
#         fh.write(f"imagePath: {image_path}\n")

#     return redirect('/')


# @app.route("/storeinfile", methods=['POST'])
# def storeinfile():
#     data = request.get_json()
#     startX = int(data['startX'])
#     startY = int(data['startY'])
#     endX = int(data['endX'])
#     endY = int(data['endY'])

#     with open("frontend_data.txt", "a") as fh:
#         fh.write(f"startX: {startX}, startY: {startY}, endX: {endX}, endY: {endY}\n")
    

#     return redirect('/')
    


# @app.route("/processimage")
# def processImage():
#     """
#         Calls the main in openCV
#     """
    
#     df = pd.read_csv('../Assets/Data.csv')
#     NAMES = df['Name']

#     is_sign_added = True
#     image_path = "uploads/image0.jpeg"  

#     finimg = processfn(image_path, is_sign_added, NAMES, (startX, startY), (endX, endY), ())
    
#     # file = request.files['imageLoader']
#     image_filename = f'image{i}.jpeg'
#     image_dir = "uploads"  
#     os.makedirs(image_dir, exist_ok=True)  
    
#     image_path = os.path.join(image_dir, image_filename)  
#     finimg.save(image_path)

#     i += 1

#     return redirect('/storefile')
 
import os
import uuid
import pandas as pd
import cv2

from flask import Flask, render_template, request, redirect, jsonify, session
from main import main as processfn

# Flask setup
app = Flask(__name__, template_folder="frontend")
app.secret_key = "your_secret_key"  # Required for Flask sessions

# File paths
DATA_PATH = '../Assets/Data-for-Certificate.xlsx'
IMAGE_TEMPLATE_PATH = '../Assets/Certificate.jpeg'
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route("/")
def home():
    return render_template('rectangle.html')

@app.route("/storefile", methods=['POST'])
def storefile():
    # Save the uploaded image with a unique filename
    file = request.files['imageLoader']
    image_filename = f"{uuid.uuid4().hex}.jpeg"
    image_path = os.path.join(UPLOAD_DIR, image_filename)
    file.save(image_path)

    # Store image path in the session for later use
    session['uploaded_image'] = image_path

    # Log the file path
    with open("frontend_data.txt", "a") as fh:
        fh.write(f"imagePath: {image_path}\n")

    return redirect('/')

@app.route("/storeinfile", methods=['POST'])
def storeinfile():
    # Save rectangle coordinates from the frontend
    data = request.get_json()
    session['startX'] = int(data['startX'])
    session['startY'] = int(data['startY'])
    session['endX'] = int(data['endX'])
    session['endY'] = int(data['endY'])

    # Log the rectangle coordinates
    with open("frontend_data.txt", "a") as fh:
        fh.write(f"startX: {session['startX']}, startY: {session['startY']}, "
                 f"endX: {session['endX']}, endY: {session['endY']}\n")

    return jsonify({"message": "Coordinates stored successfully!"}), 200

# @app.route("/processimage", methods=['GET'])
# def process_image():
#     """
#     Calls the `processfn` function to process the uploaded image.
#     """
#     # Ensure required data is available
#     image_path = session.get('uploaded_image')
#     if not image_path:
#         return jsonify({"error": "No image uploaded."}), 400

#     coordinates = (
#         session.get('startX'),
#         session.get('startY'),
#         session.get('endX'),
#         session.get('endY'),
#     )
#     if None in coordinates:
#         return jsonify({"error": "Rectangle coordinates not set."}), 400

#     # Read names from the data file
#     df = pd.read_csv('../Assets/Data.csv')
#     NAMES = df['Name']

#     # Process the image
#     is_sign_added = True
#     processed_image = processfn(image_path, is_sign_added, NAMES, 
#                                 (coordinates[0], coordinates[1]), 
#                                 (coordinates[2], coordinates[3]), ())

#     # Save the processed image
#     processed_filename = f"processed_{uuid.uuid4().hex}.jpeg"
#     processed_path = os.path.join(UPLOAD_DIR, processed_filename)
#     processed_image.save(processed_path)

#     return jsonify({"message": "Image processed successfully!", 
#                     "processed_image": processed_path}), 200

@app.route("/processimage", methods=['GET'])
def process_image():
    # Ensure required data is available
    image_path = session.get('uploaded_image')
    if not image_path:
        return jsonify({"error": "No image uploaded."}), 400

    coordinates = (
        session.get('startX'),
        session.get('startY'),
        session.get('endX'),
        session.get('endY'),
    )
    if None in coordinates:
        return jsonify({"error": "Rectangle coordinates not set."}), 400

    # Read names from the data file
    df = pd.read_csv('../Assets/Data.csv')
    NAMES = df['Name']

    # Load signature images (example paths; update as needed)
    signature_image1 = cv2.imread('../Assets/img.png', cv2.IMREAD_UNCHANGED)
    signature_image2 = cv2.imread('../Assets/img1.png', cv2.IMREAD_UNCHANGED)

    if signature_image1 is None or signature_image2 is None:
        return jsonify({"error": "Signature images not found."}), 500

    # Process the image
    processed_image = processfn(
        image_path=image_path,
        is_sign_added=True,
        names=NAMES,
        start=(coordinates[0], coordinates[1]),
        end=(coordinates[2], coordinates[3]),
        signs=(signature_image1, signature_image2)
    )

    if processed_image is None:
        return jsonify({"error": "Image processing failed."}), 500

    # Save the processed image
    processed_filename = f"processed_{uuid.uuid4().hex}.jpeg"
    processed_path = os.path.join(UPLOAD_DIR, processed_filename)
    cv2.imwrite(processed_path, processed_image)

    return jsonify({"message": "Image processed successfully!", 
                    "processed_image": processed_path}), 200



if __name__ == "__main__":
    app.run(debug=True)
