import smtplib, ssl
from email.mime.text import MIMEText
from account import gmail

class Email:
    def __init__(self, mail_from):
        self.mail_from = mail_from

    def send_email(self, to, body, title):
        message = self.make_mime(to, body, title)
        smtp_serv = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context())
        smtp_serv.login(gmail.address, gmail.app_password)
        smtp_serv.send_message(message)

    def make_mime(self, to, body, title):    
        message = MIMEText(body, 'html')
        message['Subject'] = title
        message['To'] = to
        message['From'] = gmail.address
        return message
    
if __name__ == '__main__':
    email = Email(gmail.address)
    email.send_email(gmail.address, "test_body", "test_title")