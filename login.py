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

    def LoginAttept():
        try:
            UserAttempt = str(input("Enter your Email:   "))
            PassAttempt = hashlib.sha1(input("Enter your Password:   ").encode("utf-8")).hexdigest()
            if UserAttempt != None and PassAttempt != None:
                conn = db()
                HashPass = conn.selectPassword(UserAttempt)[0]
                if PassAttempt == HashPass:
                    print("Login Succeeded")
                else:
                    print("Login Failed")


        except Exception as e :
            print(f"Exeption was: {e}. Fix it")



# TESTING
Login.LoginAttept()




# Morgans Database Functions

# conn = db()
# conn.userDetails()
# conn.registerUser()
# conn.changePassword()