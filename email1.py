from flask_mail import Message, Mail
from flask import current_app
from __init__ import app
from config import Config


def send_email(subject,sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)



def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Suited] Reset Your Password',
        sender=app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('reset_password.txt', user=user,token=token),
        html_body=render_template('reset_password.html',user=user, token=token))

