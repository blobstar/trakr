from re import DEBUG
from flask import Flask
from flask_login import login_user, logout_user, current_user, login_required, LoginManager

from routes import init_routes
from models import get_user_by_id



app = Flask(__name__)
  

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User loader function
@login_manager.user_loader
def load_user(user_id):
    return get_user_by_id(user_id)

init_routes(app)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)