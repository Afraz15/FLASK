#from markupsafe import escape
from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def hi(name):
    #return 'hello %s' % escape(name)
    return f'hello {name}'

print(hi('yo'))








