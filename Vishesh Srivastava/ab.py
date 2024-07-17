from flask import Flask,render_template,request,redirect,url_for,jsonify
from datetime import datetime
app = Flask(__name__)

tasks = []
completed=[]
datet=0

@app.route('/todo')
def todo():
    return render_template('todo.html', tasks=tasks,completed=completed)

@app.route('/todo/add_task', methods=['POST'])
def add_task():
    global datet
    content = request.form.get('content')
    heading = request.form.get('heading')
    if content!="":
        datet=datetime.now().strftime("%c")
        tasks.append([content,datet,heading])
    return redirect(url_for('todo'))

@app.route('/todo/complete_task/<int:task_id>')
def complete_task(task_id):
    global datet
    datet=datetime.now().strftime("%c")
    if task_id < len(tasks):
        tasks[task_id][1]=datet
        completed.append(tasks[task_id])
        del tasks[task_id]
    return redirect(url_for('todo'))

@app.route('/todo/update_task/<int:task_index>', methods=['GET', 'POST'])
def update_task(task_index):
    if request.method == 'GET':
        task = tasks[task_index]
        return render_template('todo.html', tasks=tasks, completed=completed, task_to_update=task)
    elif request.method == 'POST':
        updated_content = request.form.get('newcontent')
        updated_heading = request.form.get('newheading')
        if updated_content != "":  
            tasks[task_index][0] = updated_content
            dat=datetime.now().strftime("%c")
            tasks[task_index][1]=dat
        if updated_heading != "":  
            tasks[task_index][2] = updated_heading
            dat=datetime.now().strftime("%c")
            tasks[task_index][1]=dat
        return redirect(url_for('todo'))



