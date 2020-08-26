from flask import Flask, session, request, url_for, redirect, render_template
from datetime import timedelta

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(minutes=5)
app.secret_key = "hello"
@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nam']
        session['user'] = user
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            return redirect(url_for('user'))
        else:
            return render_template('jinja 5.html')

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return f'hello {user}'
    else:
        return '<h1>permission not granted</h1>'

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
