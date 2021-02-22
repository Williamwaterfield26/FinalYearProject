from flask import Flask, render_template, url_for, redirect, request, flash, Blueprint
from forms import SignUpForm, SignInForm, AddCustomerForm, AddStockForm, AddSupplierForm, AddListingForm, AddAdminForm, CustomerSearchForm, EditCustomerForm, DeleteCustomerForm, SupplierSearchForm, EditSupplierForm, DeleteSupplierForm, ListingSearchForm, EditListingForm, DeleteLitingForm, StockSearchForm, EditStockForm, DeleteStockForm, AddSoldItemForm, DeleteSoldItemForm, EditSoldItemForm, SoldItemSearchForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_login import UserMixin
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, SubmitField, HiddenField, IntegerField, FloatField
from wtforms.validators import DataRequired, InputRequired, Length, Regexp, NumberRange
from flask_table import Table, Col, LinkCol
from django import forms
from tables import CustomerResults, SupplierResults, ListingResults, StockResults, SoldItemResults
#from models import customer



app= Flask (__name__)
app.config ['SECRET_KEY'] = 'bob'
Bootstrap(app)
db_name = 'DatabaseFYP.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

class admin(UserMixin, db.Model):
        id = db.Column(db.Integer, primary_key=True)
        ausername = db.Column(db.String(10), nullable= False, unique = True)
        apassword = db.Column(db.String(10))
        email = db.Column(db.String)


