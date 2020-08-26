 from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, User!!'

@app.route('/Afraz')
def hi():
    return 'Hello, Afraz'

@app.route('/user/<username>')  
def hi1(username):
    return 'Hello, ' + username

@app.route('/User/<username3>')
def hi3(username3):
    return f'Afraz, {username3}'

@app.route('/User/<int:id>')
def hi4(id):
    return f'This is your id : {id}'

@app.route('/User/<path:path5>')
def hi5(path5):
    return f"""This is the path to the directory ' {path5} '"""







