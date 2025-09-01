# IMPORTS
from db import db
import hashlib

# MAIN BODY

# Create a new login class
class Login:
    # Initialise Login Class
    def __init__(self, id ,username, password):
        self.id = id
        self.username = username
        self.password = hashlib.sha1(password.encode("utf-8")).hexdigest()






# TESTING
login = Login(1, "Test", "Test")

copy = b"Test"
m.update(copy)
print(m.hexdigest())
print("The Hash is: %s" % login.password)




# Morgans Database Functions

# conn = db()
# conn.userDetails()
# conn.registerUser()
# conn.changePassword()