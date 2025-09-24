from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap5 import Bootstrap
from flask_login import LoginManager

app = Flask( __name__ )
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

# Create database connection object
db = SQLAlchemy()
db.init_app(app)

# Activate login plugin
login_manager = LoginManager(app)

#redirection automatique si pas login
login_manager.login_view = "login"

Bootstrap(app)