from flask_login import login_user, logout_user, current_user
from models import User

# Mock user store
USERS = {
    "user": User("user", "user"),
    "admin": User("admin", "admin")
}

def authenticate(username):
    user = USERS.get(username)
    if user:
        login_user(user)
        return True
    return False
