from flask import Blueprint
import socket
from user.controller.user_controller import Register
user_route = Blueprint("user_route",__name__)


@user_route.route("/register",methods=['POST'])
def UserRegister():
    return Register()