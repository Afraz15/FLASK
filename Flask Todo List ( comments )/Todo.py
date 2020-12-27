from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
    
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Test.db'
#Here, we are telling our app the location of our database
# in sqlite:///, /// means to make the database in this folder/locatoin and //// means to specify the location like in other directory or some other folder
db = SQLAlchemy(app)

class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #Now we make our database structure
    Detail = db.Column(db.String(150), nullable=False)
    #id and detail are two columns
    #db.Column = make a clumn in our database file
    #db.integer = allowed data type is numbers only
    #db.String = allowed data type is String only,(150) = you can only type 150 characters?/words? in it
    #primary_key = It will restrict our database to make same/dublicate id
    #nullable = assigning it to false means that the user cannot leave it blank (it won't make any blank detail row)
    time_created = db.Column(db.DateTime, default=datetime.utcnow)
    #same as above,utcnow will automatically
    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        content_list = request.form['detail']
        #in request form, we put in the 'name=' from the form
        new_task = Work(Detail=content_list)
        # Now we are assigning Detail (from our database) = to the data entered in the form
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
            # Trying to commit/send our data to our database
        except:
            return 'there was an error commiting your data'
    else:
        tasks = Work.query.order_by(Work.time_created).all()
        return render_template('body.html', tasks = tasks)  
        # tasks = tasks means we are sharing a variable from this file with that rendered file      
    #render the jinja block file instead of the main html file

@app.route('/delete/<int:id>')
def delete(id):
    task_del = Work.query.get_or_404(id)
    # calling the id from database
    try:
        db.session.delete(task_del)
        # attempt to delete the id/task
        db.session.commit()
        return redirect('/')
    except:
        return 'there was an error deleting your task'

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    task = Work.query.get_or_404(id)

    if request.method == 'POST':
        task.Detail = request.form['detail']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'there was an error updating your data'
    else:
        return render_template('update.html', task=task)



if __name__ == "__main__":
    app.run(debug=True)

# To make db file
# we type python then type from name_of_your_file import db
# then db.create_all() and DONE
