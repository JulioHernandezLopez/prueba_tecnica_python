from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from datetime import date

from core.config import db

class login(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    useraccess = db.Column(db.String(100), unique=True)
    PassAccess = db.Column(db.String(100))
    tokenaccess = db.Column(db.String(300))
    ExpirationAcces = db.Column(db.Date)

    def __init__(self, id, useraccess, PassAccess, tokenaccess, ExpirationAcces) -> None:
        self.id = id
        self.useraccess = useraccess
        self.PassAccess = PassAccess
        self.tokenaccess = tokenaccess
        self.ExpirationAcces = ExpirationAcces

    @classmethod
    def regenerate_password(self, exp_date, token):
        if exp_date < date.today():
            new_token = generate_password_hash(token)
            return new_token
        else:
            return False
    
    @classmethod
    def check_password(self, hashes_password, password):
        if hashes_password == password:
            return True
        else:
            return False
       
        

   
        


