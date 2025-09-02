# IMPORTS
from db import db
import hashlib

# MAIN BODY


def LoginAttept(UserAttempt, PassAttempt):
    try:
        if UserAttempt != None and PassAttempt != None:
            conn = db()
            HashPass = conn.selectPassword(UserAttempt)[0]
            if PassAttempt == HashPass:
                return 1
            return 0
    except Exception as e :
        print(f"Exeption was: {e}. Fix it")
        return 0



# TESTING
LoginAttept("test@test.com",hashlib.sha1(("test").encode("utf-8")).hexdigest())


# Morgans Database Functions
# conn = db()
# conn.userDetails()
# conn.registerUser()
# conn.changePassword()