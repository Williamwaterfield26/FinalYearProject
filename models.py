class supplier(db.Model):
        __tablename__ = 'supplier'
        supplierid = db.Column(db.Integer, primary_key = True)
        suppliername = db.Column(db.String)





        def __init__(self, suppliername):
                self.suppliername = suppliername
    


class stock(db.Model):
    __tablename__ = 'stock'
    stockid = db.Column(db.Integer, primary_key = True)
    size = db.Column(db.String(3))
    type = db.Column(db.String)
    colour = db.Column(db.String)
    brand = db.Column(db.String)
    price = db.Column(db.Float)
    material = db.Column(db.String)

    supplierid = db.Column(
        db.Integer,
        db.ForeignKey('supplier.supplierid'),
        nullable=False)





    def __init__(self,size,type,colour,brand,price,material,supplierid):
        self.size = size
        self.type = type
        self.colour = colour
        self.brand = brand
        self.price = price
        self.material = material
        self.supplierid = supplierid



class solditem(db.Model):
    __tablename__ = 'solditem'
    solditemid = db.Column(db.Integer, primary_key = True)
    customerfirstname = db.Column(db.String())
    customersurname = db.Column(db.String)
    email = db.Column(db.String)
    stockid = db.Column(
        db.Integer,
        db.ForeignKey('stock.stockid'),
        nullable=False)
    price = db.Column(db.Float)
    supplierid = db.Column(
        db.Integer,
        db.ForeignKey('supplier.supplierid'),
        nullable=False)
    suppliername = db.Column(db.String)



    def __init__(self,customerfirstname, customersurname, email, stockid, price, supplierid, suppliername):
        self.customerfirstname = customerfirstname
        self.customersurname = customersurname
        self.email = email
        self.stockid = stockid
        self.price = price
        self.supplierid = supplierid
        self.suppliername = suppliername
