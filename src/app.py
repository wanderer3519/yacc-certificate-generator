# # # import sys
# # # import os
# # # import pandas as pd

# # # from flask import Flask, render_template, request, redirect  
# # # from main import main as processfn
# # # from read_csv.Names import Names

# # # data_path = '../Assets/Data-for-Certificate.xlsx'
# # # image = '../Assets/Certificate.jpeg'
# # # app = Flask(__name__, template_folder="frontend")

# # # i = 0
# # # startX = startY = 0
# # # endX = endY = 0

# # # @app.route("/")
# # # def home():
# # #     return render_template('rectangle.html')

# # # @app.route("/storefile", methods=['POST'])
# # # def storefile():
# # #     global i
    
# # #     file = request.files['imageLoader']
# # #     image_filename = f"image{i}.jpeg"
# # #     image_dir = "uploads"  
# # #     os.makedirs(image_dir, exist_ok=True)  
    
# # #     image_path = os.path.join(image_dir, image_filename)  
# # #     i += 1
# # #     file.save(image_path)

# # #     with open("frontend_data.txt", "a") as fh:
# # #         fh.write(f"imagePath: {image_path}\n")

# # #     return redirect('/')


# # # @app.route("/storeinfile", methods=['POST'])
# # # def storeinfile():
# # #     data = request.get_json()
# # #     startX = int(data['startX'])
# # #     startY = int(data['startY'])
# # #     endX = int(data['endX'])
# # #     endY = int(data['endY'])

# # #     with open("frontend_data.txt", "a") as fh:
# # #         fh.write(f"startX: {startX}, startY: {startY}, endX: {endX}, endY: {endY}\n")
    

# # #     return redirect('/')
    


# # # @app.route("/processimage")
# # # def processImage():
# # #     """
# # #         Calls the main in openCV
# # #     """
    
# # #     df = pd.read_csv('../Assets/Data.csv')
# # #     NAMES = df['Name']

# # #     is_sign_added = True
# # #     image_path = "uploads/image0.jpeg"  

# # #     finimg = processfn(image_path, is_sign_added, NAMES, (startX, startY), (endX, endY), ())
    
# # #     # file = request.files['imageLoader']
# # #     image_filename = f'image{i}.jpeg'
# # #     image_dir = "uploads"  
# # #     os.makedirs(image_dir, exist_ok=True)  
    
# # #     image_path = os.path.join(image_dir, image_filename)  
# # #     finimg.save(image_path)

# # #     i += 1

# # #     return redirect('/storefile')
 
# # # import os
# # # import uuid
# # # import pandas as pd
# # # import cv2

# # # from flask import Flask, render_template, request, redirect, jsonify, session
# # # from main import main as processfn




# # # # Flask setup
# # # app = Flask(__name__, template_folder="frontend")
# # # app.secret_key = "your_secret_key"  # Required for Flask sessions

# # # # File paths
# # # DATA_PATH = '../Assets/Data-for-Certificate.xlsx'
# # # IMAGE_TEMPLATE_PATH = '../Assets/Certificate.jpeg'
# # # UPLOAD_DIR = "uploads"
# # # os.makedirs(UPLOAD_DIR, exist_ok=True)

# # # import zipfile

# # # zip_filename = "processed_certificates.zip"
# # # zip_path = os.path.join(UPLOAD_DIR, zip_filename)

# # # with zipfile.ZipFile(zip_path, "w") as zipf:
# # #     for name in NAMES:
# # #         cert_path = os.path.join(UPLOAD_DIR, f"{name}_certificate.jpeg")
# # #         zipf.write(cert_path, os.path.basename(cert_path))


# # # @app.route("/")
# # # def home():
# # #     return render_template('rectangle.html')

# # # @app.route("/storefile", methods=['POST'])
# # # def storefile():
# # #     # Save the uploaded image with a unique filename
# # #     file = request.files['imageLoader']
# # #     image_filename = f"{uuid.uuid4().hex}.jpeg"
# # #     image_path = os.path.join(UPLOAD_DIR, image_filename)
# # #     file.save(image_path)

# # #     # Store image path in the session for later use
# # #     session['uploaded_image'] = image_path

# # #     # Log the file path
# # #     with open("frontend_data.txt", "a") as fh:
# # #         fh.write(f"imagePath: {image_path}\n")

# # #     return redirect('/')

# # # @app.route("/storeinfile", methods=['POST'])
# # # def storeinfile():
# # #     # Save rectangle coordinates from the frontend
# # #     data = request.get_json()
# # #     session['startX'] = int(data['startX'])
# # #     session['startY'] = int(data['startY'])
# # #     session['endX'] = int(data['endX'])
# # #     session['endY'] = int(data['endY'])

