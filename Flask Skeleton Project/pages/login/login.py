from flask import Blueprint, render_template, redirect, request, session, url_for
from utilities.db.db_manager import dbManager
from utilities.db.users import Users

# login blueprint definition
login = Blueprint('login', __name__,
                  static_folder='static',
                  static_url_path='/login',
                  template_folder='templates')


# Routes
@login.route('/login')
def index():
    return render_template('login.html')


@login.route('/sign_in', methods=['POST'])
def sign_in_func():
    # get the data
    email = request.form['Email_Login']
    password = request.form['psw']
    if (email != "" and password != ""):
        result = Users.get_user(email)
        if not result:  # the email does not exist
            msg = "  כתובת המייל " + email + " לא קיימת. נסה להירשם   "
            return render_template('/login.html', msg=msg)
        elif result[0].password == password:  # the email exists & correct password
            if not session.get("shoppingCart"):
                session["shoppingCart"] = []
            session["email"] = result[0].email
            session['first_name'] = result[0].first_name
            session['last_name'] = result[0].last_name
            session['phone_number'] = result[0].phone_number
            session['address'] = result[0].address
            session["is_logged_in"] = True
            return redirect(url_for('homepage.index', msg=2))
            # return render_template('/homepage.html', firstLog=True)
        else:  # the email exists & wrong password
            msg = "סיסמא לא נכונה, בבקשה נסה שוב"
            return render_template('/login.html', msg=msg)
    else:
        msg = "נסיון התחברות שגוי, בבקשה נסה שוב"
        return render_template('/login.html', msg=msg)


@login.route('/sign_up', methods=['POST'])
def sign_up_func():
    # get the data
    email = request.form['emailSignUp']
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    password = request.form['psw1']
    phoneNumber = request.form['phoneNumber']
    address = request.form['address']
    if (email != ""
            and firstName != ""
            and lastName != ""
            and password != ""
            and phoneNumber != ""
            and address != ""):
        # check if email exists
        result = Users.get_user(email)
        if result and len(result) >= 1:  # the email already exists
            msg = "  כתובת המייל " + email + " קיימת. נסה להתחבר   "
            return render_template('/login.html', msg=msg)
        # return "Registration failed"
        else:  # new user, insert to db
            # come back to home page
            if Users.insert_user(email, firstName, lastName, password, phoneNumber, address) > 0:
                if not session.get("shoppingCart"):
                    session["shoppingCart"] = []
                session["email"] = email
                session['first_name'] = firstName
                session['last_name'] = lastName
                session['phone_number'] = phoneNumber
                session['address'] = address
                session["is_logged_in"] = True
                return redirect(url_for('homepage.index', msg=2))
    else:
        msg = "התחברות נכשלה, נסה שוב"
        return render_template('/login.html', msg=msg)
        # return "Registration failed. Please try again.", 400


@login.route('/logout')
def logout_func():
    session["shoppingCart"] = ''
    session["email"] = ''
    session['first_name'] = ''
    session['last_name'] = ''
    session['phone_number'] = ''
    session['address'] = ''
    session["is_logged_in"] = ''
    return redirect(url_for('homepage.index', msg=1))
    # return render_template('/', logout=True)
