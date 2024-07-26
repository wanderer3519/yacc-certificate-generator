from flask import Flask,render_template, request ,redirect

app = Flask(__name__,template_folder="frontend") 

@app.route("/")
def home():
    return render_template('rectangle.html')

@app.route("/storeinfile", methods=['POST']) 
def StoringInFile(): 
    data = request.json
    with open("frontend_data.txt", "a") as fh:
        startX = str(data['startX'])
        startY = str(data['startY'])
        endX = str(data['endX'])
        endY = str(data['endY'])
        imagepath = '../'
        data = f"startX: {startX}, startY: {startY}, endX: {endX}, endY: {endY}\n"
        fh.write(data)
    return redirect('rectangle.html') 
# call openCV
# main(true, true, data, coords)

def processImage():
    pass
    NAMES = ['1', '2']
    is_sign_added = True
    is_watermark_added = False

    '''
        Calls the main in openCV
    '''
