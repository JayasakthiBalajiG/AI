from flask import Blueprint, request, jsonify
from huggingface_hub import hf_hub_download
import joblib
from firebase import db

predictions_table = db.collection("prediction")

# Load the model from Hugging Face
model_path = hf_hub_download(repo_id='bnamazci/gradient-boosting-model2', filename='gradient_boosting_model.joblib')
model = joblib.load(model_path)

# Create the Blueprint
predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/predict', methods=['POST'])

def predict():
    try:
        # Parse request data
        data = request.json
        email = data.get('email')
        inputs = [
            data.get('age'),
            data.get('gender'),
            data.get('Action'),
            data.get('Adventure'),
            data.get('Animation'),
            data.get('Children'),
            data.get('Comedy'),
            data.get('Crime'),
            data.get('Documentary'),
            data.get('Drama'),
            data.get('Fantasy'),
            data.get('Film-Noir'),
            data.get('Horror'),
            data.get('Musical'),
            data.get('Mystery'),
            data.get('Romance'),
            data.get('Sci-Fi'),
            data.get('Thriller'),
            data.get('War'),
            data.get('Western')
        ]

        # Validate inputs
        if not email or any(x is None for x in inputs):
            return jsonify({"error": "Missing required inputs"}), 400

        # Ensure all inputs are numbers
        try:
            inputs = [float(x) if isinstance(x, (int, float)) else float(x) for x in inputs]
            inputs = [int(x) if isinstance(x, float) and x.is_integer() else x for x in inputs]
        except ValueError:
            return jsonify({"error": "All input values must be numeric"}), 400

        # Perform prediction
        prediction = model.predict([inputs])[0]

        # Prepare data for Firestore
        prediction_data = {
            "email": email,
            "inputs": {key: (int(val) if isinstance(val, (int, float)) and isinstance(val, float) and val.is_integer() else float(val))
                       for key, val in zip(['age', 'gender', 'Action', 'Adventure', 'Animation', 'Children', 
                                            'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 
                                            'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 
                                            'War', 'Western'], inputs)},
            "prediction": int(prediction) if isinstance(prediction, (int, float)) and isinstance(prediction, float) and prediction.is_integer() else float(prediction)
        }

        # Save prediction to Firebase
        predictions_table.document(email).set(prediction_data)

        # Return prediction
        return jsonify({"prediction": int(prediction) if isinstance(prediction, (int, float)) and prediction.is_integer() else float(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
