from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug import generate_password_hash, check_password_hash
from . import  db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True)
    _password = db.Column(db.String(123))
    email_confirmed = db.Column(db.Boolean)
    
    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = generate_password_hash(plaintext)

    def is_correct_password(self, plaintext):
        return check_password_hash(self._password, plaintext)