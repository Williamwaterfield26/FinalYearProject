

#SHOULD BE IN APP.PY
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
                stockid = request.form['stockid']
                price = request.form['price']
                
                record = listing(stockid, price)
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
        stockid = qry.first()
        if stockid:
                form = DeleteListingForm(formdata=request.form, obj=stockid)
                if request.method == 'POST' and form.validate():
                        db.session.delete(stockid)
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
        stockid = qry.first()
        if stockid:
                form = EditListingForm(formdata=request.form, obj=stockid)
                if request.method == 'POST' and form.validate():
                        save_listing(stockid,form)
                        flash ('Listing Updated!')
                        return redirect('/listingpage')
                return render_template('listingpage.html', form=form)
        else:
                return 'Error loading the listing'. format(listingid=listingid )


def save_listing(supplierid, form, new=False):
        stockid.stockid = form.stockid.data
        stockid.price = form.price.data
        if new:
                db.session.add(stockid)
        db.session.commit()


@app.route('/listingresults')
@login_required
def searchlistingresults(search):
        results=[]
        search_string = search.data['search']
        if search_string:
                if search.data ['select'] == 'stockid':
                        qry = db.session.query(listing).filter(listing.stockid.contains(search_string))
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


#TABLES.Py
class ListingResults(Table):
        listingid = Col('listingid', show= False)
        stockid = Col('Stockid')
        price = Col('Price')
        edit = LinkCol('Edit', 'editlisting', url_kwargs=dict(listingid='listingid'))
        delete = LinkCol('Delete', 'deletelisting', url_kwargs=dict(listingid='listingid'))



#FORMS.PY


class AddListingForm(FlaskForm):
    listingid = HiddenField()
    stockid = IntegerField('Stock ID', [InputRequired(),
    NumberRange(min=1.00, max=4000, message= "Invalid Stock ID")
    ])
    price = FloatField('Price', [InputRequired(),
    NumberRange(min=1.00, message= "Invalid Price Range. Please enter a price of at least £1"),
    ])
    submit = SubmitField('Add Listing')


class EditListingForm(FlaskForm):
    stockid = IntegerField('Stock ID', [InputRequired(),
    NumberRange(min=1.00, max=4000, message= "Invalid Stock ID")
    ])
    price = FloatField('Price', [InputRequired(),
    NumberRange(min=1.00, max=4000, message= "Invalid Price Range. Please enter a price of at least £1"),
    ])
    update = SubmitField('Update')
    cancel = SubmitField('Cancel')



class DeleteListingForm(FlaskForm):
    stockid= IntegerField('Stock ID')
    price= IntegerField('Price')
    delete = SubmitField('Delete')

class ListingSearchForm(FlaskForm):
    choices = [('stockid', 'stockid')]
    select = SelectField ('Search for a listing', choices=choices)
    search = StringField('')