from flask import Flask, render_template, request

app = Flask(__name__)



@app.get('/')
def index():
    return render_template('index.html')



@app.post('/submit')
def submit():
    num = request.form.get('num')
    return render_template('submit.html', num = num)
