from flask import Flask, request, session, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = 'hi'

@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    else:
        return render_template("jin.html")

@app.route('/index')
def index():
    if "username" in session:
        return 'you are logged in'
    else:
        return 'there was some problem'



