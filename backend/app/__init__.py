from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:sifra@localhost/DataBaseDRS'
db = SQLAlchemy(app)

from backend.app.routs import __init__
