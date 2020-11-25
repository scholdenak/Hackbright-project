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

    # person_prefs = Preference(user_id, date_person_id,
    #                         is_video, is_socially_distant,
    #                         is_co_quarantined, is_outside,
    #                         is_at_home)

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

# def get_date_by_id

# def query_date():
#     """queries through date ideas"""
#     pass
    # DateIdea.query.filter(DateIdea.attribute == bool, 
                        #   DateIdea.attribute == bool).all()

# Take in two attributes at True => all date ideas with those attributes

# examples:
# arguments(is_video=True, is_outside=True)
# output(return all with True is video and True is outside)

# arguments(is_video=True, both=True (is_outside=True or is_at_home=True))
# output(return all with True is video and either outside or home is true)

# Approach(pseudocode):
# function takes in the bubble answer and location answer
# def filter_date_ideas(bubble, location):
#     """queries date options with arguments of bubble and location from form"""

# # q = date idea query start
#     q = DateIdea.query
# # form answer bubble = bubble variable
#     bubble2 = request.form.get('bubble')

#     # print(f'$$$$$$$$$$$$$$$$$$${bubble}$$$$$$$$$$$$$$$$$$$')
# # form answer location = location variable
#     location = request.form.get('location')
# # if location variable is both:

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

# in server.py function
# function to pick random out of date_options

    

# def select_date():
#     pass


if __name__=='__main__':
    from server import app
    connect_to_db(app)