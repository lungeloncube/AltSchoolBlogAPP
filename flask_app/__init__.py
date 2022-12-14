########## THIS FILE CONTAINS ALL THE IMPORTS AND DATABASE INSTANCES ##########
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_app.config import Config

# initialize all the extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


# Define a function for creating the app
def create_app(config_class=Config):
    basedir = os.path.abspath(os.path.dirname(__file__))
    # create flask app instance
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'blog.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config.from_object(Config)

    # now pass the app to all of those extensions
    db.init_app(app)
    import flask_app.models

    with app.app_context():
        db.create_all()
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # import blueprints
    from flask_app.users.routes import users
    from flask_app.posts.routes import posts
    from flask_app.main.routes import main
    from flask_app.errors.handlers import errors

    # now register all these blueprints
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    # now return the app that we have created above
    return app
