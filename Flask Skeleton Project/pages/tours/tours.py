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
@tours.route('/tours', defaults={'order_check_list': []})
@tours.route('/tours/<order_check_list>', methods=['GET'])
def tour_page(order_check_list):
    print(order_check_list)
    tours_list_distinct = Tours.get_tours_dictinct()
    tour_list = Tours.get_all_tours()
    if session.get("email"):
        tour_dates = not_ordered_dates_list(session["email"])
        user_tours = Tours.get_ordered_dates(session["email"])
    else:
        tour_dates= ''
        user_tours= ''
    return render_template('tours.html', tours_list_distinct=tours_list_distinct, tour_list=tour_list,
                           tour_dates=tour_dates, user_tours=user_tours,order_check_list=order_check_list)



@tours.route('/tourOrder', methods=['GET'])
def order_tour():
    order_check_list = [True, 0, False, False, False]
    if 'tourDate' in request.args:
        email = session["email"]
        tour_dt = request.args["tourDate"]
        num_of_tickets = request.args['numOfTickets']
        current_places_left = Tours.update_places_left(tour_dt, num_of_tickets)
        check_user_tour = Users_tours.get_user_specific_tour(email, tour_dt)
        if current_places_left < 0:
            order_check_list[0] = False
            order_check_list[1] = abs(current_places_left)
        else:
            order_check_list[2] = True
            Users_tours.insert_user_tours(email, tour_dt, num_of_tickets)
    return redirect(url_for('tours.tour_page',order_check_list=order_check_list))


@tours.route('/update_tour_order', methods=['GET'])
def update_tour():
    order_check_list = [True, 0, False, False, False]
    if 'tourDateForUpdate' in request.args:
        email = session["email"]
        tour_dt = request.args["tourDateForUpdate"]
        new_num_of_tickets = request.args['updateNumTickets']
        previous_num_of_tickets = int(Users_tours.get_user_specific_tour(email, tour_dt)[0][2])
        if request.args['submit_button'] == 'עדכן כמות כרטיסים':
            difference = int(new_num_of_tickets) - previous_num_of_tickets
            if Tours.update_places_left(tour_dt, difference) >= 0:
                Users_tours.update_num_of_tickets(email, tour_dt, new_num_of_tickets)
                order_check_list[3]=True
        if request.args['submit_button'] == 'בטל רישום לסיור':
            Tours.update_places_left(tour_dt, -previous_num_of_tickets)
            Users_tours.delete_user_tour(email, tour_dt)
            order_check_list[4] = True
        return redirect(url_for('tours.tour_page',order_check_list=order_check_list))