"""Script to seed database."""

import os
import json
from random import choice

import crud
import model
import server

os.system('dropdb corona-dates')
os.system('createdb corona-dates')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/date_data.json') as f:
    date_data = json.loads(f.read())

dates_in_db = []
for date in date_data:
    date_name, description, is_video, is_socially_distant, is_co_quarantined, is_outside, is_at_home = (date['date_name'],
                                                                                                        date['description'],
                                                                                                        date['is_video'],
                                                                                                        date['is_socially_distant'],
                                                                                                        date['is_co_quarantined'],
                                                                                                        date['is_outside'],
                                                                                                        date['is_at_home'])
    db_date = crud.create_date_idea(date_name, 
                                    description, 
                                    is_video, 
                                    is_socially_distant, 
                                    is_co_quarantined, 
                                    is_outside, 
                                    is_at_home,
                                    submitted_by='admin')
    dates_in_db.append(db_date)

with open('data/user_data.json') as u:
    user_data = json.loads(u.read())

users_in_db = []
for user in user_data:
    email, password, fname, lname = (user['email'],
                                    user['password'],
                                    user['fname'],
                                    user['lname'])
    db_user = crud.create_user(email, password, fname, lname)
    users_in_db.append(db_user)

# # Create 10 users; each user will make 10 ratings
# for n in range(10):
#     email = f'user{n}@test.com'  # Voila! A unique email!
#     password = 'test'

#     user = crud.create_user(email, password)

#     for _ in range(10):
#         random_movie = choice(movies_in_db)
#         score = randint(1, 5)

#         crud.create_rating(user, random_movie, score)