@app.route('/signin', methods= ['GET','POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit():
            ausername= request.form['ausername']
            apassword= request.form['apassword']
            #remember = True if request.form.get('remember') else False
            
            record = admin.query.filter_by(ausername=ausername).first()
            if not admin or not check_password_hash(admin.apassword, apassword):
                    flash('Please check your login details and try again.')
                    return redirect(url_for('signin.html'))
            return redirect(url_for('loggedin.html'))
    return render_template('signin.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
        form = AddAdminForm()
        if form.validate_on_submit():
                ausername = request.form['ausername']
                apassword = request.form['apassword']
                email = request.form['email']
                
                #record = admin(ausername,apassword,email)
                record = admin(ausername= ausername, apassword= generate_password_hash(apassword, method = 'sha256'), email= email)
                db.session.add(record)
                db.session.commit()
                message = f"The Supplier has been submitted"
                return render_template('signin.html', message=message)
        else:
                #show validation
                for field, errors in form.errors.items():
                        for error in errors:
                                flash("Error in {}: {}".format(
                                        getattr(form, field).label.text,
                                        error
                                ), 'error')
                return render_template('signup.html', form=form)


#hi
#@app.route('/signup', methods=['GET', 'POST'])
#def signup():
#        form = AddAdminForm()
#        if form.validate_on_submit:
#                ausername = request.form['ausername']
#                apassword = request.form['apassword']
#                email = request.form['email']
#                #record = Admin(ausername= ausername, apassword= generate_password_hash(apassword, method = 'sha256'), email= email)
#                new_admin = Admin(ausername= ausername, apassword= generate_password_hash(apassword, method = 'sha256'), email= email)
#                db.session.add(new_admin)
#                db.session.commit()
#                return redirect(url_for('/signin'))
#        else:   
 #               if admin:
#
 #                       admin = Admin.query.filter_by(ausername=ausername).first()
#                        return redirect(url_for('/signup'))


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
def loggedin():
        return render_template('loggedin.html')


@app.route('/supplierpage', methods = ['GET', 'POST'])
def supplierpage():
        search = SupplierSearchForm(request.form)
        if request.method == 'POST':
                return searchsupplierresults(search)
        return render_template('supplierpage.html',form=search)
        


@app.route('/customerpage', methods = ['GET', 'POST'])
def customerpage():
        #form = CustomerSearchForm()
        search = CustomerSearchForm(request.form)
        if request.method == 'POST':
                return searchcustomerresults(search)

        #return render_template('customerpage.html', search=search, form=form)
        return render_template('customerpage.html', form=search)

# #number 1
@app.route('/customerresults')
def searchcustomerresults(search):
        results = []
        search_string = search.data['search']

        if search.data['search']== '':
                qry = db.session.query(customer)
                results = qry.all()
        if not results:
                flash('No results found')
                return redirect ('/customerpage')
        else:
                table = CustomerResults(results)
                table.border = True
                return render_template('results.html', table=table)



# @app.route('/customerresults/<int:customerid>', methods=['GET', 'POST'])
# def searchcustomerresults(search):
#         results = []
#         search_string = search.data['search']
#         if search_string:
#                 if search.data['select']== 'customerid':
#                         qry = db.session.query(customerid, customersurname).filter(customerfirstname==customersurname).filter(customer.customerid.contains(search_string))
#                         results= [item[0] for item in qry.all()]
#                 elif search.data ['select'] == 'customerfirstname':
#                         qry = db.session.query(customerfirstname).filter(customerfirstname.customerfirstname.contains(search_string))
#                         results = qry.all()
#                 elif search.data ['select'] == 'customersurname':
#                         qry = db.session.query(customersurname).filter(customersurname.customersurname.contains(search_string))
#                         results = qry.all()
                        
#         if not results:
#                 flash('No results found')
#                 return redirect ('/customerpage')
#         else:
#                 table = CustomerResults(results)
#                 table.border = True
#                 return render_template('results.html', table=table)







#@app.route('/editcustomer',methods=['GET', 'POST'])
@app.route('/editcustomer/<int:customerid>', methods=['GET', 'POST'])
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
def results():
        return render_template('results.html')


@app.route('/userpage')
def userpage():
        return render_template('userpage.html')



@app.route('/listingpage',methods = ['GET', 'POST'])
def listingpage():
        search = ListingSearchForm(request.form)
        if request.method == 'POST':
                return searchlistingresults(search)
        return render_template('listingpage.html', form=search)
        


@app.route('/stockpage', methods = ['GET', 'POST'])
def stockpage():
        search = StockSearchForm(request.form)
        if request.method == 'POST':
                return searchstockresults(search)
        return render_template('stockpage.html', form=search)


@app.route('/solditempage', methods = ['GET', 'POST'])
def solditempage():
        search = SoldItemSearchForm(request.form)
        if request.method == 'POST':
                return searchsolditemresults(search)
        return render_template('solditempage.html', form=search)


@app.route('/logoff')
def logoff():
        return render_template('logoff.html')
        
        
class supplier(db.Model):
        __tablename__ = 'supplier'
        supplierid = db.Column(db.Integer, primary_key = True)
        suppliername = db.Column(db.String)


        def __init__(self, suppliername):
                self.suppliername = suppliername
    


@app.route('/addsupplier', methods=['GET', 'POST'])
def addsupplier():
        form = AddSupplierForm()
        if form.validate_on_submit():
                suppliername = request.form['suppliername']
                
                record = supplier(suppliername)
                db.session.add(record)
                db.session.commit()
                message = f"The Supplier has been submitted"
                return render_template('supplierpage.html', message=message)
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
def deletesupplier(supplierid):
        qry = db.session.query(supplier).filter(supplier.supplierid==supplierid)
        suppliername = qry.first()
        if suppliername:
                form = DeleteSupplierForm(formdata=request.form, obj=supplier)
                if request.method == 'POST' and form.validate():
                        db.session.delete(suppliername)
                        db.session.commit()
                        flash('Supplier deleted successfully!')
                        return redirect('/supplierpage')
                return render_template('deletesupplier.html', form=form)
        else:
                return 'Error deleting supplier'.format(supplierid=supplierid)
















@app.route('/editsupplier/<int:supplierid>',methods= ['GET','POST'])
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
        

@app.route('/searchsupplier')
def searchsupplierresults(search):
        results = []
        search_string = search.data['search']
        if search.data['search']== '':
                qry = db.session.query(supplier)
                results = qry.all()
        if not results:
                flash('No results found')
                return redirect('/supplierpage')
        else:
                table = SupplierResults(results)
                table.border = True
                return render_template('results.html', table=table)




@app.route('/allsupplier')
def allsupplier():
        return render_template('allsupplier.html')




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
                return render_template('customerpage.html', message=message)
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
@app.route('/deletecustomer/<int:customerid>', methods=['GET','POST'])
def deletecustomer(customerid):
        qry = db.session.query(customer).filter(customer.customerid==customerid)
        customersurname = qry.first()
        if customersurname:
                form = DeleteCustomerForm(formdata=request.form, obj=customer)
                if request.method == 'POST' and form.validate():
                        db.session.delete(customersurname)
                        db.session.commit()
                        flash('Customer deleted successfully!')
                        return redirect('/customerpage')
                return render_template('deletecustomer.html', form=form)
        else:
                return 'Error deleting customer'.format (customerid=customerid)



# @app.route('/editcustomer')
# def editcustomer():
#         return render_template('editcustomer.html')

# @app.route('/searchcustomer')
# def searchcustomer():
#         return render_template('searchcustomer.html')
# @app.route('/allcustomer')
# def allcustomer():
#         return render_template('allcustomer.html')






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
                return render_template('stockpage.html', message=message)
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
def deletestock(stockid):
        qry = db.session.query(stock).filter(stock.stockid==stockid)
        stockid = qry.first()
        if stockid:
                form = DeleteStockForm(formdata=request.form, obj=stock)
                if request.method == 'POST' and form.validate():
                        db.session.delete(stockid)
                        db.session.commit()
                        flash('Stock deleted successfully!')
                        return redirect('/stockpage')
                return render_template('deletestock.html', form=form)
        else:
                return 'Error deleting stock'.format (stockid=stockid)


@app.route('/editstock/<int:stockid>', methods=['GET', 'POST'])
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






@app.route('/stockresults')
def searchstockresults(search):
        results = []
        search_string = search.data['search']

        if search.data['search']== '':
                qry = db.session.query(stock)
                results = qry.all()
        if not results:
                flash('No results found')
                return redirect ('/stockpage')
        else:
                table = StockResults(results)
                table.border = True
                return render_template('results.html', table=table)


@app.route('/allstock')
def allstock():
        return render_template('allstock.html')

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
                return render_template('solditempage.html', message=message)
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
def deletesolditem(solditemid):
        qry = db.session.query(solditem).filter(solditem.solditemid==solditemid)
        solditemid = qry.first()
        if solditemid:
                form = DeleteSoldItemForm(formdata=request.form, obj=solditem)
                if request.method == 'POST' and form.validate():
                        db.session.delete(solditemid)
                        db.session.commit()
                        flash('Sold Item deleted successfully!')
                        return redirect('/solditempage')
                return render_template('solditempage.html', form=form)
        else:
                return 'Error deleting the Sold Item'.format (solditemid=solditemid)


@app.route('/editsolditem/<int:solditemid>', methods=['GET', 'POST'])
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



        suppliername = ('Supplier Name')
        edit = LinkCol('Edit', 'editsolditem', url_kwargs=dict(solditemid='solditemid'))
        delete = LinkCol('Delete', 'editsolditem', url_kwargs=dict(solditemid='solditemid'))




def save_solditem(solditemid, form, new=False):
        solditemid.solditemid = form.solditemid.data
        solditemid.customerfirstname = form.customerfirstname.data
        solditemid.email = form.email.data
        solditemid.stockid = form.stockid.data
        solditemid.price = form.price.data
        solditemid.supplierid = form.supplierid.data
        solditemid.suppliername = form.suppliername.data
        if new:
                db.session.add(solditemid)
        db.session.commit()


@app.route('/solditemresults')
def searchsolditemresults(search):
        results = []
        search_string = search.data['search']

        if search.data['search']== '':
                qry = db.session.query(solditem)
                results = qry.all()
        if not results:
                flash('No results found')
                return redirect ('/solditempage')
        else:
                table = SoldItemResults(results)
                table.border = True
                return render_template('results.html', table=table)




@app.route('/allsolditems')
def allsolditems():
        return render_template('allsolditems.html')

@app.route('/adduser')
def adduser():
        return render_template('adduser.html')

@app.route('/deleteuser')
def deleteuser():
        return render_template('deleteuser.html')

@app.route('/edituser')
def edituser():
        return render_template('edituser.html')

@app.route('/searcheduser')
def searcheduser():
        return render_template('searcheduser.html')

@app.route('/alluser')
def alluser():
        return render_template('alluser.html')

class listing(db.Model):
        __tablename__ = 'listing'
        listingid = db.Column(db.Integer, primary_key = True)
        supplierid = db.Column(db.Integer)
        price = db.Column(db.Float)


        def __init__(self, supplierid, price):
                self.supplierid = supplierid
                self.price = price
    


@app.route('/addlisting', methods=['GET', 'POST'])
def addlisting():
        form = AddListingForm()
        if form.validate_on_submit():
                supplierid = request.form['supplierid']
                price = request.form['price']
                
                record = listing(supplierid, price)
                db.session.add(record)
                db.session.commit()
                message = f"The Listing has been submitted"
                return render_template('addlisting.html', message=message)
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
def deletelisting(listingid):
        qry = db.session.query(listing).filter(listing.listingid==listingid)
        supplierid = qry.first()
        if supplierid:
                form = DeleteLitingForm(formdata=request.form, obj=listing)
                if request.method == 'POST' and form.validate():
                        db.session.delete(supplierid)
                        db.session.commit()
                        flash('Listing deleted succesfully!')
                        return redirect('/listingpage')
                return render_template('deletelisting.html', form=form)
        else:
                return 'Error deleting listing'. format(listingid=listingid)
        

@app.route('/editlisting<int:listingid>', methods=['GET', 'POST'])
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
def searchlistingresults(search):
        results=[]
        search_string = search.data['search']
        if search.data['search']== '':
                qry = db.session.query(listing)
                results = qry.all()
        if not results:
                flash('No results found')
                return redirect ('/listingpage')
        else:
                table = ListingResults(results)
                table.border = True
                return render_template('results.html', table=table)



@app.route('/alllistings')
def alllistings():
        return render_template('alllistings.html')




#CUSTOMER STUFF

# @app.route('/all_customers')
# def all_customers():
#     return 'All Customers Page'

# # @app.route('/addcustomer', methods =['GET', 'POST'])
# # def addcustomer():
# #     form = AddCustomerForm()
# #     if form. validate_on_submit():
# #         customerfirstname = request.form['customerfirstname']
# #         customersurname = request.form['customersurname']
# #         email = request.form['email']

                
# #         record = customer(customerfirstname,customersurname,email)
# #         db.session.add(record)
# #         db.session.commit()
# #         message = f"The Customer has been submitted"
# #         return render_template('customerpage.html', message=message)


# # @app.route('/customer/<customerid>', methods = ['GET', 'POST'])
# # def customer(customerid):
# #     customer = customer.query.get(customerid)
# #     return render_template('customerpage.html', customer = customer)


# @app.route('/editcustomer/<customerid>', methods = ['GET', 'POST'])
# def editcustomer(customerid):
#     customer = Customer.query.get(customerid)
#     form = EditCustomerForm(obj=customer)
#     if request.method== 'GET':
#         form.populate_obj(customer)
#     elif request.method == 'POST':
#         if form.update.data and form.validate_on_submit():
#             customer.customerfirstname = form.customerfirstname.data
#             customer.customersurname = form.customersurname.data
#             customer.email = form.email.data
#             db.session.commit()
#             flash ('Update was successful', 'success')
#             return redirect(url_for('customers.customer',customerid= customerid))
#         if form.cancel.data:
#             return redirect(url_for('customers.customer',customerid = customerid))
#         return render_template('customerpage.html', form=form)


# @app.route('/deletecustomer/<customerid>', methods= ['GET','POST'])
# def deletecustomer(customerid):
#     if customer.query.filter_by(customerid=customer).delete():
#         db.session.commit()
#         flash('Customer has been deleted', 'success')
#         return redirect (url_for('customerpage.html'))
#     return redirect(url_for('customerpage.html', customerid=customerid))


# @app.route('/searchcustomer',methods=['GET','POST'])
# def searchcustomer():
#     customers=None
#     target_string = request.form['search']
#     customers = Customer.query.filter(Customer.title.contains(target_string)).all()

#     if target_string == "":
#         search_msg = f'No matching customers found- displaying all {len(customers)} customers'
#         color = 'danger'
#     else:
#         search_msg = f'{len(customers)} customers found'
#         color = 'success'
#     return render_template('customerpage.html',title = 'Search result', customers=customers, search_msg = search_msg, color=color)




if __name__ == "__main__":
    app.run(debug=True)