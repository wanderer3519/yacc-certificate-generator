from flask import Flask,render_template, request ,redirect, url_for
import sys
sys.path.append('..')
import openCV.main as processfn


app = Flask(__name__,template_folder="frontend") 

@app.route("/")
def home():
    return render_template('rectangle.html')

@app.route("/storeinfile", methods=['POST']) 
def StoringInFile(): 
    data = request.json
    with open("frontend_data.txt", "a") as fh:
        global startX, startY, endX, endY
        startX = int(data['startX'])
        startY = int(data['startY'])
        endX = int(data['endX'])
        endY = int(data['endY'])
        imagepath = '../Assets/"Certificate.jpeg'
        data = f"startX: {startX}, startY: {startY}, endX: {endX}, endY: {endY}\n"
        fh.write(data)
    return redirect('rectangle.html') 
# call openCV
# main(true, true, data, coords)

@app.route("/processimage")
def processImage():
    '''
        Calls the main in openCV
    '''
    NAMES = ['1', '2']
    is_sign_added = True
    is_watermark_added = True
    finimg = processfn.main(is_sign_added, is_watermark_added, NAMES, startX, startY, endX, endY)
    return redirect('/')


