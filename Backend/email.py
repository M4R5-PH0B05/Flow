import smtplib as smtp
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#MAIN BODY

sender_email = "thomaswaddington1@gmail.com"
password = "egfp wjfa qqqk ifrl"


class emailWrapper:

    # Sends email to specific address, uses hard coded company password.
    @staticmethod
    def send_email(reciver, subject, body):
        message = MIMEMultipart()
        message["From"] = sender
        message["To"] = reciver
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        with smtp.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, reciver, message.as_string())
        print("Email sent")

    @staticmethod
    def send_bulk(reciver_list, subject, body):
        for reciver in reciver_list:
            send_email(reciver, subject, body)

