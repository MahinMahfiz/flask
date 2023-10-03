def RegisterValidation(username,password,email,userrole,usertype):
    if (
        isinstance(username, str) and
        0 < len(username) <= 50 and
        2 < len(password) <= 50 and
        isinstance(email, str) and
        0 < len(email) <= 100 and
        isinstance(userrole, str) and
        0 < len(username) <= 20 and
        isinstance(usertype, str) and
        0 < len(username) <= 20
    ):
        return True
    else:
        return False