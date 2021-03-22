from flask import Flask, render_template, url_for, redirect, request, flash, Blueprint
from forms import SignUpForm, SignInForm, AddCustomerForm, AddStockForm, AddSupplierForm, AddListingForm, AddUserForm, CustomerSearchForm, EditCustomerForm, DeleteCustomerForm, SupplierSearchForm, EditSupplierForm, DeleteSupplierForm, ListingSearchForm, EditListingForm, DeleteListingForm, StockSearchForm, EditStockForm, DeleteStockForm, AddSoldItemForm, DeleteSoldItemForm, EditSoldItemForm, SoldItemSearchForm, UserSearchForm, EditUserForm, DeleteUserForm, RegisterForm, LoginForm, ComplieMoniesDueForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_login import UserMixin, LoginManager
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, SubmitField, HiddenField, IntegerField, FloatField
from wtforms.validators import DataRequired, InputRequired, Length, Regexp, NumberRange
from flask_table import Table, Col, LinkCol
from django import forms
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from tables import CustomerResults, SupplierResults, ListingResults, StockResults, SoldItemResults, UserResults, MoniesDueResults
from werkzeug.security import generate_password_hash, check_password_hash
#from models import customer
from flask_login import login_user, login_required, logout_user
import pandas as pd
from django.db.models import Sum
from sqlalchemy.sql import func





app= Flask (__name__)
app.config ['SECRET_KEY'] = 'bob'
Bootstrap(app)
db_name = 'DatabaseFYP.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
login_manager=LoginManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)





@app.route('/preregistereduser')
def preregistereduser():
        return render_template('preregistereduser.html')


@app.route('/invaliddetails')
def invaliddetails():
        return render_template('invaliddetails.html')

@app.route('/registered')
def registered():
        return render_template('registered.html')



@app.route('/loggedin')
@login_required
def loggedin():
        return render_template('loggedin.html')


@app.route('/supplierpage', methods = ['GET', 'POST'])
@login_required
def supplierpage():
        search = SupplierSearchForm(request.form)
        if request.method == 'POST':
                return searchsupplierresults(search)
        return render_template('supplierpage.html',form=search)
        


@app.route('/customerpage', methods = ['GET', 'POST'])
@login_required
def customerpage():
        #form = CustomerSearchForm()
        search = CustomerSearchForm(request.form)
        if request.method == 'POST':
                return searchcustomerresults(search)

        #return render_template('customerpage.html', search=search, form=form)
        return render_template('customerpage.html', form=search)







@app.route('/allcustomer')
@login_required
def allcustomer():
        results=[]
        qry = db.session.query(customer)
        results = qry.all()
        table=CustomerResults(results)
        table.border =True
        return render_template('allcustomer.html', table=table)

#works for customersurname
@app.route('/customerresults')
@login_required
def searchcustomerresults(search):
        results = []
        search_string = search.data['search']
        if search_string:
                if search.data ['select'] == 'customersurname':
                        qry = db.session.query(customer).filter(customer.customersurname.contains(search_string))
                        results = qry.all()
                else:
                        qry = db.session.query(customer)
                        results = qry.all()
        if not results:
                flash('No results found, please try again')
                return redirect ('/customerpage')
        else:
                table = CustomerResults(results)
                table.border = True
                return render_template('results.html', table=table)





#@app.route('/editcustomer',methods=['GET', 'POST'])
@app.route('/editcustomer/<int:customerid>', methods=['GET', 'POST'])
@login_required
#@app.route('/editcustomer/<customerid>',methods=['GET', 'POST'])
def editcustomer(customerid):
        qry = db.session.query(customer).filter( customer.customerid == customerid)
        customersurname = qry.first()
        if customersurname:
                form = EditCustomerForm(formdata=request.form, obj = customersurname)
                if request.method == 'POST' and form.validate():
                        save_customer(customersurname,form)

                        flash ('Customer updated!')
                        return redirect ('/customerpage')
                return render_template('customerpage.html', form=form)
        else:
                return 'Error loading the customer'.format(customerid=customerid)
