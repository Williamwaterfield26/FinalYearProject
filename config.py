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

    # app.config['MAIL_SERVER']='smtp.gmail.com'
    # app.config['MAIL_PORT'] = 465
    # app.config['MAIL_USERNAME'] = 'suitedpython@gmail.com'
    # app.config['MAIL_PASSWORD'] = 'Psuited14'
    #         # app.config['MAIL_USE_TLS'] = False
    #         # app.config['MAIL_USE_SSL'] = True
    # mail = Mail(app)


    # MAIL_SERVER='smtp.googlemail.com'
    # MAIL_PORT=587
    # MAIL_USE_TLS=1
    # MAIL_USERNAME='suitedpython@gmail.com'
    # MAIL_PASSWORD='grkzeqnagvphzvyk'


    # EMAIL_HOST = 'smtp.gmail.com'
    # EMAIL_HOST_USER = 'suitedpython@gmail.com'
    # EMAIL_HOST_PASSWORD = 'grkzeqnagvphzvyk'
    # EMAIL_PORT = 587
    # EMAIL_USE_TLS = True



    # app.config['MAIL_SERVER']='smtp.gmail.com'
    # app.config['MAIL_PORT'] = 465
    # app.config['MAIL_USERNAME'] = 'suitedpython@gmail.com'
    # app.config['MAIL_PASSWORD'] = 'Psuited14'
    # app.config['MAIL_USE_TLS'] = False
    # app.config['MAIL_USE_SSL'] = True




# class Config(object):
# 	# key for CSF
# 	SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(32)
# 	# sqlalchemy .db location (for sqlite)
# 	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#         'sqlite:///' + os.path.join(basedir, 'app.db')
# 	# sqlalchemy track modifications in sqlalchemy
# 	SQLALCHEMY_TRACK_MODIFICATIONS = False
# 	MAIL_SERVER = os.environ.get('MAIL_SERVER')
# 	MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
# 	MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
# 	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
# 	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
# 	ADMINS = ['email@email.com']