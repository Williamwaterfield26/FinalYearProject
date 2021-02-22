from flask_table import Table, Col, LinkCol


class CustomerResults(Table):
        customerid = Col('customerid', show = False)
        customerfirstname = Col('customerfirstname')
        customersurname = Col('customersurname')
        email = Col('email')
        edit = LinkCol('Edit', 'editcustomer', url_kwargs=dict(customerid='customerid'))
        delete = LinkCol('Delete', 'deletecustomer', url_kwargs=dict(customerid='customerid'))
        

class SupplierResults(Table):
        supplierid = Col('supplierid', show= False)
        suppliername = Col('suppliername')
        edit = LinkCol('Edit', 'editsupplier', url_kwargs=dict(supplierid='supplierid'))
        delete = LinkCol('Delete', 'deletesupplier', url_kwargs=dict(supplierid='supplierid'))
        

class ListingResults(Table):
        listingid = Col('listingid', show= False)
        supplierid = Col('supplierid')
        price = Col('price')
        edit = LinkCol('Edit', 'editlisting', url_kwargs=dict(listingid='listingid'))
        delete = LinkCol('Delete', 'deletelisting', url_kwargs=dict(listingid='listingid'))
        