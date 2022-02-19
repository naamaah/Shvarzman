from flask import Blueprint, render_template, request, session, redirect, url_for
from utilities.db.comments import Comments
from datetime import datetime
from utilities.db.users import Users

# contactUs blueprint definition
contactUs = Blueprint('contactUs', __name__,
                      static_folder='static',
                      static_url_path='/contactUs',
                      template_folder='templates')


# Routes
@contactUs.route('/contactUs')
def index():
    return render_template('contactUs.html')


@contactUs.route('/contactForm', methods=['POST'])
def contactForm():
    # get the data
    print('help')
    email = request.form['emailaddress']
    first_name = request.form['firstname']
    last_name = request.form['lastname']
    phone_number = request.form['phonenumber']
    text = request.form['subject']
    if ( email != ""
            and first_name != ""
            and last_name != ""
            and phone_number != ""):
    # insert to comment table
            result =  Comments.insert_comment(email, first_name, last_name, phone_number, text) #Users.insert_user(email, first_name, last_name, 'fdfdfd', phone_number, text)
            return redirect('/homepage')
