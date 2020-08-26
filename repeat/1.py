from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'this is home page'

@app.route('/<text>')
def user(text):
    return f'this is the text that you typed in {text}'

@app.route('/admin')
def admin():
    return redirect(url_for('home'))

@app.route('/Admin')
def Admin():
    return redirect(url_for('user', name = 'Admin'))

