from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = '024d0dc3a9588cd5b9474f27df153c9b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Faça login para acessar essa página'
login_manager.login_message_category = 'alert-info'


from blogdosdevs import routes
