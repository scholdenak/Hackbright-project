"""CRUD functions"""

from model import db, DateLiked, User, DateIdea,connect_to_db, DatePerson, Preference


def create_user(email, password, fname, lname):
    """creates and returns a new user

    >>> create_user('test2@test2', 'test2', 'test2', 'test2')
    <User user_id=2 email=test2@test2 fname=test2 lname=test2>"""

    user = User(email=email, password=password, fname=fname, lname=lname)

    db.session.add(user)
    db.session.commit()

    return user
    

def get_user_by_email(email):
    "Return a user from their email"

    return User.query.filter_by(email=email).first()


def create_date_idea(date_name, description, is_video, is_socially_distant, is_co_quarantined, is_outside, is_at_home, submitted_by):
    """creates a date idea
    
    >>> create_date_idea('test2', 'test2', True, True, True, True, True, 1)
    <DateIdea idea_id=2 date_name=test2>"""

    date_idea = DateIdea(date_name=date_name, description=description, is_video=is_video,
    is_socially_distant=is_socially_distant, is_co_quarantined=is_co_quarantined,
    is_outside=is_outside, is_at_home=is_at_home, submitted_by=submitted_by)

    db.session.add(date_idea)
    db.session.commit()

    return date_idea


def add_date_liked(user_id, idea_id):
    """adds a date id to the liked date table with user id"""

    liked_date = DateLiked(user_id=user_id, idea_id=idea_id)

    db.session.add(liked_date)
    db.session.commit()

    return liked_date


def get_user_liked_id(user_id):
    """queries for all of a user's liked_id"""

    return DateLiked.query.filter_by(user_id=user_id).all()


# TODO(NE) make query to check if date already exists in user liked dates
# in server.py line 148 check if already in

def get_date_liked(user_id, idea_id):
    """gets the date liked by the user id and the date id"""

    return DateLiked.query.filter(DateLiked.user_id==user_id,
                             DateLiked.idea_id==idea_id).first()


def create_date_person(user_id, name, relationship_type):
    """Adds a date person that user will be going on date with"""

    date_person = DatePerson(user_id=user_id, name=name, relationship_type=relationship_type)

    db.session.add(date_person)
    db.session.commit()

    return date_person

def create_person_preferences(user_id, date_person_id,
                            is_video, is_socially_distant,
                            is_co_quarantined, is_outside,
                            is_at_home):
    """adds preferences to table connected to user_id and date_person_id"""

    person_prefs = Preference(user_id=user_id, date_person_id=date_person_id,
                            is_video=is_video, is_socially_distant=is_socially_distant,
                            is_co_quarantined=is_co_quarantined, is_outside=is_outside,
                            is_at_home=is_at_home)

    db.session.add(person_prefs)
    db.session.commit()

    return person_prefs


def get_date_people_by_user_id(user_id):
    """queries all date people by the user_id"""

    return DatePerson.query.filter(DatePerson.user_id==user_id).all()


def get_date_person_id(user_id, name):
    """get the person id by name and user_id"""

    return DatePerson.query.filter(DatePerson.user_id==user_id,
                             DatePerson.name==name).first().date_person_id


def generate_from_person_id(date_person_id):
    """generates a new date from person_id preferences"""

    person_prefs = Preference.query.filter(Preference.date_person_id==date_person_id).first()
   
    # person_prefs.attribute == 
    print(f'\n\n{person_prefs}')

    if person_prefs.is_video == True:
        bubble = (DateIdea.is_video == True)

    if person_prefs.is_socially_distant == True:
        bubble = (DateIdea.is_socially_distant == True)

    if person_prefs.is_co_quarantined == True:
        bubble = (DateIdea.is_co_quarantined == True)

    if person_prefs.is_outside == True and person_prefs.is_at_home == False:
        location = (DateIdea.is_outside == True)

    if person_prefs.is_at_home == True and person_prefs.is_outside == False:
        location = (DateIdea.is_at_home == True)

    if person_prefs.is_at_home == True and person_prefs.is_outside == True:
        location = ((DateIdea.is_at_home == True) | (DateIdea.is_outside == True))
    
    q = DateIdea.query

    return q.filter(bubble,location).all()

    # date_options = q.filter(DateIdea.is_video == is_video, DateIdea.is_socially_distant == is_socially_distant,
    # DateIdea.is_co_quarantined == is_co_quarantined, DateIdea.is_at_home == is_at_home, 
    # DateIdea.is_outside == is_outside).all()







if __name__=='__main__':
    from server import app
    connect_to_db(app)