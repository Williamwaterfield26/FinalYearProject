from flask_table import Table, Col


class CustomerResults(Table):
        customerid = Col('customerid', show = False)
        customerfirstname = Col('customerfirstname')
        customersurname = Col('customersurname')
        email = Col('email')