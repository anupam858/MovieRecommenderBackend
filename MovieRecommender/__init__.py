import os
from flask import Flask
import pymongo
from flask_cors import CORS
from . import movies
from .db import mongo

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    cors = CORS(app)
    
    app.config["MONGO_URI"] = os.getenv('DB_URI')
    mongo.init_app(app)
    
    app.config.from_mapping(
        SECRET_KEY= os.getenv('SECRET_KEY')
    )

    app.register_blueprint(movies.movie_bp)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app