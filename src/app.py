from flask import Flask
from flask_restful import Resource, Api
import flask_sqlalchemy
from routes.homes.route import HomeRoute, HomeRouteWithId
from utils.db import db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sql"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    api = Api(app)
    db.init_app(app) # Initialize the database
    db.create_all(app=app) # Create tables
    api.add_resource(HomeRoute, '/')
    api.add_resource(HomeRouteWithId, '/<string:id>')
    return app

