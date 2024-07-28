from flask import Flask,render_template, request ,redirect, url_for
from werkzeug.utils import secure_filename
import sys
sys.path.append('..')
import openCV.main as processfn
from read_csv.Names import Names

data_path = '../Assets/Data-for-Certificate.xlsx'
image = '../Assets/Certificate.jpeg'
app = Flask(__name__,template_folder="frontend") 

@app.route("/")
def home():
    return render_template('rectangle.html')

@app.route("/storeinfile", methods=['POST']) 
def StoringInFile(): 
    data = request.get_json()
    with open("frontend_data.txt", "a") as fh:
        global startX, startY, endX, endY, imagepath
        startX = int(data['startX'])
        startY = int(data['startY'])
        endX = int(data['endX'])
        endY = int(data['endY'])
        imagepath = data['image']
        data = f"startX: {startX}, startY: {startY}, endX: {endX},endY: {endY} image: {imagepath}"
        fh.write(data)
    return redirect('rectangle.html') 
# call openCV
# main(true, true, data, coords)

@app.route("/processimage")
def processImage():
    '''
        Calls the main in openCV
    '''
    NAMES = Names(data_path)
    is_sign_added = True
    is_watermark_added = True
    finimg = processfn.main(image, is_sign_added, is_watermark_added, NAMES, startX, startY, endX, endY)
    return redirect('/')


