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

if __name__=='__main__':
    from server import app
    connect_to_db(app)