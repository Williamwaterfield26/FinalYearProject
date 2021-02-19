from app import db
#from sqlite3 import model
from flask import Flask, render_template, url_for, redirect
#from forms import SignUpForm, SignInForm, AddCustomerForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, IntegerField, FloatField
from wtforms.validators import DataRequired, InputRequired, Length, Regexp, NumberRange




# class customer(db.Model):
#     __tablename__ = 'customers'
#     customerid = db.Column(db.Integer, primary_key = True)
#     customerfirstname = db.Column(db.String(20))
#     customersurname = db.Column(db.String(20))
#     email = db.Column(db.String)

#     def __init__(self, customerfirstname, customersurname, email):
#         self.customerfirstname = customerfirstname
#         self.customersurname = customersurname
#         self.email = email