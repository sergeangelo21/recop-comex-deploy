from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy 
from flask_mail import Mail
from flask_migrate import Migrate

bcrypt = Bcrypt()
login = LoginManager()
db = SQLAlchemy()
mail = Mail()
migrate = Migrate()