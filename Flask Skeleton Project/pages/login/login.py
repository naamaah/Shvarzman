from flask import Blueprint, render_template, redirect, request, session
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

# @login.route('/get_user', methods=["POST"])
# def get_user_func():
#     # get the data
#     email = request.form["Email_Login"]
#     password = request.json["psw"]
#     # check if email exists
#     result = Users.get_user(email)
#     if not result:
#         return f"The mail {email} not exists. Try register instead/", 400
#     elif result[0].password == password:
#         session["user_id"] = result[0].id
#         session["email"] = result[0].email
#         session["full_name"] = result[0].full_name
#         session["is_logged_in"] = True
#         return render_template('settings.html')
#     else:
#         return "Incorrect password. Try again.", 400


@login.route('/sign_in', methods = ['POST'])
def sign_in_func():
    # get the data
    email = request.form['Email_Login']
    password = request.form['psw']
    result = Users.get_user(email)
    if not result: # the email does not exist
        return f"The mail {email} not exists. Try register instead/", 400
    elif result[0].password == password:
        if not session.get("shoppingCart"):
        #     # if 'shoppingCart' not in session:
            session["shoppingCart"] = []
        session["email"] = result[0].email
        session['first_name'] = result[0].first_name
        session['last_name'] = result[0].last_name
        session['phone_number'] = result[0].phone_number
        session['address'] = result[0].address
        session["is_logged_in"] = True
        return redirect('/homepage')
    else:
        return "Incorrect password. Try again.", 400


@login.route('/sign_up', methods = ['POST'])
def sign_up_func():
    # get the data
    email = request.form['emailSignUp']
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    password = request.form['psw1']
    phoneNumber = request.form['phoneNumber']
    address = request.form['address']
    # check if email exists
    result = Users.get_user(email)
    if result and len(result) >= 1:
        return "Registration failed"
    # insert to db
    else:
        if Users.insert_user(email, firstName, lastName, password, phoneNumber, address) > 0:
            # come back to home page
            if not session.get("shoppingCart"):
                session["shoppingCart"] = []
            session["email"] = email
            session['first_name'] = firstName
            session['last_name'] = lastName
            session['phone_number'] = phoneNumber
            session['address'] = address
            session["is_logged_in"] = True
            return redirect('/')
        else:
            return "Registration failed. Please try again.", 400


@login.route('/logout')
def logout_func():
    session["shoppingCart"] = ''
    session["email"] = ''
    session['first_name'] = ''
    session['last_name'] = ''
    session['phone_number'] = ''
    session['address'] = ''
    session["is_logged_in"] = ''
    # session.clear()
    return redirect('/homepage')
