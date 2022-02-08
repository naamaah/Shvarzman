import pandas as pd
from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify
from utilities.db.users_tours import Users_tours
from utilities.db.users import Users
from utilities.db.tours import Tours

# tours blueprint definition
tours = Blueprint('tours', __name__,
                  static_folder='static',
                  static_url_path='/tours',
                  template_folder='templates')


def not_ordered_dates_list(email):
    all_tours = pd.DataFrame(Tours.get_all_dates())
    ordered_tours = pd.DataFrame(Tours.get_ordered_dates(email))
    if not ordered_tours.empty:
        not_ordered_dates = all_tours[all_tours.tour_dt.isin(ordered_tours.tour_dt) == False]
        not_ordered_dates_not_null = not_ordered_dates.loc[not_ordered_dates['tour_dt'].notnull()]
        return not_ordered_dates_not_null
    else:
        return all_tours


# Routes
@tours.route('/tours', defaults={'message': ""})
@tours.route('/tours/<message>', methods=['GET'])
def tour_page(message):
    tours_list_distinct = Tours.get_tours_dictinct()
    tour_list = Tours.get_all_tours()
    if session.get("email"):
        tour_dates = not_ordered_dates_list(session["email"])
        user_tours = Tours.get_ordered_dates(session["email"])
    else:
        tour_dates= ''
        user_tours= ''
    return render_template('tours.html', tours_list_distinct=tours_list_distinct, tour_list=tour_list,
                           tour_dates=tour_dates, user_tours=user_tours, message=message)



@tours.route('/tourOrder', methods=['GET'])
def order_tour():
    message=''
    if 'tourDate' in request.args:
        email = session["email"]
        tour_dt = request.args["tourDate"]
        num_of_tickets = request.args['numOfTickets']
        current_places_left = Tours.update_places_left(tour_dt, num_of_tickets)
        tour_name = Tours.get_tour_name(tour_dt)[0][0]
        if current_places_left < 0:
            message = " לצערנו חסרים " + str(abs(current_places_left))+ " מקומות ל" +str(tour_name)+  " בתאריך המבוקש, אנא הירשם מחדש עם כמות כרטיסים תקינה"
        else:
            message = "הרשמה ל" +str(tour_name) + " בוצעה בהצלחה, ניפגש בקרוב (:"
            Users_tours.insert_user_tours(email, tour_dt, num_of_tickets)
    return redirect(url_for('tours.tour_page',  message=message))


@tours.route('/update_tour_order', methods=['GET'])
def update_tour():
    message=''
    if 'tourDateForUpdate' in request.args:
        email = session["email"]
        tour_dt = request.args["tourDateForUpdate"]
        new_num_of_tickets = request.args['updateNumTickets']
        previous_num_of_tickets = int(Users_tours.get_user_specific_tour(email, tour_dt)[0][2])
        tour_name = Tours.get_tour_name(tour_dt)[0][0]
        if request.args['submit_button'] == 'עדכן כמות כרטיסים':
            difference = int(new_num_of_tickets) - previous_num_of_tickets
            current_places_left = Tours.update_places_left(tour_dt, difference)
            if Tours.update_places_left(tour_dt, difference) >= 0:
                Users_tours.update_num_of_tickets(email, tour_dt, new_num_of_tickets)
                message = "כמות הכרטיסים ל" + str(tour_name)+ " עודכנה ל-" + str(new_num_of_tickets) + " כרטיסים"
            else:
                message = " לצערנו חסרים " + str(abs(current_places_left))+ " מקומות ל" +str(tour_name)+  " בתאריך המבוקש, לכן לא ניתן לבצע עדכון להזמנה"
        if request.args['submit_button'] == 'בטל רישום לסיור':
            Tours.update_places_left(tour_dt, -previous_num_of_tickets)
            Users_tours.delete_user_tour(email, tour_dt)
            message = "ביטול הזמנה ל" +  str(tour_name)+ " בוצע בהצלחה"
        return redirect(url_for('tours.tour_page', message=message))