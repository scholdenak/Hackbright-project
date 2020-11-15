"""CRUD functions"""

from model import db, DateLiked, User, DateIdea,connect_to_db

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



def query_date():
    """queries through date ideas"""
    pass
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
def filter_date_ideas(form[bubble], form[location]):
    """queries date options with arguments of bubble and location from form"""

# q = date idea query start
    q = DateIdea.query
# form answer bubble = bubble variable
    bubble = form[bubble]
# form answer location = location variable
    location = form[location]
# if location variable is both:
    if location = 'both':
#   date options = query DateIdeas WHERE ((bubble variable) = True, 
#                                 home is True or outside is True) all
        date_options = q.filter(DateIdea.bubble == True, 
                                (DateIdea.location == True)).all()
# else:
    else:
#   date options = query DateIdeas WHERE ((bubble variable) = True,
#                                 (location variable) is True) all
        date_options = q.filter(DateIdea.bubble == True, 
                                (DateIdea.location == True)).all()

 return date option

# in server.py function
# function to pick random out of date_options

    

def select_date():
    pass


if __name__=='__main__':
    from server import app
    connect_to_db(app)