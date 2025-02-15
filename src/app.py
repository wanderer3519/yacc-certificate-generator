import sys
import os
import pandas as pd

from flask import Flask, render_template, request, redirect  
from main import main as processfn
# from read_csv.Names import Names

data_path = '../Assets/Data-for-Certificate.xlsx'
image = '../Assets/Certificate.jpeg'
app = Flask(__name__)

i = 0
startX = startY = 0
endX = endY = 0

@app.route("/")
def home():
    return render_template('index.html')    


@app.route("/processimage", methods=['POST'])
def processImage():
    """
        Calls the main in openCV
    """
    
    df = pd.read_csv('../Assets/Data.csv')
    NAMES = df['Name']

    is_sign_added = True
    image_path = "uploads/image0.jpeg"  

    startX = request.form['startX']
    startY = request.form['startY']
    endX = request.form['endX']
    endY = request.form['endY']

    print(f'start: {startX, startY}, end: {endX, endY}')

    finimg = processfn(image_path, is_sign_added, NAMES, (startX, startY), (endX, endY), ())
    
    # file = request.files['imageLoader']
    image_filename = f'image{i}.jpeg'
    image_dir = "uploads"  
    os.makedirs(image_dir, exist_ok=True)  
    
    image_path = os.path.join(image_dir, image_filename)  
    finimg.save(image_path)

    i += 1

    return redirect('/')
 
# import os
# import json
# import pandas as pd
# from flask import Flask, render_template, request, redirect, jsonify, send_file
# from main import main as processfn  # Your certificate generation function
# import cv2

# app = Flask(__name__)

# # Paths
# UPLOAD_FOLDER = "uploads"
# OUTPUT_FOLDER = "outputs"
# DATA_FILE = "../Assets/Data.csv"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# # Global Variables
# coordinates = {}
# certificate_template = None

# # Function to add a name to the certificate
# def add_name(image, name, startX, startY, endX, endY):
#     font_scale = 1
#     thickness = 2
#     font = cv2.FONT_HERSHEY_COMPLEX_SMALL

#     # Get the text size
#     (text_width, text_height), baseline = cv2.getTextSize(name, font, font_scale, thickness)
#     total_height = text_height + baseline

#     # Calculate the text's position to center it within the rectangle
#     name_loc_width = (startX + endX) // 2 - (text_width // 2)
#     name_loc_height = (startY + endY) // 2 + (text_height // 2)

#     # Add the name text to the image
#     cv2.putText(image, name, (name_loc_width, name_loc_height), font, font_scale, (0, 0, 255), thickness, cv2.LINE_AA)
#     print(f"Added name: {name} at position: {(name_loc_width, name_loc_height)}")
#     return image



# @app.route("/")
# def home():
#     return render_template('index.html')

# # @app.route("/storefile", methods=['POST'])
# # def storefile():
# #     """
# #     Save the uploaded certificate template image.
# #     """
# #     if 'imageLoader' not in request.files:
# #         return "No file uploaded", 400

# #     file = request.files['imageLoader']
# #     if file.filename == '':
# #         return "No selected file", 400

# #     if file:
# #         template_path = os.path.join('uploads', file.filename)
# #         file.save(template_path)
# #         print(f"Certificate template uploaded and saved at: {template_path}", flush=True)

# #         # Return response with a button to go back to the home page
# #         return """
# #                 <h1>File Uploaded Successfully</h1>
# #                 <p>Your certificate template has been uploaded.</p>
# #                 <button onclick="window.location.href='/'">Go to Home</button>
# #         """

# @app.route("/storefile", methods=['POST'])
# def storefile():
#     """
#     Save the uploaded certificate template image.
#     """
#     if 'imageLoader' not in request.files:
#         return "No file uploaded", 400

#     file = request.files['imageLoader']
#     if file.filename == '':
#         return "No selected file", 400

#     if file:
#         template_path = os.path.join('uploads', file.filename)
#         os.makedirs('uploads', exist_ok=True)  # Ensure the directory exists
#         file.save(template_path)

#         print(f"Image uploaded and saved at: {template_path}", flush=True)

#         # Redirect to coordinate selection page with the uploaded image
#         return render_template('coordinate_selection.html', image_path=template_path)


# # # Route for storing rectangle coordinates
# # @app.route("/storeinfile", methods=["POST"])
# # def store_in_file():
# #     global coordinates
# #     data = request.get_json()
# #     coordinates["startX"] = int(data["startX"])
# #     coordinates["startY"] = int(data["startY"])
# #     coordinates["endX"] = int(data["endX"])
# #     coordinates["endY"] = int(data["endY"])
# #     return jsonify({"message": "Coordinates saved successfully"}), 200

# @app.route("/storeinfile", methods=['POST'])
# def store_coordinates():
#     """
#     Store coordinates sent from the frontend.
#     """
#     data = request.get_json()
#     if not data:
#         return {"error": "No data received"}, 400

#     startX = data.get('startX')
#     startY = data.get('startY')
#     endX = data.get('endX')
#     endY = data.get('endY')

#     print(f"Received coordinates: start=({startX}, {startY}), end=({endX}, {endY})", flush=True)

#     # Save coordinates for future use
#     coordinates = {
#         "startX": startX,
#         "startY": startY,
#         "endX": endX,
#         "endY": endY,
#     }
#     with open('coordinates.json', 'w') as f:
#         json.dump(coordinates, f)

#     return {"message": "Coordinates saved successfully!"}, 200


# @app.route("/processimage", methods=["GET"])
# def process_image():
#     global certificate_template, coordinates
#     if not certificate_template:
#         return jsonify({"error": "Template missing"}), 400

#     if not coordinates:
#         return jsonify({'error': 'Coordinates missing'}), 400


#     try:
#         # Read the names from the data file
#         df = pd.read_csv(DATA_FILE)
#         names = df["Name"]

#         # Load the template image
#         template = cv2.imread(certificate_template)
#         if template is None:
#             print("Failed to load certificate template")
#             return jsonify({"error": "Failed to load certificate template"}), 500

#         # Prepare output directory
#         output_paths = []
#         for idx, name in enumerate(names):
#             try:
#                 output_path = os.path.join(OUTPUT_FOLDER, f"certificate_{idx + 1}.jpeg")
#                 print(f"Saving certificate to: {output_path}")

#                 # Generate the certificate
#                 updated_img = add_name(
#                     template.copy(),
#                     name,
#                     coordinates["startX"],
#                     coordinates["startY"],
#                     coordinates["endX"],
#                     coordinates["endY"],
#                 )

#                 # Save the updated image
#                 success = cv2.imwrite(output_path, updated_img)
#                 if not success:
#                     print(f"Failed to save certificate for {name} at {output_path}")
#                 else:
#                     output_paths.append(output_path)

#             except Exception as e:
#                 print(f"Error generating certificate for {name}: {e}")

#         # Check if any certificates were generated
#         if not output_paths:
#             return jsonify({"error": "No certificates were generated"}), 500

#         # Return the first generated certificate for download (example)
#         return send_file(
#             output_paths[0], as_attachment=True, download_name="certificate.jpeg"
#         )

#     except Exception as e:
#         print(f"Error processing certificates: {e}")
#         return jsonify({"error": str(e)}), 500



# if __name__ == "__main__":
#     app.run(debug=True)