# # #     # Log the rectangle coordinates
# # #     with open("frontend_data.txt", "a") as fh:
# # #         fh.write(f"startX: {session['startX']}, startY: {session['startY']}, "
# # #                  f"endX: {session['endX']}, endY: {session['endY']}\n")

# # #     return jsonify({"message": "Coordinates stored successfully!"}), 200

# # # @app.route("/processimage", methods=['GET'])
# # # def process_image():
# # #     """
# # #     Calls the `processfn` function to process the uploaded image.
# # #     """
# # #     # Ensure required data is available
# # #     image_path = session.get('uploaded_image')
# # #     if not image_path:
# # #         return jsonify({"error": "No image uploaded."}), 400

# # #     coordinates = (
# # #         session.get('startX'),
# # #         session.get('startY'),
# # #         session.get('endX'),
# # #         session.get('endY'),
# # #     )
# # #     if None in coordinates:
# # #         return jsonify({"error": "Rectangle coordinates not set."}), 400

# # #     # Read names from the data file
# # #     df = pd.read_csv('../Assets/Data.csv')
# # #     NAMES = df['Name']

# # #     # Process the image
# # #     is_sign_added = True
# # #     processed_image = processfn(image_path, is_sign_added, NAMES, 
# # #                                 (coordinates[0], coordinates[1]), 
# # #                                 (coordinates[2], coordinates[3]), ())

# # #     # Save the processed image
# # #     processed_filename = f"processed_{uuid.uuid4().hex}.jpeg"
# # #     processed_path = os.path.join(UPLOAD_DIR, processed_filename)
# # #     processed_image.save(processed_path)

# # #     return jsonify({"message": "Image processed successfully!", 
# # #                     "processed_image": processed_path}), 200

# # # @app.route("/processimage", methods=['GET'])
# # # def process_image():
# # #     # Ensure required data is available
# # #     image_path = session.get('uploaded_image')
# # #     if not image_path:
# # #         return jsonify({"error": "No image uploaded."}), 400

# # #     coordinates = (
# # #         session.get('startX'),
# # #         session.get('startY'),
# # #         session.get('endX'),
# # #         session.get('endY'),
# # #     )
# # #     if None in coordinates:
# # #         return jsonify({"error": "Rectangle coordinates not set."}), 400

# # #     # Read names from the data file
# # #     df = pd.read_csv('../Assets/Data.csv')
# # #     NAMES = df['Name']

# # #     # Load signature images (example paths; update as needed)
# # #     signature_image1 = cv2.imread('../Assets/img.png', cv2.IMREAD_UNCHANGED)
# # #     signature_image2 = cv2.imread('../Assets/img1.png', cv2.IMREAD_UNCHANGED)

# # #     if signature_image1 is None or signature_image2 is None:
# # #         return jsonify({"error": "Signature images not found."}), 500

# # #     # Process the image
# # #     processed_image = processfn(
# # #         image_path=image_path,
# # #         is_sign_added=True,
# # #         names=NAMES,
# # #         start=(coordinates[0], coordinates[1]),
# # #         end=(coordinates[2], coordinates[3]),
# # #         signs=(signature_image1, signature_image2)
# # #     )

# # #     if processed_image is None:
# # #         return jsonify({"error": "Image processing failed."}), 500

# # #     # Save the processed image
# # #     processed_filename = f"processed_{uuid.uuid4().hex}.jpeg"
# # #     processed_path = os.path.join(UPLOAD_DIR, processed_filename)
# # #     cv2.imwrite(processed_path, processed_image)

# # #     return jsonify({"message": "Image processed successfully!", 
# # #                     "processed_image": processed_path}), 200



# # # if __name__ == "__main__":
# # #     app.run(debug=True)

# # # from flask import Flask, request, jsonify, send_file, render_template
# # # from werkzeug.utils import secure_filename
# # # import os
# # # from PIL import Image, ImageDraw
# # # import io

# # # app = Flask(__name__)

# # # # Configuration
# # # UPLOAD_FOLDER = 'uploads'
# # # PROCESSED_FOLDER = 'processed'
# # # ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
# # # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# # # app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# # # # Ensure folders exist
# # # os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# # # os.makedirs(PROCESSED_FOLDER, exist_ok=True)

# # # # Globals to store rectangle coordinates and filename
# # # rectangle_coords = {}
# # # uploaded_file_path = None

