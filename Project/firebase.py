import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK with your service account file
cred = credentials.Certificate("aialgo-863b3-firebase-adminsdk-ram9z-4e4a52ba7c.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore DB instance
db = firestore.client()
