from flask import Blueprint, request, jsonify
from firebase_admin import firestore
from firebase import db
from utils.encryption import encrypt_password, check_password

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')

    if not email or not password or not name:
        return jsonify({"error": "All fields are required"}), 400

    # Encrypt the password and store user in Firestore
    encrypted_password = encrypt_password(password)
    user_ref = db.collection('users').document(email)
    if user_ref.get().exists:
        return jsonify({"error": "User already exists"}), 400

    user_ref.set({
        'email': email,
        'password': encrypted_password,
        'name': name,
        'created_at': firestore.SERVER_TIMESTAMP
    })
    return jsonify({"message": "User created successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    user_ref = db.collection('users').document(email)
    user_data = user_ref.get()

    if not user_data.exists:
        return jsonify({"error": "User not found"}), 404

    user = user_data.to_dict()
    if check_password(password, user['password']):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid password"}), 400
