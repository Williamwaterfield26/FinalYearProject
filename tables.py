from flask_table import Table, Col, LinkCol


class CustomerResults(Table):
        customerid = Col('customerid', show = False)
        customerfirstname = Col('customerfirstname')
        customersurname = Col('customersurname')
        email = Col('email')
        edit = LinkCol('Edit', 'editcustomer', url_kwargs=dict(customerid='customerid'))
        delete = LinkCol('Delete', 'deletecustomer', url_kwargs=dict(customerid='customerid'))
        
