"""Server for covid date generator app."""
from crud import get_user_by_email
from flask import (Flask, render_template, request, flash, session,
                   redirect, url_for)
from model import connect_to_db, User

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "'dflkghnm'[pdftnhmp"
app.jinja_env.undefined = StrictUndefined

@app.route('/', methods=['GET', 'POST'])
def login():
    """user enters email and password to move to preferences"""
    # error = None
    if request.method == 'POST':
        user = get_user_by_email(request.form['email'])
        if user == None:
            flash('Invalid Credentials. Please try again.')
            return render_template('homepage.html')
        else:
            if request.form['password'] != user.password:
                flash('Invalid Credentials. Please try again.')
            else:
                # flash('Login Successful')
                session['current_user'] = user.fname
                return redirect('/main-menu')
    return render_template('homepage.html')
    # , error=error)

@app.route('/main-menu')
def show_main_menu():
    """Go to references page"""

    return render_template('main-menu.html')

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

    return render_template('date-selection.html')

# def logout

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