#</int:customerid>


def save_customer(customersurname, form, new=False):
        customersurname.customerfirstname = form.customerfirstname.data
        customersurname.customersurname = form.customersurname.data
        customersurname.email = form.email.data

        if new:
                db.session.add(customersurname)
        db.session.commit()




@app.route('/results')
@login_required
def results():
        return render_template('results.html')






@app.route('/listingpage',methods = ['GET', 'POST'])
@login_required
def listingpage():
        search = ListingSearchForm(request.form)
        if request.method == 'POST':
                return searchlistingresults(search)
        return render_template('listingpage.html', form=search)
        



@app.route('/stockpage', methods = ['GET', 'POST'])
@login_required
def stockpage():
        search = StockSearchForm(request.form)
        if request.method == 'POST':
                return searchstockresults(search)
        return render_template('stockpage.html', form=search)


@app.route('/solditempage', methods = ['GET', 'POST'])
@login_required
def solditempage():
        search = SoldItemSearchForm(request.form)
        if request.method == 'POST':
                return searchsolditemresults(search)
        return render_template('solditempage.html', form=search)

@app.route('/compilemonies', methods = ['GET', 'POST'])
@login_required
def compilemonies():
        search = ComplieMoniesDueForm(request.form)
        if request.method == 'POST':
                return searchcompilemonies(search)
        return render_template('compilemonies.html', form=search)


        
        
class supplier(db.Model):
        __tablename__ = 'supplier'
        supplierid = db.Column(db.Integer, primary_key = True)
        suppliername = db.Column(db.String)


        def __init__(self, suppliername):
                self.suppliername = suppliername
    


@app.route('/addsupplier', methods=['GET', 'POST'])
@login_required
def addsupplier():
        form = AddSupplierForm()
        if form.validate_on_submit():
                suppliername = request.form['suppliername']
                
                record = supplier(suppliername)
                db.session.add(record)
                db.session.commit()
                message = f"The Supplier has been submitted"
                return redirect(url_for('supplierpage'))
        else:
                #show validation
                for field, errors in form.errors.items():
                        for error in errors:
                                flash("Error in {}: {}".format(
                                        getattr(form, field).label.text,
                                        error
                                ), 'error')
                return render_template('addsupplier.html', form=form)





@app.route('/deletesupplier/<int:supplierid>', methods=['GET', 'POST'])
@login_required
def deletesupplier(supplierid):
        qry = db.session.query(supplier).filter(supplier.supplierid==supplierid)
        suppliername = qry.first()
        if suppliername:
                form = DeleteSupplierForm(formdata=request.form, obj=suppliername)
                if request.method == 'POST' and form.validate():
                        db.session.delete(suppliername)
                        db.session.commit()
                        flash('Supplier deleted successfully!')
                        return redirect('/supplierpage')
                return render_template('deletesupplier.html', form=form)
        else:
                return 'Error deleting supplier'.format(supplierid=supplierid)


@app.route('/allsupplier')
@login_required
def allsupplier():
        results=[]
        qry = db.session.query(supplier)
        results = qry.all()
        table=SupplierResults(results)
        table.border =True
        return render_template('allsupplier.html', table=table)




@app.route('/editsupplier/<int:supplierid>',methods= ['GET','POST'])
@login_required
def editsupplier(supplierid):
        qry = db.session.query(supplier).filter(supplier.supplierid== supplierid)
        suppliername = qry.first()
        if suppliername:
                form = EditSupplierForm(formdata=request.form, obj=suppliername)
                if request.method == 'POST' and form.validate():
                        save_supplier(suppliername, form)

                        flash('Supplier Updated!')
                        return redirect ('/supplierpage')
                return render_template('supplierpage.html', form=form)
        else:
                return 'Error loading supplier'.format(supplierid=supplierid)

