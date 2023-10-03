# user.controller.user_controller
# @Author md mahin mahfiz <mahin.m360ict@gmail.com>

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
            return jsonify({"success":False,"data":"Invalid inputssss"})
        
    else:
        return jsonify({"success":False,"data":"Fields cannot be empty"})