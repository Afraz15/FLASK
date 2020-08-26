from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == 'POST':
        usr = request.form['nm']
        return redirect(url_for('u', user = usr))
    else:
        return render_template('jinja 4.html')

@app.route('/<user>')
def u(user):
    return f'hello {user}'
