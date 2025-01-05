# app.py
from flask import Flask
from firebase_admin import firestore
from utils.encryption import encrypt_password, check_password
from firebase import db  # Import Firestore instance

def create_user(email, password, name):
    """Create a new user in Firestore with encrypted password."""
    # Encrypt the password
    encrypted_password = encrypt_password(password)
    
    # Add user to Firestore
    user_ref = db.collection('users').document(email)
    user_ref.set({
        'email': email,
        'password': encrypted_password,
        'name': name,
        'preferences': [],
        'created_at': firestore.SERVER_TIMESTAMP
    })
    
    return {"message": "User created successfully!"}

def verify_user(email, password):
    """Verify if the user's password matches."""
    # Fetch user data from Firestore
    user_ref = db.collection('users').document(email)
    user_data = user_ref.get()
    
    if user_data.exists:
        user = user_data.to_dict()
        if check_password(password, user['password']):
            return {"message": "Login successful!"}
        else:
            return {"message": "Invalid password!"}
    else:
        return {"message": "User not found!"}

# Initialize Flask app
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
