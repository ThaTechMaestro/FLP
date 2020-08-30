from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('login.html')

database ={"Joseph":"123", "Collins":"123"}

@app.route('/form_login', methods=['POST', 'GET'])
def login():

    name1=request.form['username']
    password=request.form['password']

    if name1 not in database:
        return render_template('login.html', info="Invalid User")
    else:
        if database[name1] != password:
            return render_template('login.html', info="Invalid Passoword")
        else:
            return render_template('home.html',name=name1)