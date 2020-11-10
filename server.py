"""Server for covid date generator app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, url_for)
from model import connect_to_db

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "'dflkghnm'[pdftnhmp"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage"""

    # if user not in session:
    return render_template('homepage.html')

# @app.route('/login')
# def login():
#     pass

# @app.route("/login", methods=["GET"])
# def show_login():
#     """Show login form."""

#     return render_template("login.html")


# @app.route("/login", methods=["POST"])
# def process_login():
#     """Log user into site.

#     Find the user's login credentials located in the 'request.form'
#     dictionary, look up the user, and store them in the session.
#     """

    # TODO: Need to implement this!

    # The logic here should be something like:
    #
    # - get user-provided name and password from request.form
    # - use customers.get_by_email() to retrieve corresponding Customer
    #   object (if any)
    # - if a Customer with that email was found, check the provided password
    #   against the stored one
    # - if they match, store the user's email in the session, flash a success
    #   message and redirect the user to the "/melons" route
    # - if they don't, flash a failure message and redirect back to "/login"
    # - do the same if a Customer with that email doesn't exist

#     return "Oops! This needs to be implemented"

# @app.route('/register', methods=['POST'])
# def register_user():
#     email = request.form['email']
#     password = request.form['password']

#     user = get_user_by_email(email)
#     if user:
#         return 'A user already exists with that email.'
#     else:
#         create_user(email, password)

#         return redirect('/login-form')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
