"""Server for covid date generator app."""
from crud import get_user_by_email
from flask import (Flask, render_template, request, flash, session,
                   redirect, url_for)
from model import connect_to_db, User, DateIdea
import random
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
# @app.route('/dates-liked')
# def show_dates_liked():
#     """Shows all the dates the user likes"""

#     return render_template('dates-liked.html')


@app.route('/generate-date')
def start_date_generator():
    """Allows user to pick options for date"""

    return render_template('generate-date.html')


@app.route('/date-selection')
def show_date_selection():
    """From users submission selects a date and shows details"""

    return redirect('/date-selection')

@app.route('/date-selection', methods=['POST'])
def generate_preferred_date():
    """uses form selections to query dates"""

    bubble_data = request.form['bubble']
    location_data = request.form['location']
    q = DateIdea.query
    
    if bubble_data == "is_video":
        if location_data == "is_outside":
            date_options = q.filter(DateIdea.is_video == True, 
                                           DateIdea.is_outside == True).all()

        if location_data == "is_at_home":
            date_options = q.filter(DateIdea.is_video == True, 
                                           DateIdea.is_at_home == True).all()

        if location_data == 'both':
            date_options = q.filter(DateIdea.is_video == True, 
                                           ((DateIdea.is_at_home == True) |
                                           (DateIdea.is_outside == True))).all()

    if bubble_data == "is_socially_distant":
        if location_data == "is_outside":
            date_options = q.filter(DateIdea.is_socially_distant == True, 
                                        DateIdea.is_outside == True).all()

 
        if location_data == "is_at_home":
            date_options = q.filter(DateIdea.is_socially_distant == True, 
                                        DateIdea.is_at_home == True).all()

        if location_data == 'both':
            date_options = q.filter(DateIdea.is_socially_distant == True, 
                                           ((DateIdea.is_at_home == True) |
                                           (DateIdea.is_outside == True))).all()

    if bubble_data == "is_co_quarantined":
        if location_data == "is_outside":
            date_options = q.filter(DateIdea.is_co_quarantined == True, 
                                        DateIdea.is_outside == True).all()

        if location_data == "is_at_home":
            date_options = q.filter(DateIdea.is_co_quarantined == True, 
                                        DateIdea.is_at_home == True).all()
   
        if location_data == 'both':
            date_options = q.filter(DateIdea.is_co_quarantined == True, 
                                           ((DateIdea.is_at_home == True) |
                                           (DateIdea.is_outside == True))).all()

    date_choice = (random.choice(date_options))

    # return date_options
    return render_template ('date-selection.html', date_choice=date_choice)

@app.route('/dates-liked')
def show_dates_liked():

    return render_template('dates-liked.html')
    
# def logout

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
