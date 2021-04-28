from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, BooleanField, validators
from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, SubmitField, HiddenField, IntegerField, FloatField, SelectField, Form
from wtforms.validators import DataRequired, InputRequired, Length, Regexp, NumberRange, Email, EqualTo
from wtforms.fields.html5 import EmailField
#from app import db



class AddCustomerForm(FlaskForm):
    customerid = HiddenField()
    customerfirstname = StringField('Customer Firstname',[InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Firstname"),
    ])
    customersurname = StringField('Customer Surname',[InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Surname"),
    ])
    email = EmailField('Email',[InputRequired(),
    ])
    submit = SubmitField ('Add')


class AddSoldItemForm(FlaskForm):
    solditemid = HiddenField()
    customerfirstname = StringField('Customer Firstname',[InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Firstname"),
    ])
    customersurname = StringField('Customer Surname',[InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Surname"),
    ])
    email = EmailField('Email',[InputRequired(),
    ])
    stockid = SelectField('stockid', choices=[])
    price = FloatField('Price', [InputRequired(),
    NumberRange(min=1.00, message= "Invalid Price Range. Please enter a price of at least £1"),
    ])
    supplierid = SelectField('supplierid', choices=[])
    suppliername = StringField('Supplier Name', [InputRequired(),
    ])
    submit = SubmitField('Add Sold Item')

class DeleteSoldItemForm(FlaskForm):
    customerfirstname =StringField('Customer Firstname')
    customersurname = StringField('Customer Surname')
    email = EmailField('Email')
    stockid = SelectField('stockid', choices=[])
    price = IntegerField('Price')
    supplierid = SelectField('supplierid', choices=[])
    suppliername = StringField('Supplier Name')
    delete = SubmitField('Delete')




class SoldItemSearchForm(FlaskForm):
    choices = [('customersurname','customersurname')]
    select = SelectField ('Search for a customer', choices=choices)
    search = StringField('')

class ComplieMoniesDueForm(FlaskForm):
    choices = [('supplierid','supplierid')]
    select = SelectField ('Search for the Money Owed to a supplier, type in a supplier ID( YOU MUST TYPE IN A FULL ID e.g. <supplier 22>)', choices=choices)
    search = StringField('')


class EditSoldItemForm(FlaskForm):
    solditemid = HiddenField()
    customerfirstname = StringField('Customer Firstname',[InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Firstname"),
    ])
    customersurname = StringField('Customer Surname',[InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Surname"),
    ])
    email = EmailField('Email',[InputRequired(),
    ])
    stockid = SelectField('stockid', choices=[])
    price = FloatField('Price', [InputRequired(),
    NumberRange(min=1.00, message= "Invalid Price Range. Please enter a price of at least £1"),
    ])
    supplierid = SelectField('supplierid', choices=[])
    suppliername = StringField('Supplier Name', [InputRequired(),
    ])
    update =SubmitField('Update')


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
    material = StringField('Material', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Material"),
    ])
    supplierid = SelectField('supplierid', choices=[])
    submit = SubmitField('Add Stock')
    



class AddSupplierForm(FlaskForm):
    supplierid = HiddenField()
    suppliername = StringField('Supplier Name', [InputRequired(),
    ])
    submit = SubmitField('Add Supplier')



class AddListingForm(FlaskForm):
    listingid = HiddenField()
    stockid = SelectField('stockid', choices=[])
    price = FloatField('Price', [InputRequired(),
    NumberRange(min=1.00, message= "Invalid Price Range. Please enter a price of at least £1"),
    ])
    submit = SubmitField('Add Listing')



class CustomerSearchForm(FlaskForm):
    choices = [('customersurname','customersurname')]
    select = SelectField ('Search for a customer', choices=choices)
    search = StringField('')


class EditCustomerForm(FlaskForm):
    customerfirstname = StringField('Customer Firstname',[InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Firstname"),
    ])
    customersurname = StringField('Customer Surname',[InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Surname"),
    ])
    email = EmailField('Email',[InputRequired(),
    ])
    update = SubmitField('Update')




