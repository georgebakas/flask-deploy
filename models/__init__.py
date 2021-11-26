'''
Now we’ll add a SQLAlchemy model for the User object, and a database engine initialization code. 

The User object won’t be used by our demo app in any meaningful way, 
but we’ll need it to make sure database migrations work and SQLAlchemy-Flask integration is set up correctly.

Note how UUID is generated automatically as an object ID by default expression.

'''

import uuid
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String())
    email = db.Column(db.String(), unique=True)