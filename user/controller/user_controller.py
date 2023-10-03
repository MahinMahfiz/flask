from flask import request,jsonify
from user.validation.register_validation import RegisterValidation
from user.services.user_services import RegistrationServices
from config import bcrypt
def Register():
    data = request.get_json()
    if data:
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        userrole = data.get('userrole')
        usertype = data.get('usertype')
        valid = RegisterValidation(username,password,email,userrole,usertype)

        if valid:
            return RegistrationServices(username,password,email,userrole,usertype)
        else:
            return jsonify({"msg":"Invalid input"})
        
    else:
        return jsonify({"msg":"Fields cannot be empty"})