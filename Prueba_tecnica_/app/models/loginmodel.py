from models.loginuser import login
from datetime import date, timedelta
from core.config import db

class ModelUser():

    @classmethod
    def login(cls, user):
        try:
            users_data = login.query.filter_by(useraccess=user.useraccess).first()
            if users_data != None: 
                if login.regenerate_password(users_data.ExpirationAcces, users_data.tokenaccess):
                    user_resp = login(users_data.id, users_data.useraccess, login.check_password(users_data.PassAccess, user.PassAccess), login.regenerate_password(users_data.ExpirationAcces,users_data.tokenaccess), users_data.ExpirationAcces)
                    users_data.tokenaccess = user_resp.tokenaccess
                    users_data.ExpirationAcces = date.today() + timedelta(days=2)
                    db.session.commit()
                    return user_resp
                else:
                    user_resp = login(users_data.id, users_data.useraccess, login.check_password(users_data.PassAccess, user.PassAccess), users_data.tokenaccess, users_data.ExpirationAcces)
                    return user_resp
            else:    
                return None
        except Exception as ex:
            raise Exception(ex)
    
    


