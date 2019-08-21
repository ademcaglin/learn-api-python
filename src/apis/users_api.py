from flask import jsonify, Blueprint, request
from repositories import user_repository
users_api = Blueprint('users_api', __name__)


@users_api.route("/api/users")
def get_user():
    name = request.args["name"]
    if name:
        return jsonify(user_repository.get_user(name))
    else:
        return jsonify({"error": "NotFound"})


@users_api.route("/api/users", methods=['POST'])
def add_user():
    content = request.json
    user_repository.insert_user(content["name"], content["age"])
    return ('', 204)