class DeleteCustomerForm(FlaskForm):
    customerfirstname =StringField('Customer Firstname')
    customersurname =StringField('Customer Surname')
    email =EmailField('Email')
    delete = SubmitField('Delete')


class EditSupplierForm(FlaskForm):
    suppliername = StringField('Supplier Name', [InputRequired(),
    ])
    update = SubmitField('Update')


class DeleteSupplierForm(FlaskForm):
    suppliername= StringField('Supplier Name')
    delete = SubmitField('Delete')

class SupplierSearchForm(FlaskForm):
    choices = [('suppliername', 'suppliername')]
    select = SelectField('Search for a supplier', choices=choices)
    search = StringField('')




class EditListingForm(FlaskForm):
    stockid = SelectField('stockid', choices=[])
    price = FloatField('Price', [InputRequired(),
    NumberRange(min=1.00, max=4000, message= "Invalid Price Range. Please enter a price of at least £1"),
    ])
    update = SubmitField('Update')
    cancel = SubmitField('Cancel')


class DeleteListingForm(FlaskForm):
    stockid = SelectField('stockid', choices=[])
    price= IntegerField('Price')
    delete = SubmitField('Delete')

class ListingSearchForm(FlaskForm):
    choices = [('stockid', 'stockid')]
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
    material = StringField('Material', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Material"),
    ])
    supplierid = SelectField('supplierid', choices=[])
    update = SubmitField('Update')


class StockSearchForm(FlaskForm):
    choices = [('stockid', 'stockid')]
    select = SelectField('Search for a stock item', choices=choices)
    search = StringField('')

class DeleteStockForm(FlaskForm):
    size= StringField('size')
    type= StringField('type')
    colour = StringField('colour')
    brand = StringField('brand')
    price = IntegerField('price')
    material = StringField('material')
    supplierid = SelectField('supplierid', choices=[])
    delete = SubmitField('Delete')



class UserSearchForm(FlaskForm):
    choices = [('username','username')]
    select = SelectField('Search for an User', choices=choices)
    search = StringField('')

class EditUserForm(FlaskForm):
    username = StringField('Username', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Username"),
    Length(min=1,max=10, message="Too many characters for your username")
    ])
    email = StringField('Email',[InputRequired(),
    ])
    update = SubmitField('Update')

class DeleteUserForm(FlaskForm):
    username = StringField('Username')
    email = EmailField('Email')
    delete = SubmitField('Delete')

class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Username"),
    Length(min=1,max=10, message="Too many characters for your username")
    ])
    password = PasswordField("password", validators=[DataRequired(),
    Length(min=1,max=10, message="Too many characters for your password")
    ])
    remember_me = BooleanField()
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(),
    Length(min=1,max=10, message="Too many characters for your username"),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Username"),
    ])
    password = PasswordField("password", validators=[DataRequired(),
    Length(min=1,max=10, message="Too many characters for your password")
    ])
    email = EmailField("email", validators=[DataRequired(), Email()])
    submit = SubmitField('Register')

class AddUserForm(FlaskForm):
    id = HiddenField()
    username = StringField('Username', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Username"),
    Length(min=1,max=10, message="Too many characters for your username")
    ])
    password = StringField('Password', [InputRequired(),
    Length(min=1,max=10, message="Too many characters for your password")
    ])
    email = EmailField('Email',[InputRequired(),
    ])
    submit = SubmitField('Register')


class ResetPasswordRequestForm(FlaskForm):
    email = EmailField('Email',validators = [DataRequired(), Email()])
    submit = SubmitField ('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    # password = PasswordField('New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    # confirm  = PasswordField('Repeat Password')


    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')


        # password = PasswordField('Password', validators=[DataRequired(),EqualTo('password2',
        #     message="Passwords must match")])


# ##reset monday
# class ForgotForm(FlaskForm):
#     email = StringField('Email',validators = [DataRequired(), Email()])
#     # email = StringField('Email',
#     # validators.DataRequired(), validators.Email()]
#     # )

class PasswordResetForm(FlaskForm):
    current_password = PasswordField('Current Password', [validators.DataRequired()]
    )

class ForgotForm(FlaskForm):
    email = EmailField('Email', [validators.DataRequired(), validators.Email()]
    )
    