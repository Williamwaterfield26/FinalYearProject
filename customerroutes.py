from flask import Blueprint, render_template, redirect, url_for, flash, request
from forms import EditCustomerForm, CustomerSearchForm, AddCustomerForm
customers = Blueprint('customers', __name__)

@customers.route('/all_customers')
def all_customers():
    return 'All Customers Page'

@customers.route('/new_customer', methods =['GET', 'POST'])
def new_customer():
    form = AddCustomerForm()
    if form. validate_on_submit():
        customerfirstname = request.form['customerfirstname']
        customersurname = request.form['customersurname']
        email = request.form['email']

                
        record = customer(customerfirstname,customersurname,email)
        db.session.add(record)
        db.session.commit()
        message = f"The Customer has been submitted"
        return render_template('customerpage.html', message=message)


@customers.route('/customer/<customerid>', methods = ['GET', 'POST'])
def customer(customerid):
    customer = customer.query.get(customerid)
    return render_template('customerpage.html', customer = customer)


@customers.route('/editcustomer/<customerid>', methods = ['GET', 'POST'])
def edit_customer(customerid):
    customer = Customer.query.get(customerid)
    form = EditCustomerForm(obj=customer)
    if request.method== 'GET':
        form.populate_obj(customer)
    elif request.method == 'POST':
        if form.update.data and form.validate_on_submit():
            customer.customerfirstname = form.customerfirstname.data
            customer.customersurname = form.customersurname.data
            customer.email = form.email.data
            db.session.commit()
            flash ('Update was successful', 'success')
            return redirect(url_for('customers.customer',customerid= customerid))
        if form.cancel.data:
            return redirect(url_for('customers.customer',customerid = customerid))
        return render_template('customerpage.html', form=form)


@customers.route('/deletecustomer/<customerid>', methods= ['GET','POST'])
def delete_customer(customerid):
    if customer.query.filter_by(customerid=customer).delete():
        db.session.commit()
        flash('Customer has been deleted', 'success')
        return redirect (url_for('customerpage.html'))
    return redirect(url_for('customerpage.html', customerid=customerid))


@customers.route('/searchcustomer',methods=['GET','POST'])
def searchcustomer():
    customers=None
    target_string = request.form['CustomerSearchForm']
    customers = Customer.query.filter(Customer.title.contains(target_string)).all()

    if target_string == "":
        search_msg = f'No matching customers found- displaying all {len(customers)} customers'
        color = 'danger'
    else:
        search_msg = f'{len(customers)} customers found'
        color = 'success'
    return render_template('customerpage.html',title = 'Search result', customers=customers, search_msg = search_msg, color=color)
