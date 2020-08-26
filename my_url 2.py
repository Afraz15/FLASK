from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/login2')
def login2():
    return 'hello login page'

@app.route('/<username>')
def user(username):
    return f'hello {username}'

with app.test_request_context():
    print(url_for('login'))





