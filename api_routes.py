from flask import Flask, request, json
from user_dao import *

app = Flask(__name__)


@app.route("/users", methods=['GET', 'POST'])
def api_get_all_users():
    if request.method == 'GET':
        users_list = get_users_list()
        return json.jsonify(users_list)

    if request.method == 'POST':
        info = request.json
        add_new_user(info)
        return {'response': "User added successfully"}


@app.route("/user/<user_id>", methods=['GET'])
def api_get_user_by_id(user_id):
    if request.method == 'GET':
        user = get_user_by_id(user_id)
        return json.jsonify(user)


@app.route("/user/edit/<user_id>", methods=['PUT'])
def api_update_user_by_id(user_id):
    if request.method == 'PUT':
        user = request.json
        update_user_by_id(user_id, user)
        return {'response': 'User updated successfully'}


@app.route("/user/del/<user_id>", methods=["DELETE"])
def api_delete_user_by_id(user_id):
    delete_user(user_id)
    return {'response': 'User deleted successfully'}


if __name__ == '__main__':
    app.run()

"""
    curl -i -H "Content-Type: application/json" 
    -X POST -d '{"username":"maria", "email":"maria@email.com", "password":"m123"}' 
    http://127.0.0.1:5000/users
"""
