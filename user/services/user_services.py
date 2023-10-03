# user.services.user_services
# @Author md mahin mahfiz <mahin.m360ict@gmail.com>

from flask import jsonify
from sqlalchemy import text
from config import db
from config import bcrypt
import sentry_sdk
def RegistrationServices(username,password,email,userrole,usertype):
    query = text("SELECT property360.registerusers(:username, :password, :email, :userrole, :usertype)")
    pw_hash = bcrypt.generate_password_hash(password)
    try:
        db.session.execute(query, {"username":username,"password":str(pw_hash),"email":email,"userrole":userrole,"usertype":usertype})
        db.session.commit()
        return jsonify({"success":True,"data":{"username":username,"email":email,"userrole":userrole,"usertype":usertype}})
    except Exception as e:
        db.session.rollback()
        sentry_sdk.capture_exception(e)
        return jsonify({"success":False,"data":str(e)})
    finally:
        db.session.close()