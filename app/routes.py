from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from .models import User
from . import db

main = Blueprint('main', __name__)

# API Đăng ký
@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists"}), 400

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# API Đăng nhập
@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username, password=password).first()
    if not user:
        return jsonify({"message": "Invalid username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify({"access_token": access_token}), 200

# API bảo mật
@main.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({"message": "You have accessed a protected route!"}), 200
