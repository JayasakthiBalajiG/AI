from flask import Blueprint, request, jsonify
from firebase import db

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    """Save feedback with rating, email, and title in the feedback collection."""
    data = request.json
    email = data.get('email')
    title = data.get('title')
    rating = data.get('rating')

    if not email or not title or rating is None:
        return jsonify({"error": "Email, title, and rating are required"}), 400

    if not (1 <= rating <= 5):
        return jsonify({"error": "Rating must be between 1 and 5"}), 400

    try:
        # Reference to the feedback collection
        feedback_ref = db.collection('feedback').document(email)
        
        # Save feedback directly in the document
        feedback_ref.set({
            'email': email,
            'title': title,
            'rating': rating
        })
        
        return jsonify({"message": "Feedback submitted successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