# # # # Utility function to check allowed file types
# # # def allowed_file(filename):
# # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # @app.route('/')
# # # def index():
# # #     return render_template('index.html')

# # # @app.route('/storefile', methods=['POST'])
# # # def store_file():
# # #     global uploaded_file_path

# # #     if 'imageLoader' not in request.files:
# # #         return "No file part", 400

# # #     file = request.files['imageLoader']

# # #     if file.filename == '':
# # #         return "No selected file", 400

# # #     if file and allowed_file(file.filename):
# # #         filename = secure_filename(file.filename)
# # #         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
# # #         file.save(file_path)
# # #         uploaded_file_path = file_path
# # #         return "File uploaded successfully!"

# # #     return "Invalid file type", 400

# # # @app.route('/storeinfile', methods=['POST'])
# # # def store_in_file():
# # #     global rectangle_coords

# # #     data = request.get_json()
# # #     if not data:
# # #         return jsonify({"error": "No data provided"}), 400

# # #     try:
# # #         rectangle_coords = {
# # #             'startX': int(data['startX']),
# # #             'startY': int(data['startY']),
# # #             'endX': int(data['endX']),
# # #             'endY': int(data['endY'])
# # #         }
# # #         return jsonify({"message": "Coordinates saved successfully!"})

# # #     except (KeyError, ValueError):
# # #         return jsonify({"error": "Invalid data format"}), 400

# # # @app.route('/processimage', methods=['GET'])
# # # def process_image():
# # #     global uploaded_file_path, rectangle_coords

# # #     if not uploaded_file_path or not rectangle_coords:
# # #         return jsonify({"error": "File or coordinates not provided"}), 400

# # #     try:
# # #         # Open the uploaded image
# # #         with Image.open(uploaded_file_path) as img:
# # #             draw = ImageDraw.Draw(img)
# # #             rect = [
# # #                 rectangle_coords['startX'],
# # #                 rectangle_coords['startY'],
# # #                 rectangle_coords['endX'],
# # #                 rectangle_coords['endY']
# # #             ]
# # #             # Draw a rectangle on the image
# # #             draw.rectangle(rect, outline="teal", width=3)

# # #             # Save the processed image
# # #             processed_file_path = os.path.join(
# # #                 app.config['PROCESSED_FOLDER'], 'processed_' + os.path.basename(uploaded_file_path)
# # #             )
# # #             img.save(processed_file_path)

# # #         return jsonify({"message": "Certificates processed successfully!", "processed_image": processed_file_path})

# # #     except Exception as e:
# # #         return jsonify({"error": str(e)}), 500

# # # @app.route('/download', methods=['GET'])
# # # def download():
# # #     global uploaded_file_path

# # #     if not uploaded_file_path:
# # #         return "No file available for download", 400

# # #     try:
# # #         filename = os.path.basename(uploaded_file_path)
# # #         return send_file(uploaded_file_path, as_attachment=True, download_name=filename)

# # #     except Exception as e:
# # #         return str(e), 500

# # # if __name__ == '__main__':
# # #     app.run(debug=True)

# # from flask import Flask, request, jsonify, send_file, render_template, session, redirect
# # from werkzeug.utils import secure_filename
# # import os
# # from PIL import Image, ImageDraw
# # import pandas as pd
# # import zipfile
# # import uuid

# # app = Flask(__name__)
# # app.secret_key = "your_secret_key"

# # # Configuration
# # UPLOAD_FOLDER = 'uploads'
# # PROCESSED_FOLDER = 'processed'
# # ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
# # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# # app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# # # Ensure folders exist
# # os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# # os.makedirs(PROCESSED_FOLDER, exist_ok=True)

# # # Globals to store rectangle coordinates and filename
# # rectangle_coords = {}
# # uploaded_file_path = None

# # # Utility function to check allowed file types
# # def allowed_file(filename):
# #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/storefile', methods=['POST'])
# # def store_file():
# #     global uploaded_file_path

# #     if 'imageLoader' not in request.files:
# #         return "No file part", 400

# #     file = request.files['imageLoader']

# #     if file.filename == '':
# #         return "No selected file", 400

# #     if file and allowed_file(file.filename):
# #         filename = secure_filename(file.filename)
# #         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
# #         file.save(file_path)
# #         uploaded_file_path = file_path
# #         return "File uploaded successfully!"

# #     return "Invalid file type", 400

# # @app.route('/storeinfile', methods=['POST'])
# # def store_in_file():
# #     global rectangle_coords

# #     data = request.get_json()
# #     if not data:
# #         return jsonify({"error": "No data provided"}), 400

