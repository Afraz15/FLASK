from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello user'

@app.route('/login')
def login():
    return 'this is your login page' 

@app.route('/user/<yo>')
def name(yo):
    return f'hello bro {yo}'

@app.route('/<path:yo>')
def path(yo):
    return f'this is the path {yo} ' 

@app.route('/<int:num>')
def id(num):
    return f'this is your id : {num}'






