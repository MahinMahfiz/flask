from flask import Flask
from user.route.user_route import user_route
from config import db,bcrypt
app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
bcrypt.init_app(app)
#routes
#user
app.register_blueprint(user_route, url_prefix="/user")



if __name__ == '__main__':
    app.run(debug=True)