# #     try:
# #         rectangle_coords = {
# #             'startX': int(data['startX']),
# #             'startY': int(data['startY']),
# #             'endX': int(data['endX']),
# #             'endY': int(data['endY'])
# #         }
# #         return jsonify({"message": "Coordinates saved successfully!"})

# #     except (KeyError, ValueError):
# #         return jsonify({"error": "Invalid data format"}), 400

# # @app.route('/processcertificates', methods=['GET'])
# # def process_certificates():
# #     """
# #     Generate certificates for all names in the data file, save them, and zip them.
# #     """
# #     global uploaded_file_path, rectangle_coords

# #     if not uploaded_file_path or not rectangle_coords:
# #         return jsonify({"error": "File or coordinates not provided"}), 400

# #     # Load names from the CSV file
# #     data_path = '../Assets/Data.csv'  # Path to the CSV file with names
# #     try:
# #         df = pd.read_csv(data_path)
# #         names = df['Name']
# #     except Exception as e:
# #         return jsonify({"error": f"Failed to load names from CSV: {str(e)}"}), 500

# #     processed_files = []

# #     try:
# #         # Process the image for each name
# #         for name in names:
# #             with Image.open(uploaded_file_path) as img:
# #                 draw = ImageDraw.Draw(img)

# #                 # Draw the rectangle on the image
# #                 rect = [
# #                     rectangle_coords['startX'],
# #                     rectangle_coords['startY'],
# #                     rectangle_coords['endX'],
# #                     rectangle_coords['endY']
# #                 ]
# #                 draw.rectangle(rect, outline="teal", width=3)

# #                 # Add the name to the certificate
# #                 font_size = 400  # Adjust as needed
# #                 text_x = (rectangle_coords['startX'] + rectangle_coords['endX']) // 2
# #                 text_y = rectangle_coords['startY'] + 10
# #                 draw.text((text_x, text_y), name, fill="black")

# #                 # Save the processed image
# #                 processed_file_name = f"{name}_certificate.jpeg"
# #                 processed_file_path = os.path.join(app.config['PROCESSED_FOLDER'], processed_file_name)
# #                 img.save(processed_file_path)
# #                 processed_files.append(processed_file_path)

# #         # Create a ZIP file containing all processed certificates
# #         zip_filename = 'processed_certificates.zip'
# #         zip_path = os.path.join(app.config['UPLOAD_FOLDER'], zip_filename)
# #         with zipfile.ZipFile(zip_path, 'w') as zipf:
# #             for file_path in processed_files:
# #                 zipf.write(file_path, os.path.basename(file_path))

# #         return jsonify({"message": "Certificates processed successfully!", "zip_path": zip_path})

# #     except Exception as e:
# #         return jsonify({"error": str(e)}), 500

# # @app.route('/downloadcertificates', methods=['GET'])
# # def download_certificates():
# #     """
# #     Allow the user to download the ZIP file of processed certificates.
# #     """
# #     zip_path = os.path.join(app.config['UPLOAD_FOLDER'], 'processed_certificates.zip')

# #     if not os.path.exists(zip_path):
# #         return jsonify({"error": "ZIP file not found. Please process certificates first."}), 400

# #     try:
# #         return send_file(zip_path, as_attachment=True, download_name='processed_certificates.zip')

# #     except Exception as e:
# #         return jsonify({"error": str(e)}), 500

# # if __name__ == '__main__':
# #     app.run(debug=True)

# from flask import Flask, render_template, request, send_from_directory
# import cv2
# import os
# from werkzeug.utils import secure_filename

# app = Flask(__name__)

# # Set up the uploads and static folder
# UPLOAD_FOLDER = 'uploads'
# STATIC_FOLDER = 'static'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['STATIC_FOLDER'] = STATIC_FOLDER
# app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# # Function to check allowed file extensions
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# # The function that adds name to the image
# def add_names(image, names, rect_startX, rect_startY, rect_endX, rect_endY):
#     # Draw a rectangle on the image
#     cv2.rectangle(image, (rect_startX, rect_startY), (rect_endX, rect_endY), (0, 255, 0), 2)
    
#     # Set font properties
#     font_scale = 1
#     thickness = 1
#     font = cv2.FONT_HERSHEY_COMPLEX_SMALL

#     # Initial vertical offset for names
#     y_offset = rect_startY + 20  # 20px below the rectangle start

#     # Loop through the names and add each one to the image
#     for name in names:
#         # Get the text size
#         (text_width, text_height), baseline = cv2.getTextSize(name, font, font_scale, thickness)
        
