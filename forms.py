from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, BooleanField
from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, SubmitField, HiddenField, IntegerField, FloatField, SelectField, Form
from wtforms.validators import DataRequired, InputRequired, Length, Regexp, NumberRange, Email

#from app import db

class SignUpForm(FlaskForm):
    ausername = StringField('Username')
    apassword = PasswordField('Password')
    email = StringField('Email')
    submit = SubmitField('Sign Up')
    
#    def __init__(self, username, password, email, submit):
#        self.username = username
#        self.password = password
#        self.email = email
#        self.submit = submit


class SignInForm(FlaskForm):
    ausername = StringField('Username')
    apassword = PasswordField('Password')
    submit = SubmitField('Sign In')

#    def __init__ (self, username, password, submit):
#        self.username = username
#        self.password = password
#        self.submit = submit

class AddCustomerForm(FlaskForm):
    customerid = HiddenField()
    customerfirstname = StringField('Customer Firstname',[InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Firstname"),
    Length(max=20, message="Too long Firstname")
    ])
    customersurname = StringField('Customer Surname',[InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Surname"),
    Length(max=20, message="Too long Surname")
    ])
    email = StringField('Email',[InputRequired(),
    #Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Email"),
    ])
    submit = SubmitField ('Add Customer')


class AddSoldItemForm(FlaskForm):
    solditemid = HiddenField()
    customerfirstname = StringField('Customer Firstname',[InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Firstname"),
    Length(max=20, message="Too long Firstname")
    ])
    customersurname = StringField('Customer Surname',[InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Surname"),
    Length(max=20, message="Too long Surname")
    ])
    email = StringField('Email',[InputRequired(),
    #Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Email"),
    ])
    stockid = IntegerField('Stock ID', [InputRequired(),
    NumberRange(min=1.00, max=4000, message= "Invalid Stock ID")
    ])
    price = FloatField('Price', [InputRequired(),
    NumberRange(min=1.00, message= "Invalid Price Range. Please enter a price of at least £1"),
    ])
    supplierid = IntegerField('Supplier ID', [InputRequired(),
    NumberRange(min=1.00, max=4000, message= "Invalid Supplier ID")
    ])
    suppliername = StringField('Supplier Name', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Supplier Name"),
    ])
    submit = SubmitField('Add Sold Item')

class DeleteSoldItemForm(FlaskForm):
    customerfirstname =('Customer Firstname')
    customersurname = ('Customer Surname')
    email = ('Email')
    price = ('Price')
    supplierid = ('Supplier ID')
    suppliername = ('Supplier Name')
    delete = ('Delete')


class SoldItemSearchForm(FlaskForm):
    choices = [('customersurname','customersurname')]
    select = SelectField ('Search for a customer', choices=choices)
    search = StringField('')

class EditSoldItemForm(FlaskForm):
    solditem = HiddenField()
    customerfirstname = StringField('Customer Firstname',[InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Firstname"),
    Length(max=20, message="Too long Firstname")
    ])
    customersurname = StringField('Customer Surname',[InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Surname"),
    Length(max=20, message="Too long Surname")
    ])
    email = StringField('Email',[InputRequired(),
    #Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Email"),
    ])
    price = FloatField('Price', [InputRequired(),
    NumberRange(min=1.00, message= "Invalid Price Range. Please enter a price of at least £1"),
    ])
    supplierid = IntegerField('Supplier ID', [InputRequired(),
    NumberRange(min=1.00, max=4000, message= "Invalid Supplier ID")
    ])
    suppliername = StringField('Supplier Name', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Supplier Name"),
    ])
    update =SubmitField('Update')
    cancel =SubmitField('Cancel')


class AddStockForm(FlaskForm):
    stockid = HiddenField()
    size = StringField('Size', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Size"),
    Length(min=0,max=3, message="Too many characters for Size")
    ])
    type = StringField('Type', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Type of clothing"),
    ])
    colour = StringField('Colour', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Colour"),
    ])
    brand = StringField('Brand', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Brand"),
    ])
    price = FloatField('Price', [InputRequired(),
    NumberRange(min=1.00, message= "Invalid Price Range. Please enter a price of at least £1"),
    ])
    supplierid = IntegerField('Supplier ID', [InputRequired(),
    NumberRange(min=1.00, max=4000, message= "Invalid Supplier ID")
    ])
    material = StringField('Material', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Material"),
    ])
    submit = SubmitField('Add Stock')
    

class AddSupplierForm(FlaskForm):
    supplierid = HiddenField()
    suppliername = StringField('Supplier Name', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Supplier Name"),
    ])
    submit = SubmitField('Add Supplier')

class AddListingForm(FlaskForm):
    listingid = HiddenField()
    supplierid = IntegerField('Supplier ID', [InputRequired(),
    NumberRange(min=1.00, max=4000, message= "Invalid Supplier ID")
    ])
    price = FloatField('Price', [InputRequired(),
    NumberRange(min=1.00, max=4000, message= "Invalid Price Range. Please enter a price of at least £1"),
    ])
    submit = SubmitField('Add Listing')






