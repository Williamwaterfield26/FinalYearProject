import os 
import smtplib
from flask_mail import Mail, Message
from app.__init__ import mail

basedir = os.path.abspath(os.path.dirname(__file__))



class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'DatabaseFYP.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('587')or 25)
    MAIL_USE_TLS = os.environ.get('1') is not None
    MAIL_USERNAME = os.environ.get('suitedpython@gmail.com')
    MAIL_PASSWORD = os.environ.get('grkzeqnagvphzvyk')
    ADMINS = ('willwater2699@gmail.com')








