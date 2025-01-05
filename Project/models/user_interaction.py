from flask import Blueprint, jsonify, request
from firebase import db

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/get_user_profile', methods=['GET'])
def get_user_profile():
    """Retrieve data for a specific user from the user_profile collection."""
    email = request.args.get('email')

    if not email:
        return jsonify({"error": "Email is required"}), 400

    try:
        # Reference the user_profile collection
        user_ref = db.collection('user_profile').document(email)
        
        # Fetch the document
        user_data = user_ref.get()
        
        if user_data.exists:
            return jsonify({"user_profile": user_data.to_dict()}), 200
        else:
            return jsonify({"error": "User profile not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
