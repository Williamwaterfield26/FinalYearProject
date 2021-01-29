from flask import Flask, render_template, url_for
from forms import SignUpForm, SignInForm
from flask_sqlalchemy import SQLAlchemy

app= Flask (__name__)
app.config ['SECRET_KEY'] = 'bob'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin')
def signin():
    form = SignInForm()
    return render_template('signin.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    return render_template('signup.html', form=form)


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


@app.route('/supplierpage')
def supplierpage():
        return render_template('supplierpage.html')


@app.route('/customerpage')
def customerpage():
        return render_template('customerpage.html')


@app.route('/userpage')
def userpage():
        return render_template('userpage.html')



@app.route('/listingpage')
def listingpage():
        return render_template('listingpage.html')


@app.route('/stockpage')
def stockpage():
        return render_template('stockpage.html')

@app.route('/solditempage')
def solditempage():
        return render_template('solditempage.html')


@app.route('/logoff')
def logoff():
        return render_template('logoff.html')



@app.route('/addsupplier')
def addsupplier():
        return render_template('addsupplier.html')

@app.route('/deletesupplier')
def deletesupplier():
        return render_template('deletesupplier.html')


@app.route('/editsupplier')
def editsupplier():
        return render_template('editsupplier.html')

@app.route('/searchsupplier')
def searchsupplier():
        return render_template('searchsupplier.html')

@app.route('/allsupplier')
def allsupplier():
        return render_template('allsupplier.html')

@app.route('/addcustomer')
def addcustomer():
        return render_template('addcustomer.html')

@app.route('/editcustomer')
def editcustomer():
        return render_template('editcustomer.html')

@app.route('/searchcustomer')
def searchcustomer():
        return render_template('searchcustomer.html')


@app.route('/allcustomer')
def allcustomer():
        return render_template('allcustomer.html')

@app.route('/addstock')
def addstock():
        return render_template('addstock.html')

@app.route('/editstock')
def editstock():
        return render_template('editstock.html')

@app.route('/searchstock')
def searchstock():
        return render_template('searchstock.html')

@app.route('/allstock')
def allstock():
        return render_template('allstock.html')

@app.route('/deletesolditem')
def deletesolditem():
        return render_template('deletesolditem.html')

@app.route('/editsolditem')
def editsolditem():
        return render_template('editsolditem.html')

@app.route('/searchedsolditem')
def searchedsolditem():
        return render_template('searchedsolditem.html')

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

@app.route('/addlisting')
def addlisting():
        return render_template('addlisting.html')

@app.route('/deletelisting')
def deletelisting():
        return render_template('deletelisting.html')

@app.route('/editlisting')
def editlisting():
        return render_template('editlisting.html')

@app.route('/searchedlisting')
def searchedlisting():
        return render_template('searchedlisting.html')

@app.route('/alllistings')
def alllistings():
        return render_template('alllistings.html')



if __name__ == "__main__":
    app.run(debug=True)