class AddAdminForm(FlaskForm):
    id = HiddenField()
    ausername = StringField('Username', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Username"),
    ])
    apassword = StringField('Password', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Password"),
    ])
    email = StringField('Email',[InputRequired(),
    #Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Email"),
    ])
    submit = SubmitField('Sign Up')
    

#class CustomerSearchForm(Form):
    # choices = [('customerid', 'customerid'), ('customerfirstname'), ('customersurname', 'customersurname'), ('email','email')]
    # select = SelectField ('Search for a customer', choices=choices)
    # search = StringField('')
class CustomerSearchForm(FlaskForm):
    choices = [('customersurname','customersurname')]
    select = SelectField ('Search for a customer', choices=choices)
    search = StringField('')


class EditCustomerForm(FlaskForm):
    customerfirstname = StringField('Customer Firstname',[InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Firstname"),
    Length(max=20, message="Too long Firstname")
    ])
    customersurname = StringField('Customer Surname',[InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Surname"),
    Length(max=20, message="Too long Surname")
    ])
    email = StringField('Email',[InputRequired(),
    #Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Email"),
    ])
    update = SubmitField('Update')
    cancel = SubmitField('Cancel')


class DeleteCustomerForm(FlaskForm):
    customerfirstname =('Customer Firstname')
    customersurname =('Customer Surname')
    email =('Email')
    delete = SubmitField('Delete')


class EditSupplierForm(FlaskForm):
    suppliername = StringField('Supplier Name', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Supplier Name"),
    ])
    update = SubmitField('Update')
    cancel = SubmitField('Cancel')

class DeleteSupplierForm(FlaskForm):
    suppliername= ('Supplier Name')
    delete = SubmitField('Delete')

class SupplierSearchForm(FlaskForm):
    choices = [('suppliername', 'suppliername')]
    select = SelectField('Search for a supplier', choices=choices)
    search = StringField('')


class EditListingForm(FlaskForm):
    supplierid = IntegerField('Supplier ID', [InputRequired(),
    NumberRange(min=1.00, max=4000, message= "Invalid Supplier ID")
    ])
    price = FloatField('Price', [InputRequired(),
    NumberRange(min=1.00, max=4000, message= "Invalid Price Range. Please enter a price of at least £1"),
    ])
    update = SubmitField('Update')
    cancel = SubmitField('Cancel')

class DeleteLitingForm(FlaskForm):
    supplierid= ('Supplier ID')
    price= ('Price')
    delete = SubmitField('Delete')

class ListingSearchForm(FlaskForm):
    choices = [('supplierid', 'supplierid')]
    select = SelectField ('Search for a listing', choices=choices)
    search = StringField('')

class EditStockForm(FlaskForm):
    size = StringField('Size', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Size"),
    Length(min=0,max=3, message="Too many characters for Size")
    ])
    type = StringField('Type', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Type of clothing"),
    ])
    colour = StringField('Colour', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Colour"),
    ])
    brand = StringField('Brand', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Brand"),
    ])
    price = FloatField('Price', [InputRequired(),
    NumberRange(min=1.00, message= "Invalid Price Range. Please enter a price of at least £1"),
    ])
    supplierid = IntegerField('Supplier ID', [InputRequired(),
    NumberRange(min=1.00, max=4000, message= "Invalid Supplier ID")
    ])
    material = StringField('Material', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Material"),
    ])
    update = SubmitField('Update')
    cancel = SubmitField('Cancel')

class StockSearchForm(FlaskForm):
    choices = [('stockid', 'stockid')]
    select = SelectField('Search for a stock item', choices=choices)
    search = StringField('')

class DeleteStockForm(FlaskForm):
    size= ('size')
    type= ('type')
    colour = ('colour')
    brand = ('brand')
    price = ('price')
    supplierid =('supplierid')
    material = ('material')
    delete = SubmitField('Delete')



class AdminSearchForm(FlaskForm):
    choices = [('ausername','ausername')]
    select = SelectField('Search for an Admin', choices=choices)
    search = StringField('')

class EditAdminForm(FlaskForm):
    ausername = StringField('Username', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Username"),
    ])
    apassword = StringField('Password', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Password"),
    ])
    email = StringField('Email',[InputRequired(),
    #Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Email"),
    ])
    update = SubmitField('Update')

class DeleteAdminForm(FlaskForm):
    ausername = ('Username')
    apassword = ('Password')
    email = ('Email')
    delete = SubmitField('Delete')

class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField()
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired(), Email()])
    submit = SubmitField('Register')

class AddUserForm(FlaskForm):
    id = HiddenField()
    username = StringField('Username', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Username"),
    ])
    password = StringField('Password', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Password"),
    ])
    email = StringField('Email',[InputRequired(),
    #Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Email"),
    ])
    submit = SubmitField('Register')
