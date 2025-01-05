from flask import Flask
from routes.auth import auth_bp # perform authentication in routes/auth.py, give bp to app.py
from models.user_profile import interaction_bp # Import the user profile blueprint
from models.movie import movie_bp  # Import the new movie blueprint
from models.user_interaction import profile_bp  # Import the new profile blueprint
from models.feedback import feedback_bp  # Import feedback blueprint
from models.prediction import predict_bp  # Prediction blueprint

app = Flask(__name__)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(interaction_bp, url_prefix='/interaction')
app.register_blueprint(movie_bp, url_prefix='/movies')
app.register_blueprint(profile_bp, url_prefix='/profile')
app.register_blueprint(feedback_bp, url_prefix='/feedback')
app.register_blueprint(predict_bp, url_prefix='/api')  # Adding the prediction blueprint

if __name__ == '__main__':
    app.run(debug=True)