def save_supplier(suppliername, form, new=False):
        suppliername.suppliername = form.suppliername.data

        if new:
                db.session.add(suppliername)
        db.session.commit()


#works for suppliername
@app.route('/supplierresults')
@login_required
def searchsupplierresults(search):
        results = []
        search_string = search.data['search']
        if search_string:
                if search.data ['select'] == 'suppliername':
                        qry = db.session.query(supplier).filter(supplier.suppliername.contains(search_string))
                        results = qry.all()
                else:
                        qry = db.session.query(supplier)
                        results = qry.all()
        if not results:
                flash('No results found, please try again')
                return redirect ('/supplierpage')
        else:
                table = SupplierResults(results)
                table.border = True
                return render_template('results.html', table=table)



class customer(db.Model):
    __tablename__ = 'customers'
    customerid = db.Column(db.Integer, primary_key = True)
    customerfirstname = db.Column(db.String(20))
    customersurname = db.Column(db.String(20))
    email = db.Column(db.String)

    def __init__(self, customerfirstname, customersurname, email):
        self.customerfirstname = customerfirstname
        self.customersurname = customersurname
        self.email = email
    





@app.route('/addcustomer', methods=['GET', 'POST'])
@login_required
def addcustomer():
        form = AddCustomerForm()
        if form.validate_on_submit():
                customerfirstname = request.form['customerfirstname']
                customersurname = request.form['customersurname']
                email = request.form['email']

                
                record = customer(customerfirstname,customersurname,email)
                db.session.add(record)
                db.session.commit()
                message = f"The Customer has been submitted"
                return redirect(url_for('customerpage'))

        else:
                #show validation
                for field, errors in form.errors.items():
                        for error in errors:
                                flash("Error in {}: {}".format(
                                        getattr(form, field).label.text,
                                        error
                                ), 'error')
                return render_template('addcustomer.html', form=form)





# Delete customer from database which matches the ID
@app.route('/deletecustomer/<int:customerid>', methods=['GET', 'POST'])
@login_required
def deletecustomer(customerid):
        qry = db.session.query(customer).filter( customer.customerid == customerid)
        customersurname = qry.first()
        if customersurname:
                form = DeleteCustomerForm(formdata=request.form, obj=customersurname)
                if request.method == 'POST' and form.validate():
                        db.session.delete(customersurname)
                        db.session.commit()
                        flash('Customer deleted successfully!')
                        return redirect('/customerpage')
                return render_template('customerpage.html', form=form)
        else:
                return 'Error deleting customer'.format(customerid=customerid)





class stock(db.Model):
    __tablename__ = 'stock'
    stockid = db.Column(db.Integer, primary_key = True)
    size = db.Column(db.String(3))
    type = db.Column(db.String)
    colour = db.Column(db.String)
    brand = db.Column(db.String)
    price = db.Column(db.Float)
    supplierid = db.Column(db.Integer)
    material = db.Column(db.String)



    def __init__(self,size,type,colour,brand,price,supplierid,material):
        self.size = size
        self.type = type
        self.colour = colour
        self.brand = brand
        self.price = price
        self.supplierid = supplierid
        self.material = material


                




@app.route('/addstock', methods=['GET', 'POST'])
@login_required
def addstock():
        form = AddStockForm()
        if form.validate_on_submit():
                size = request.form['size']
                type = request.form['type']
                colour = request.form['colour']
                brand = request.form['brand']
                price = request.form['price']
                supplierid = request.form['supplierid']
                material = request.form['material']

                
                record = stock(size,type,colour,brand,price,supplierid,material)
                db.session.add(record)
                db.session.commit()
                message = f"The Stock has been submitted"
                return redirect(url_for('stockpage'))
        else:
                #show validation
                for field, errors in form.errors.items():
                        for error in errors:
                                flash("Error in {}: {}".format(
                                        getattr(form, field).label.text,
                                        error
                                ), 'error')
                return render_template('addstock.html', form=form)




