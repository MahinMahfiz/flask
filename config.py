# config
# @Author md mahin mahfiz <mahin.m360ict@gmail.com>

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import sentry_sdk
db = SQLAlchemy()

SQLALCHEMY_DATABASE_URI = 'postgresql://armaan:123456@192.168.0.227:5432/Property360'
SQLALCHEMY_TRACK_MODIFICATIONS = False

bcrypt = Bcrypt()

sentry_sdk.init(
    dsn="https://0f01b4913a0d75feefb0d917e9b14475@o4505974199156736.ingest.sentry.io/4505985888878593",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)


