"""Server for covid date generator app."""
from crud import get_user_by_email
from flask import (Flask, render_template, request, flash, session,
                   redirect, url_for)
from model import connect_to_db, User

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "'dflkghnm'[pdftnhmp"
app.jinja_env.undefined = StrictUndefined

@app.route('/', methods=['GET'])
def show_homepage():
    """Show homepage"""

    return render_template('homepage.html')



@app.route('/', methods=['POST'])
def login():
    """user enters email and password to move to preferences"""
    
    user = get_user_by_email(request.form['email'])
    if user == None:
        flash('Invalid Credentials. Please try again.')
        return render_template('homepage.html')

    else:
        if request.form['password'] != user.password:
            flash('Invalid Credentials. Please try again.')
            return render_template('homepage.html')
        
        else:
            session['current_user'] = user.fname
            return redirect('/main-menu') 

@app.route('/main-menu')
def show_main_menu():
    """Go to references page"""

    return render_template('main-menu.html')

# TODO
@app.route('/dates-liked')
def show_dates_liked():
    """Shows all the dates the user likes"""

    return render_template('dates-liked.html')


@app.route('/generate-date')
def start_date_generator():
    """Allows user to pick options for date"""

    return render_template('generate-date.html')


@app.route('/date-selection')
def show_date_selection():
    """From users submission selects a date and shows details"""

    # ask user for input in form in html for preferences
    # pull preferences answers from forms
    # if preference == true
        # select random from preference with true

        # if self.attribute = form anwer and self.attribute = form answer and self.attribute = form answer:
            # select random from date_idea class 
            #   self.attribute = form anwer and self.attribute = form answer and self.attribute = form answer
        # SELECT random FROM date_idea WHERE 
        
    return render_template('date-selection.html')

# def logout

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