@app.route('/deletestock/<int:stockid>', methods=['GET','POST'])
@login_required
def deletestock(stockid):
        qry = db.session.query(stock).filter(stock.stockid==stockid)
        stockid = qry.first()
        if stockid:
                form = DeleteStockForm(formdata=request.form, obj=stockid)
                if request.method == 'POST' and form.validate():
                        db.session.delete(stockid)
                        db.session.commit()
                        flash('Stock deleted successfully!')
                        return redirect('/stockpage')
                return render_template('deletestock.html', form=form)
        else:
                return 'Error deleting stock'.format (stockid=stockid)


@app.route('/editstock/<int:stockid>', methods=['GET', 'POST'])
@login_required
def editstock(stockid):
        qry = db.session.query(stock).filter( stock.stockid == stockid)
        stockid = qry.first()
        if stockid:
                form = EditStockForm(formdata=request.form, obj = stockid)
                if request.method == 'POST' and form.validate():
                        save_stock(stockid,form)

                        flash ('Stock updated!')
                        return redirect ('/stockpage')
                return render_template('stockpage.html', form=form)
        else:
                return 'Error loading the customer'.format(stockid=stockid)




@app.route('/allstock')
@login_required
def allstock():
        results=[]
        qry = db.session.query(stock)
        results = qry.all()
        table=StockResults(results)
        table.border =True
        return render_template('allstock.html', table=table)


def save_stock(stockid, form, new=False):
        #stockid.stockid = form.stockid.data
        stockid.size = form.size.data
        stockid.type = form.type.data
        stockid.colour = form.colour.data
        stockid.brand = form.brand.data
        stockid.price = form.price.data
        stockid.supplierid = form.supplierid.data
        stockid.material = form.material.data
        if new:
                db.session.add(stockid)
        db.session.commit()



#not working yet need to leave the house!
@app.route('/stockresults')
@login_required
def searchstockresults(search):
        results = []
        search_string = search.data['search']
        if search_string:
                if search.data ['select'] == 'stockid':
                        qry = db.session.query(stock).filter(stock.stockid.contains(search_string))
                        results = qry.all()
                else:
                        qry = db.session.query(stock)
                        results = qry.all()

        if not results:
                flash('No results found, please try again')
                return redirect ('/stockpage')
        else:
                table = StockResults(results)
                table.border = True
                return render_template('results.html', table=table)






class solditem(db.Model):
    __tablename__ = 'solditem'
    solditemid = db.Column(db.Integer, primary_key = True)
    customerfirstname = db.Column(db.String())
    customersurname = db.Column(db.String)
    email = db.Column(db.String)
    stockid = db.Column(db.Integer)
    price = db.Column(db.Float)
    supplierid = db.Column(db.Integer)
    suppliername = db.Column(db.String)



    def __init__(self,customerfirstname, customersurname, email, stockid, price, supplierid, suppliername):
        self.customerfirstname = customerfirstname
        self.customersurname = customersurname
        self.email = email
        self.stockid = stockid
        self.price = price
        self.supplierid = supplierid
        self.suppliername = suppliername



@app.route('/addsolditem', methods=['GET', 'POST'])
@login_required
def addsolditem():
        form = AddSoldItemForm()
        if form.validate_on_submit():
                customerfirstname = request.form['customerfirstname']
                customersurname = request.form['customersurname']
                email = request.form['email']
                stockid = request.form['stockid']
                price = request.form['price']
                supplierid = request.form['supplierid']
                suppliername = request.form['suppliername']

                
                record = solditem(customerfirstname, customersurname, email, stockid, price, supplierid, suppliername)
                db.session.add(record)
                db.session.commit()
                message = f"The Sold Item has been submitted"
                return redirect(url_for('solditempage'))
        else:
                #show validation
                for field, errors in form.errors.items():
                        for error in errors:
                                flash("Error in {}: {}".format(
                                        getattr(form, field).label.text,
                                        error
                                ), 'error')


                return render_template('addsolditem.html', form=form)