#         # Calculate position to center the text horizontally within the rectangle
#         x_offset = (rect_startX + rect_endX) // 2 - (text_width // 2)
        
#         # Put the text on the image
#         image = cv2.putText(image, name, (x_offset, y_offset), font, font_scale, (0, 0, 255), thickness, cv2.LINE_AA)
        
#         # Move the y-offset down for the next name
#         y_offset += text_height + baseline + 10  # Add space between names

#     return image

# # Home route to upload file
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Route to handle the image upload and name addition
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return "No file part", 400

#     file = request.files['file']
#     names_input = request.form['names']  # Accepting a comma-separated list of names

#     if file.filename == '' or not allowed_file(file.filename):
#         return "No selected file or invalid file type", 400

#     # Save the uploaded file
#     filename = secure_filename(file.filename)
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     file.save(file_path)

#     # Read the image using OpenCV
#     image = cv2.imread(file_path)

#     # Set coordinates for the rectangle (example values)
#     rect_startX, rect_startY, rect_endX, rect_endY = 100, 100, 500, 300

#     # Convert the comma-separated names input into a list
#     names = [name.strip() for name in names_input.split(',')]

#     # Add the names to the image
#     image_with_names = add_names(image, names, rect_startX, rect_startY, rect_endX, rect_endY)

#     # Save the new image
#     output_path = os.path.join(app.config['STATIC_FOLDER'], 'output_' + filename)
#     cv2.imwrite(output_path, image_with_names)

#     # Send the new image back to the user
#     return send_from_directory(app.config['STATIC_FOLDER'], 'output_' + filename)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, send_from_directory
import cv2
import os
from werkzeug.utils import secure_filename
import numpy as np

app = Flask(__name__)

# Set up the uploads and static folder
UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['STATIC_FOLDER'] = STATIC_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Store start and end coordinates of the rectangle
start_point = None
end_point = None
is_drawing = False

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Mouse callback function to capture rectangle coordinates
def capture_rectangle(event, x, y, flags, param):
    global start_point, end_point, is_drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        # Record the starting point of the rectangle
        if not is_drawing:
            start_point = (x, y)
            is_drawing = True
        else:
            end_point = (x, y)
            is_drawing = False

# The function that adds name to the image
def add_names(image, names):
    # Draw the rectangle on the image using the coordinates
    if start_point and end_point:
        cv2.rectangle(image, start_point, end_point, (0, 255, 0), 2)

    # Set font properties
    font_scale = 1
    thickness = 1
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL

    # Initial vertical offset for names
    y_offset = start_point[1] + 20 if start_point else 100  # 20px below the rectangle start

    # Loop through the names and add each one to the image
    for name in names:
        # Get the text size
        (text_width, text_height), baseline = cv2.getTextSize(name, font, font_scale, thickness)
        
        # Calculate position to center the text horizontally within the rectangle
        x_offset = (start_point[0] + end_point[0]) // 2 - (text_width // 2) if start_point and end_point else 100
        
        # Put the text on the image
        image = cv2.putText(image, name, (x_offset, y_offset), font, font_scale, (0, 0, 255), thickness, cv2.LINE_AA)
        
        # Move the y-offset down for the next name
        y_offset += text_height + baseline + 10  # Add space between names

    return image

# Home route to upload file
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the image upload and name addition
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    names_input = request.form['names']  # Accepting a comma-separated list of names

    if file.filename == '' or not allowed_file(file.filename):
        return "No selected file or invalid file type", 400

    # Save the uploaded file
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Read the image using OpenCV
    image = cv2.imread(file_path)

    # Convert the comma-separated names input into a list
    names = [name.strip() for name in names_input.split(',')]

    # Display the image and capture the rectangle selection
    global start_point, end_point, is_drawing
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", capture_rectangle)

    while True:
        # Show the image with the rectangle
        temp_image = image.copy()
        if start_point and end_point:
            temp_image = add_names(temp_image, names)
        cv2.imshow("Image", temp_image)

        # Break the loop when two clicks are made
        if start_point and end_point:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After capturing the rectangle coordinates, add names
    image_with_names = add_names(image, names)

    # Save the new image
    output_path = os.path.join(app.config['STATIC_FOLDER'], 'output_' + filename)
    cv2.imwrite(output_path, image_with_names)

    # Close the image window
    cv2.destroyAllWindows()

    # Send the new image back to the user
    return send_from_directory(app.config['STATIC_FOLDER'], 'output_' + filename)

if __name__ == '__main__':
    app.run(debug=True)
