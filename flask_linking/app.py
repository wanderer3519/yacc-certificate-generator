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
        data = f"startX: {startX}, startY: {startY}, endX: {endX}, endY: {endY}\n"
        fh.write(data)
    return redirect('rectangle.html') 