@app.route('/deletesolditem/<int:solditemid>', methods=['GET','POST'])
@login_required
def deletesolditem(solditemid):
        qry = db.session.query(solditem).filter(solditem.solditemid==solditemid)
        customersurname = qry.first()
        if customersurname:
                form = DeleteSoldItemForm(formdata=request.form, obj=customersurname)
                if request.method == 'POST' and form.validate():
                        db.session.delete(customersurname)
                        db.session.commit()
                        flash('Sold Item deleted successfully!')
                        return redirect('/solditempage')
                return render_template('deletesolditem.html', form=form)
        else:
                return 'Error deleting the Sold Item'.format (solditemid=solditemid)


@app.route('/editsolditem/<int:solditemid>', methods=['GET', 'POST'])
@login_required
def editsolditem(solditemid):
        qry = db.session.query(solditem).filter( solditem.solditemid == solditemid)
        solditemid = qry.first()
        if solditemid:
                form = EditSoldItemForm(formdata=request.form, obj = solditemid)
                if request.method == 'POST' and form.validate():
                        save_solditem(solditemid,form)

                        flash ('Sold Item updated!')
                        return redirect ('/solditempage')
                return render_template('solditempage.html', form=form)
        else:
                return 'Error loading the sold item'.format(solditemid=solditemid)






        # suppliername = ('Supplier Name')
        # edit = LinkCol('Edit', 'editsolditem', url_kwargs=dict(solditemid='solditemid'))
        # delete = LinkCol('Delete', 'editsolditem', url_kwargs=dict(solditemid='solditemid'))

@app.route('/allsolditem')
@login_required
def allsolditem():
        results=[]
        qry = db.session.query(solditem)
        results = qry.all()
        table=SoldItemResults(results)
        table.border =True
        return render_template('allsolditem.html', table=table)



def save_customer(customersurname, form, new=False):
        customersurname.customerfirstname = form.customerfirstname.data
        customersurname.customersurname = form.customersurname.data
        customersurname.email = form.email.data

        if new:
                db.session.add(customersurname)
        db.session.commit()


def save_solditem(solditemid, form, new=False):
        solditemid.customerfirstname = form.customerfirstname.data
        solditemid.customersurname = form.customersurname.data
        solditemid.email = form.email.data
        solditemid.stockid = form.stockid.data
        solditemid.price = form.price.data
        solditemid.supplierid = form.supplierid.data
        solditemid.suppliername = form.suppliername.data
        if new:
                db.session.add(solditemid)
        db.session.commit()



@app.route('/solditemresults')
@login_required
def searchsolditemresults(search):
        results = []
        search_string = search.data['search']
        if search_string:
                if search.data ['select'] == 'customersurname':
                        qry = db.session.query(solditem).filter(solditem.customersurname.contains(search_string))
                        results = qry.all()
                        # table = SoldItemResults(results)
                        # table.border = True
                        # return render_template('results.html', table=table)

        if not results:
                flash('No results found')
                return redirect ('/solditempage')
        else:
                table = SoldItemResults(results)
                table.border = True
                return render_template('results.html', table=table)





@app.route('/moniesdueresults')
@login_required
def searchcompilemonies(search):
        supplierid = search
        results = []
        search_string = search.data['search']
        if search_string:
                if search.data ['select'] == 'supplierid':
                        results = db.session.query(func.sum(solditem.price).filter(solditem.supplierid==(search_string)))

                else:
                        qry = db.session.query(solditem)
                        results = qry.all()
        if not results:
                flash('No results found')
                return redirect ('/compilemonies')
        else:
                for i in results:
                        print(i[0])
                Hello=('The money owed to the supplier in £ is...')
                return render_template('results.html', i=i, Hello=Hello)



