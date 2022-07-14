from flask import Flask
from flask_restful import Resource, Api
from routes.homes.route import HomeRoute, HomeRouteWithId

app = Flask(__name__)
api = Api(app)

api.add_resource(HomeRoute, '/')
api.add_resource(HomeRouteWithId, '/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)