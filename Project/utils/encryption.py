import bcrypt

def encrypt_password(password):
    """Encrypt the user's password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def check_password(password, hashed_password):
    """Check if the provided password matches the stored hashed password."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
