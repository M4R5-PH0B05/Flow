from sympy.codegen import Print

from db import db
import hashlib


def Register(Forename, Surname, Email, Password):
    try:
        conn = db()
        forename = Forename.title()
        surname = Surname.title()

        #########################################################
        # DO EMAIL VALIDATION ON FRONTEND, LESS SERVER REQUESTS #
        #########################################################

        password = hashlib.sha1((Password).encode("utf-8")).hexdigest()
        if conn.userDetails(Email) != 0:
            raise Exception("Email already in use")
            return 0
        conn.registerUser(forename,surname,Email,password, permissions = False)
        return 1
    except Exception as e:
        print(f"Exeption was: {e}")
        return 0