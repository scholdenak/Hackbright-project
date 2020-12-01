"""Models for corona date app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  """App users."""

  __tablename__ = 'users'

  user_id = db.Column(db.Integer,
                      autoincrement=True,
                      primary_key=True)
  email = db.Column(db.String, unique=True)
  password = db.Column(db.String)
  fname = db.Column(db.String)
  lname = db.Column(db.String)

  def __repr__(self):
      return f'<User user_id={self.user_id} email={self.email} fname={self.fname} lname={self.lname}>'


class DateIdea(db.Model):
    """Date ideas"""

    __tablename__ = 'dates'

    idea_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date_name = db.Column(db.String)
    description = db.Column(db.String)
    is_video = db.Column(db.Boolean)
    is_socially_distant = db.Column(db.Boolean)
    is_co_quarantined = db.Column(db.Boolean)
    is_outside = db.Column(db.Boolean)
    is_at_home = db.Column(db.Boolean)
    picture = db.Column(db.String)
    submitted_by = db.Column(db.String)
    
    #  db.ForeignKey('users.user_id'))

    # user = db.relationship('User', backref='users')

    def __repr__(self):
        return (f'<DateIdea idea_id={self.idea_id} date_name={self.date_name}' 
        f' is_video={self.is_video} is_socially_distant={self.is_socially_distant}'
        f' is_co_quarantined={self.is_co_quarantined} is_outside={self.is_outside}'
        f' is_at_home={self.is_at_home}>')
    #     #  submitted_by={self.submitted_by}>'


class DateLiked(db.Model):
    """Dates that have been liked"""

    __tablename__ = 'dates_liked'

    liked_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    idea_id = db.Column(db.Integer, db.ForeignKey('dates.idea_id'))

    user = db.relationship('User', backref='dates_liked')
    idea = db.relationship('DateIdea', backref='dates_liked')

    def __repr__(self):
        # return f'{self.idea.date_name}'
        return f'<DateLiked liked_id={self.liked_id} user_id={self.user_id} idea_id={self.idea_id}>'


class DatePerson(db.Model):

    __tablename__ = 'people'

    date_person_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    name = db.Column(db.String)
    relationship_type = db.Column(db.String)

    user = db.relationship('User', backref='people')

    def __repr__(self):
        return f'<DatePerson date_person_id={self.date_person_id} name={self.name}>'


class Preference(db.Model):

    __tablename__ = 'preferences'

    preference_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    date_person_id = db.Column(db.Integer, db.ForeignKey('people.date_person_id'))
    is_video = db.Column(db.Boolean)
    is_socially_distant = db.Column(db.Boolean)
    is_co_quarantined = db.Column(db.Boolean)
    is_outside = db.Column(db.Boolean)
    is_at_home = db.Column(db.Boolean)

    user = db.relationship('User', backref='preferences')
    person = db.relationship('DatePerson', backref='preferences')

    def __repr__(self):
        return f'\n\n <Preference preference_id={self.preference_id} user_id={self.user_id} \
            date_person_id={self.date_person_id} is_video={self.is_video} \
            is_socially_distant={self.is_socially_distant} \
            is_co_quarantined={self.is_co_quarantined} \
            is_outside={self.is_outside} is_at_home={self.is_at_home}>'

def connect_to_db(flask_app, db_uri='postgresql:///corona_dates', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)