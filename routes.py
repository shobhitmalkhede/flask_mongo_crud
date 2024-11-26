from flask import Blueprint, request, jsonify
from app import mongo
from bson import ObjectId
import bcrypt

user_bp = Blueprint('users', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    return jsonify([{"id": str(user["_id"]), "name": user["name"], "email": user["email"]} for user in users]), 200

@user_bp.route('/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one({"_id": ObjectId(id)})
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"id": str(user["_id"]), "name": user["name"], "email": user["email"]}), 200

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    hashed_password = bcrypt.hashpw(data["password"].encode('utf-8'), bcrypt.gensalt())
    user = {"name": data["name"], "email": data["email"], "password": hashed_password}
    result = mongo.db.users.insert_one(user)
    return jsonify({"id": str(result.inserted_id)}), 201

@user_bp.route('/<id>', methods=['PUT'])
def update_user(id):
    data = request.json
    updated_user = {key: value for key, value in data.items() if key in ["name", "email", "password"]}
    if "password" in updated_user:
        updated_user["password"] = bcrypt.hashpw(data["password"].encode('utf-8'), bcrypt.gensalt())
    mongo.db.users.update_one({"_id": ObjectId(id)}, {"$set": updated_user})
    return jsonify({"message": "User updated"}), 200

@user_bp.route('/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "User deleted"}), 200
