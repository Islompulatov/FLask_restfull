from flask_restful import Resource, Api
from flask import request
import uuid

from numpy import append
data = []

class HomeRoute(Resource):
    def get(self):
        print(request)
        return {'data': data}
    def post(self):
        id = str(uuid.uuid4)
        name = request.form["name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        user = {'id' = id, 'name' = name, 'last_name' = last_name, 'email' = email}
        data.append(user)
        return {'data': user}


def find_object_by_id(id):
    for data_object in data:
        if data_object.id = id:
            return data_object
        else:
            return None            
class HomeRouteWithId(Resource):
    def get(self,id):
        data_object = find_object_by_id(id)
        if(data_object):
            return {"data":data_object}
        else:
            return {"data": "Not Found"},404
