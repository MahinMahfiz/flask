from flask import jsonify
from sqlalchemy import text
from config import db

def RegistrationServices(username,password,email,userrole,usertype):
    query = text("SELECT property360.registerusers(:username, :password, :email, :userrole, :usertype)")
    try:
        db.session.execute(query, {"username":username,"password":password,"email":email,"userrole":userrole,"usertype":usertype})
        db.session.commit()
        return jsonify({"success":True,"data":{"username":username,"password":password,"email":email,"userrole":userrole,"usertype":usertype}})
    except Exception as e:
        return jsonify({"msg":str(e)})