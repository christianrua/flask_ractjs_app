from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    #app = Flask(__name__)

    app = Flask(__name__, static_folder='../../react-movie-list/build', static_url_path='/')

    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'

    db.init_app(app)
    
    from .views import main
    app.register_blueprint(main)



    return app