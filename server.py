"""Server for covid date generator app."""
from crud import get_user_by_email, add_date_liked, get_user_liked_id, get_date_liked, create_date_person
from flask import (Flask, render_template, request, flash, session,
                   redirect, url_for)
from model import connect_to_db, User, DateIdea, DateLiked
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
            session['user_id'] = user.user_id
            return redirect('/main-menu') 


@app.route('/main-menu')
def show_main_menu():
    """Go to references page"""

    return render_template('main-menu.html')


@app.route('/generate-date')
def start_date_generator():
    """Allows user to pick options for date"""

    return render_template('generate-date.html')


@app.route('/date-selection')
def generate_preferred_date():
    """uses form selections to query dates"""

    bubble_data = request.args.get('bubble')
    location_data = request.args.get('location')
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

    return render_template ('date-selection.html', date_choice=date_choice)

# #     kwargs = {'hometown': 'New York', 'university' : 'USC'}
# # User.query.filter_by(**kwargs)
# # # This above line is equivalent to saying...
# # User.query.filter_by(hometown='New York', university='USC')

# TODO refactor into server.py line 80
#     if location == 'both':
# #   date options = query DateIdeas WHERE ((bubble variable) = True, 
# #                                 home is True or outside is True) all
#         date_options = q.filter_by((bubble2) == True, 
#                                 (DateIdea.location == True)).all()
# # else:
#     else:
# #   date options = query DateIdeas WHERE ((bubble variable) = True,
# #                                 (location variable) is True) all
#         date_options = q.filter(DateIdea.bubble == True, 
#                                 (DateIdea.location == True)).all()

#     return date_options


@app.route('/dates-liked')
def show_dates_liked():
    """Shows list of all dates liked"""

    user_id = session['user_id']
    liked_dates = get_user_liked_id(user_id)
    
    return render_template('dates-liked.html', liked_dates=liked_dates)


@app.route('/save-liked-date', methods=["POST"])
def save_liked_date():
    """saves a user's liked date for their liked date page."""

    user_id = session['user_id']
    idea_id = request.form['like']
   
    current_liked = get_date_liked(user_id, idea_id)
    liked_dates = get_user_liked_id(user_id)

    if current_liked in liked_dates:
        return redirect('/dates-liked')

    else:
        add_date_liked(user_id, idea_id)
        return redirect('/dates-liked')


@app.route('/date-people')
def render_date_people():
    """Renders page with all saved date people as well as 
    option to create new person"""

    #TODO add date people from people table so a person can
    # click each one for a date option

    return render_template('date-people.html')


@app.route('/create-person-pref')
def create_new_person_and_prefs():
    """creates a new person with their preferences"""

    user_id = session['user_id']
    name = request.args.get('name')
    relationship_type = request.args.get('relationship')
    create_date_person(user_id, name, relationship_type)

    return render_template('/date-selection')

# def logout

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
