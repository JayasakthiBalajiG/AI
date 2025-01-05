from flask import Blueprint, request, jsonify
from firebase_admin import firestore
from firebase import db

interaction_bp = Blueprint('interaction', __name__)

@interaction_bp.route('/add_interaction', methods=['POST'])
def add_interaction():
    data = request.json
    email = data.get('email')
    genres = [
        'Action', 'Adventure', 'Animation', 'Children', 'Comedy', 
        'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 
        'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 
        'Thriller', 'War', 'Western'
    ]

    # Check if email is provided
    if not email:
        return jsonify({"error": "Email is required"}), 400

    # Check if all required genre fields are present
    missing_fields = [genre for genre in genres if genre not in data]
    if missing_fields:
        return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

    # Validate all genre values (should be 0 or 1)
    invalid_values = {key: value for key, value in data.items() if key in genres and value not in [0, 1]}
    if invalid_values:
        return jsonify({"error": f"Invalid values: {invalid_values}. Allowed values are 0 or 1"}), 400

    # Prepare the data for Firestore
    interaction_data = {genre: data[genre] for genre in genres}
    interaction_data['email'] = email

    # Add data to Firestore
    interaction_ref = db.collection('user_interaction').document(email)
    interaction_ref.set(interaction_data, merge=True)  # Merge ensures existing data isn't overwritten

    return jsonify({"message": "User interaction added successfully!"}), 201
