# user.validation.register_validation
# @Author md mahin mahfiz <mahin.m360ict@gmail.com>

def RegisterValidation(username,password,email,userrole,usertype):
    if (
        isinstance(username, str) and
        0 < len(username) <= 50 and
        2 < len(password) <= 50 and
        isinstance(email, str) and
        0 < len(email) <= 100 and
        isinstance(userrole, str) and
        0 < len(userrole) <= 20 and
        isinstance(usertype, str) and
        0 < len(usertype) <= 20 and
        (userrole == 'buyer' or userrole == 'seller') and
        (usertype == 'buyer' or usertype == 'seller')
    ):
        return True
    else:
        return False