@app.route('/userresults')
@login_required
def searchuserresults(search):
        results = []
        search_string = search.data['search']
        if search_string:
                if search.data ['select'] == 'username':
                        qry = db.session.query(User).filter(User.username.contains(search_string))
                        results = qry.all()
                else:
                        qry = db.session.query(User)
                        results = qry.all()
        if not results:
                flash('No results found')
                return redirect ('/userpage')
        else:
                table = UserResults(results)
                table.border = True
                return render_template('results.html', table=table)


@app.route('/alluser')
@login_required
def alluser():
        results=[]
        qry = db.session.query(User)
        results = qry.all()
        table=UserResults(results)
        table.border =True
        return render_template('alluser.html', table=table)


@app.route('/userpage', methods = ['GET', 'POST'])
@login_required
def userpage():
        search = UserSearchForm(request.form)
        if request.method == 'POST':
                return searchuserresults(search)

        return render_template('userpage.html', form=search)


@app.route('/adduser', methods=['GET', 'POST'])
@login_required
def adduser():
        form = AddUserForm()
        if form.validate_on_submit():
                username = form.username.data
                password = form.password.data
                email = form.email.data

        if form.validate_on_submit():
                user = User.query.filter_by(username=username).first()
                if not user:
                        record = User(username=username, password=password, email=email)
                        db.session.add(record)
                        db.session.commit()
                return redirect(url_for('userpage'))
        else:
                return render_template('adduser.html', form=form)






@app.route('/edituser/<int:id>', methods=['GET', 'POST'])
@login_required
def edituser(id):
        qry = db.session.query(User).filter( User.id == id)
        username = qry.first()
        if username:
                form = EditUserForm(formdata=request.form, obj = username)
                if request.method == 'POST' and form.validate():
                        save_user(username,form)

                        flash ('User updated!')
                        return redirect ('/userpage')
                return render_template('userpage.html', form=form)
        else:
                return 'Error loading the user'.format(id=id)




def save_user(username, form, new=False):
        username.username = form.username.data
        username.password = form.password.data
        username.email = form.email.data

        if new:
                record = User(username= username, password= generate_password_hash(password, method = 'sha256'), email= email)
                db.session.add(username)
        db.session.commit()



@app.route('/deleteuser<int:id>', methods=['GET', 'POST'])
@login_required
def deleteuser(id):
        qry = db.session.query(User).filter(User.id==id)
        username = qry.first()
        if username:
                form = DeleteUserForm(formdata=request.form, obj=username)
                if request.method == 'POST' and form.validate():
                        db.session.delete(username)
                        db.session.commit()
                        flash('User deleted succesfully!')
                        return redirect('/userpage')
                return render_template('deleteuser.html', form=form)
        else:
                return 'Error deleting User'. format(id=id)



class listing(db.Model):
        __tablename__ = 'listing'
        listingid = db.Column(db.Integer, primary_key = True)
        supplierid = db.Column(db.Integer)
        price = db.Column(db.Float)


        def __init__(self, supplierid, price):
                self.supplierid = supplierid
                self.price = price
    


@app.route('/addlisting', methods=['GET', 'POST'])
@login_required
def addlisting():
        form = AddListingForm()
        if form.validate_on_submit():
                supplierid = request.form['supplierid']
                price = request.form['price']
                
                record = listing(supplierid, price)
                db.session.add(record)
                db.session.commit()
                message = f"The Listing has been submitted"
                return redirect(url_for('listingpage'))
        else:
                #show validation
                for field, errors in form.errors.items():
                        for error in errors:
                                flash("Error in {}: {}".format(
                                        getattr(form, field).label.text,
                                        error
                                ), 'error')
        return render_template('addlisting.html', form=form)





