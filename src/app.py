from flask import Flask, render_template, request, redirect
import sys
import os  

import src.main as processfn
from read_csv.Names import Names

data_path = '../Assets/Data-for-Certificate.xlsx'
image = '../Assets/Certificate.jpeg'
app = Flask(__name__, template_folder="frontend")
i = 0

startX = startY = endX = endY = ""

@app.route("/")
def home():
    return render_template('rectangle.html')

@app.route("/storefile", methods=['POST'])
def storefile():
    global i
    
    file = request.files['imageLoader']
    image_filename = f"image{i}.jpeg"
    image_dir = "uploads"  
    os.makedirs(image_dir, exist_ok=True)  
    
    image_path = os.path.join(image_dir, image_filename)  
    i += 1
    file.save(image_path)

    with open("frontend_data.txt", "a") as fh:
        fh.write(f"imagePath: {image_path}\n")

    return redirect('/')


@app.route("/storeinfile", methods=['POST'])
def storeinfile():
    data = request.get_json()
    startX = int(data['startX'])
    startY = int(data['startY'])
    endX = int(data['endX'])
    endY = int(data['endY'])

    with open("frontend_data.txt", "a") as fh:
        fh.write(f"startX: {startX}, startY: {startY}, endX: {endX}, endY: {endY} ")

    return redirect('/')
    


@app.route("/processimage")
def processImage():
    """
    Calls the main in openCV
    """
    NAMES = Names(data_path)
    is_sign_added = True
    is_watermark_added = True
    image_path = "uploads/image0.jpeg"  
    finimg = processfn.main(image_path, is_sign_added, is_watermark_added, NAMES, startX, startY, endX, endY)
    
    # file = request.files['imageLoader']
    image_filename = f'image{i}.jpeg'
    image_dir = "uploads"  
    os.makedirs(image_dir, exist_ok=True)  
    
    image_path = os.path.join(image_dir, image_filename)  
    i += 1
    finimg.save(image_path)


    return redirect('/storefile')
 


