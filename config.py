import os 

class Config(object):
    MAIL_SERVER = os.environ.get('smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('587') or 25)
    MAIL_USE_TLS = os.environ.get('1') is not None
    MAIL_USERNAME = os.environ.get('username')
    MAIL_PASSWORD = os.environ.get('password')
    ADMINS = ['willwater2699@gmail.com']



    # set MAIL_SERVER=smtp.googlemail.com
    # set MAIL_PORT=587
    # set MAIL_USE_TLS=1
    # set MAIL_USERNAME='suitedpython@gmail.com'
    # set MAIL_PASSWORD='Psuited14'