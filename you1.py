                            # RENDER TEMPLATE

from flask import request, Flask
app = Flask(__name__)

@app.route('/upload', method=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['myfiles']
        f.save('/var/uploadfile/upload.txt')

'''
from flask import Flask, render_template,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('jin.html')
'''






























