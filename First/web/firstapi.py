from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import os
from pymongo import MongoClient
from pathlib import Path

app = Flask(__name__)
api = Api(app)

client = MongoClient(f"mongodb://db:27017")
db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert_one({
    'num_of_users': 0
})


class Visit(Resource):
    def get(self):
        num = UserNum.find({})[0]['num_of_users']
        num += 1
        UserNum.update({}, {'$set':{'num_of_users':num}})
        return str(f"Hello user {num}")


# def check_data(data, function_name):
#     if "x" not in data or "y" not in data:
#         if 'x' not in data:
#             return 400, "x missing"
#         else:
#             return 400, "y missing"
#     if function_name == "divide":
#         if data["y"] == 0:
#             return 400, "Divide by 0"
#         else:
#             return 200
#     else:
#         return 200


# class Add(Resource):
#     def post(self):
#         data = request.get_json()
#         status_code = check_data(data, "add")
#         if status_code != 200:
#             ret_error = {
#                 "Message": "An error occurred",
#                 "Status Code": status_code
#             }
#             return jsonify(ret_error)
#         x = data["x"]
#         y = data["y"]
#         x = int(x)
#         y = int(y)
#         ret = x+y
#         ret_map = {
#             'Answer': ret,
#             'Status Code': 200
#         }
#         return jsonify(ret_map)


# class Subtract(Resource):
#     def post(self):
#         data = request.get_json()
#         status_code = check_data(data, "subtract")
#         if status_code != 200:
#             ret_error = {
#                 "Message": "An error occurred",
#                 "Status Code": status_code
#             }
#             return jsonify(ret_error)
#         x = data["x"]
#         y = data["y"]
#         x = int(x)
#         y = int(y)
#         ret = x-y
#         ret_map = {
#             'Answer': ret,
#             'Status Code': 200
#         }
#         return jsonify(ret_map)


# class Multiply(Resource):
#     def post(self):
#         data = request.get_json()
#         status_code = check_data(data, "multiply")
#         if status_code != 200:
#             ret_error = {
#                 "Message": "An error occurred",
#                 "Status Code": status_code
#             }
#             return jsonify(ret_error)
#         x = data["x"]
#         y = data["y"]
#         x = int(x)
#         y = int(y)
#         ret = x*y
#         ret_map = {
#             'Answer': ret,
#             'Status Code': 200
#         }
#         return jsonify(ret_map)


# class Divide(Resource):
#     def post(self):
#         data = request.get_json()
#         status_code = check_data(data, "divide")
#         if status_code != 200:
#             ret_error = {
#                 "Message": "An error occurred",
#                 "Status Code": status_code
#             }
#             return jsonify(ret_error)
#         x = data["x"]
#         y = data["y"]
#         x = float(x)
#         y = float(y)
#         ret = x/y
#         ret_map = {
#             'Answer': ret,
#             'Status Code': 200
#         }
#         return jsonify(ret_map)


# api.add_resource(Add, "/add")
# api.add_resource(Subtract, "/subtract")
# api.add_resource(Multiply, "/multiply")
# api.add_resource(Divide, "/divide")
api.add_resource(Visit, "/visit")


# @app.route('/')
# def basic_func():
#     return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")