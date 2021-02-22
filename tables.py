from flask_table import Table, Col, LinkCol


class CustomerResults(Table):
        customerid = Col('Customerid', show = False)
        customerfirstname = Col('Customerfirstname')
        customersurname = Col('Customersurname')
        email = Col('Email')
        edit = LinkCol('Edit', 'editcustomer', url_kwargs=dict(customerid='customerid'))
        delete = LinkCol('Delete', 'deletecustomer', url_kwargs=dict(customerid='customerid'))
        

class SupplierResults(Table):
        supplierid = Col('supplierid', show= True)
        suppliername = Col('Suppliername')
        edit = LinkCol('Edit', 'editsupplier', url_kwargs=dict(supplierid='supplierid'))
        delete = LinkCol('Delete', 'deletesupplier', url_kwargs=dict(supplierid='supplierid'))
        

class ListingResults(Table):
        listingid = Col('listingid', show= False)
        supplierid = Col('Supplierid')
        price = Col('Price')
        edit = LinkCol('Edit', 'editlisting', url_kwargs=dict(listingid='listingid'))
        delete = LinkCol('Delete', 'deletelisting', url_kwargs=dict(listingid='listingid'))

class StockResults(Table):
        stockid = Col('Stockid', show= False)
        size= Col('Size')
        type= Col('Type')
        colour = Col('Colour')
        brand = Col('Brand')
        price = Col('Price')
        supplierid = Col('Supplierid')
        material = Col('Material')
        edit = LinkCol('Edit', 'editstock', url_kwargs=dict(stockid='stockid'))
        delete = LinkCol('Delete', 'deletestock', url_kwargs=dict(stockid='stockid'))

class SoldItemResults(Table):
        solditemid = Col('Sold Item ID', show=False)
        customerfirstname= Col('Customer Firstname')
        customersurname= Col('Customer Surname')
        email = Col('Email')
        stockid = Col('Stock ID')
        price = ('Price')
        supplierid = ('Supplier ID')
        suppliername = ('Supplier Name')
        edit = LinkCol('Edit', 'editsolditem', url_kwargs=dict(solditemid='solditemid'))
        delete = LinkCol('Delete', 'editsolditem', url_kwargs=dict(solditemid='solditemid'))
