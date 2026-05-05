<<<<<<< HEAD
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def verify_password(password, password_hash):
=======
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def verify_password(password, password_hash):
>>>>>>> f4a19c10a8f96dd3a8eccafa90551107535f6458
    return hash_password(password) == password_hash