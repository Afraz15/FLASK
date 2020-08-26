from flask import Flask, request, session, redirect, url_for, render_template, flash

app = Flask(__name__)
app.secret_key = 'hello'

@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == 'POST':
        session['user'] = request.form['nam']
        return redirect(url_for('user'))
    else:
        return render_template('jinja 6.html')

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return f'hello {user}'
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    if 'user' in session:
        user = session['user']
        flash(f'you have been logged out!{user}', 'info')
    session.pop('user', None)
    return redirect(url_for('login'))




