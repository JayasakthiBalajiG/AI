from flask import Blueprint, jsonify
from firebase import db

movie_bp = Blueprint('movie', __name__)

@movie_bp.route('/get_movies', methods=['GET'])
def get_movies():
    """Retrieve all documents and their data from the movie collection."""
    try:
        # Reference the movie collection
        movies_ref = db.collection('movie')
        
        # Fetch all documents
        docs = movies_ref.stream()
        
        # Extract data from documents
        movies = {doc.id: doc.to_dict() for doc in docs}

        return jsonify({"movies": movies}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
