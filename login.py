from flask import request, Flask, render_template

app = Flask(__name__)

@app.route('/login', methods=[ 'GET' ])

def login():
    if request.method == 'POST':
        if valid_login(request.form['username'],
                        request.form['password']):
                        log_the_user_in(request.form['username'])
        else:
            return render_template('jin.html')
#            error = 'invalid username/password'
    else:
        return render_template('jin.html ')




    '''
def login():
    if request.method == 'POST' :
        return 'Done'
    else:
        failed
        #return render_template('jin.html')
# the request.mathod is from @app.route
    '''

    '''
    this is right
    if request.method == 'POST':
        return 'hello'
    else:
        return render_template('jin.html')
    '''




