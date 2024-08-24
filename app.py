from re import DEBUG
from flask import Flask
from flask_login import login_user, logout_user, current_user, login_required, LoginManager
import os
from routes import init_routes
from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
csrf = CSRFProtect(app)


init_routes(app)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)