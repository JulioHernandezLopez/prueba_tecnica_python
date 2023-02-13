from flask import  render_template, request, redirect, url_for, jsonify, make_response


from core.config import app
from models.loginmodel import ModelUser
from models.loginuser import login





@app.route('/')
def index():
    return redirect(url_for('login_home'))

@app.route('/login', methods=['GET','POST'])
def login_home():
    if request.method=='POST':
        user = login(0,request.form['username'], request.form['password'], '', '')
        logged_user = ModelUser.login(user)
        if  logged_user!=None:
            if logged_user.PassAccess:
                response = make_response(jsonify({'token': f'{logged_user.tokenaccess}', 'descripcionRespuesta': '', 'estado':f'{logged_user.PassAccess}'}),400)
                return response
            else:
                response = make_response(jsonify({'estado': 'false', 'descripcionRespuesta': 'Usuario o contrasenia incorrecto'}),400)
                return response
        else:
            response = make_response(jsonify({'estado': 'false', 'descripcionRespuesta': 'Usuario o contrasenia incorrecto'}),400)
            return response
    else:
       return render_template('auth/login.html')



if __name__ == 'main':
    app.run(Debug=True)
