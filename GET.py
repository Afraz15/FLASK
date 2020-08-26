from flask import  Flask,request,url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/login', mathods=['GET', 'POST'])
def login():
    if request.mathod == 'POST':
        return do_the_login
    else:
        return show_the_login_form()











