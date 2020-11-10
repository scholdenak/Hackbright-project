"""CRUD functions"""

from model import db, Date_liked, User, Date_idea,connect_to_db

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
    <Date_idea idea_id=2 date_name=test2>"""

    date_idea = Date_idea(date_name=date_name, description=description, is_video=is_video,
    is_socially_distant=is_socially_distant, is_co_quarantined=is_co_quarantined,
    is_outside=is_outside, is_at_home=is_at_home, submitted_by=submitted_by)

    db.session.add(date_idea)
    db.session.commit()

    return date_idea

if __name__=='__main__':
    from server import app
    connect_to_db(app)