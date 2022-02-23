from flask import Flask, render_template, request

app = Flask(__name__)

names = []
orgs = []


@app.get('/')
def index():
    py_name = request.args.get('queryname')
    return render_template('index.html', name=py_name)




@app.post('/submit')
def submit():
    name = request.form.get('name')
    org = request.form.get('org')
    names.append(name)
    orgs.append(org)
    return render_template('submit.html', names = names, orgs = orgs)