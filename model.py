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


class Date_idea(db.Model):
    """Date ideas"""

    __tablename__= 'dates'

    idea_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date_name = db.Column(db.String)
    description = db.Column(db.String)
    is_video = db.Column(db.Boolean)
    is_socially_distant = db.Column(db.Boolean)
    is_co_quarantined = db.Column(db.Boolean)
    is_outside = db.Column(db.Boolean)
    is_at_home = db.Column(db.Boolean)
    submitted_by = db.Column(db.String, db.ForeignKey('users.user_id'))

    user = db.relationship('User', backref='users')

    def __repr__(self):
        return f'<Date_idea idea_id={self.idea_id} date_name={self.date_name} submitted_by={self.submitted_by}>'

def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
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