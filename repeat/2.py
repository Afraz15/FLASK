from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello to homepage'

@app.route('/<name>/<age>')
def page(name, age):
    return render_template('index.html', text = name, r = age)