@app.route('/deletelisting<int:listingid>', methods=['GET', 'POST'])
@login_required
def deletelisting(listingid):
        qry = db.session.query(listing).filter(listing.listingid==listingid)
        supplierid = qry.first()
        if supplierid:
                form = DeleteListingForm(formdata=request.form, obj=supplierid)
                if request.method == 'POST' and form.validate():
                        db.session.delete(supplierid)
                        db.session.commit()
                        flash('Listing deleted succesfully!')
                        return redirect('/listingpage')
                return render_template('listingpage.html', form=form)
        else:
                return 'Error deleting listing'.format(listingid=listingid)
        

@app.route('/editlisting<int:listingid>', methods=['GET', 'POST'])
@login_required
def editlisting(listingid):
        qry = db.session.query(listing).filter(listing.listingid==listingid)
        supplierid = qry.first()
        if supplierid:
                form = EditListingForm(formdata=request.form, obj=supplierid)
                if request.method == 'POST' and form.validate():
                        save_listing(supplierid,form)
                        flash ('Listing Updated!')
                        return redirect('/listingpage')
                return render_template('listingpage.html', form=form)
        else:
                return 'Error loading the listing'. format(listingid=listingid )

def save_listing(supplierid, form, new=False):
        supplierid.supplierid = form.supplierid.data
        supplierid.price = form.price.data
        if new:
                db.session.add(supplierid)
        db.session.commit()

@app.route('/listingresults')
@login_required
def searchlistingresults(search):
        results=[]
        search_string = search.data['search']
        if search_string:
                if search.data ['select'] == 'supplierid':
                        qry = db.session.query(listing).filter(listing.supplierid.contains(search_string))
                        results = qry.all()
                else:
                        qry = db.sesssion.query(listing)
                        results = qry.all()
        if not results:
                flash('No results found')
                return redirect ('/listingpage')
        else:
                table = ListingResults(results)
                table.border = True
                return render_template('results.html', table=table)


@app.route('/alllisting')
@login_required
def alllisting():
        results=[]
        qry = db.session.query(listing)
        results = qry.all()
        table=ListingResults(results)
        table.border =True
        return render_template('alllisting.html', table=table)







###LOGIN ATTEMPT
# @app.route('/login/', methods=['GET', 'POST'])
# def login():
#         message =''
#         return render_template('index.html', message='')

#         if request.method == 'POST' and 'ausername' in request.form and 'apassword' in request.form:
#                 ausername = request.form['ausername']





@app.route('/register', methods=['GET', 'POST'])
def register():
        form = RegisterForm()
        username = form.username.data
        password = form.password.data
        email = form.email.data

        if form.validate_on_submit():
                user = User.query.filter_by(username=username).first()
                if not user:
                        record = User(username=username, password=password, email=email)
                        db.session.add(record)
                        db.session.commit()
                return redirect(url_for('login'))
        else:
                return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
        form = LoginForm()
        username = form.username.data
        password = form.password.data

        if form.validate_on_submit():
                user = User.query.filter_by(username=username).first()

                if user and user.verify_password(password):
                        login_user(user)
                        flash("User Logged In!")
                        return redirect(url_for('loggedin'))
                else:
                        flash("Invalid Login")
        else:
                print(form.errors)
        
        return render_template('login.html', form=form)

@login_manager.user_loader
def get_user(id):
        return User.query.get(id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(10))
    email = db.Column(db.String(), unique=True, nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email

    def __repr__(self):
            return f'<User {self.username}>'

    def verify_password(self,pwd):
            return check_password_hash(self.password,pwd)

@app.route("/")
#@login_required
def index():
        return render_template('index.html')

@app.route('/logout')
def logout():
        logout_user()
        return redirect(url_for('login'))

@app.route('/currentuser', methods=['GET'])
@login_required
def currentuser():
        return render_template('currentuser.html')




if __name__ == "__main__":
    app.run(debug=True)