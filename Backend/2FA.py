#IMPORTS
from email import emailWrapper
import random

TwoFactorAuthenticationTemplate = {
    "subject": "Two Factor Authentication",
    "body":
        f"""
            Two Factor Authentication


            Hi, this is your Two Factor Authentication Code:
                            {{nums}}
        """
}

#MAIN BODY
def generateNums():
    nums = []
    for i in range(6):
        nums.append(random.randint(0,9))
    return nums



def send_2FA(reciver):
    nums = generateNums()
    emailWrapper.send_email(reciver, TwoFactorAuthenticationTemplate["subject"], TwoFactorAuthenticationTemplate["body"])



#TESTING
send_2FA("tomski2007@icloud.com")