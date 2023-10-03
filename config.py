from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
db = SQLAlchemy()

SQLALCHEMY_DATABASE_URI = 'postgresql://armaan:123456@192.168.0.227:5432/Property360'
SQLALCHEMY_TRACK_MODIFICATIONS = False

bcrypt = Bcrypt()



