from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='../templates')
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@127.0.0.1:3306/pruebatecnica'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = '123root'

db = SQLAlchemy(app)
