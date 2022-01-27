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

# Routes

@tours.route('/tours', methods=['GET', 'POST'])
def reg_tour():
    check_list = [True, 0, True, False]
    tours_list_distinct = Tours.get_tours_dictinct()
    tour_list = Tours.get_all_tours()
    tour_dates = Tours.get_all_dates()
    user_tours = Users_tours.get_user_tours(session["email"])
    if request.method == 'POST':
        email = session["email"]
        tour_dt = request.form.get("tour date")
        num_of_tickets = request.form['numOfTickets']
        current_places_left = Tours.update_places_left(tour_dt, num_of_tickets)
        check_user_tour = Users_tours.get_user_specific_tour(email, tour_dt)
        if current_places_left < 0:
            check_list[0] = False
            check_list[1] = abs(current_places_left)
        elif len(check_user_tour) == 1:
            check_list[2] = False
        else:
            check_list[3] = True
            Users_tours.insert_user_tours(email, tour_dt, num_of_tickets)
    return render_template('tours.html', tours_list_distinct=tours_list_distinct, tour_list=tour_list,
                           tour_dates=tour_dates, check_list=check_list,
                           user_tours=user_tours)


@tours.route('/update_tour_order', methods=['GET', 'POST'])
def update_tour():
    email = session["email"]
    tour_dt = request.form.get("tour date for update")
    new_num_of_tickets = request.form['update_num_tickets']
    if request.method == 'POST':
        previous_num_of_tickets = int(Users_tours.get_user_specific_tour(email, tour_dt)[0][2])
        if request.form['submit_button'] == 'עדכן כמות כרטיסים':
            difference = int(new_num_of_tickets) -previous_num_of_tickets
            if Tours.update_places_left(tour_dt, difference) >= 0:
                Users_tours.update_num_of_tickets(email, tour_dt, new_num_of_tickets)
        if request.form['submit_button'] == 'בטל רישום לסיור':
            Tours.update_places_left(tour_dt,  -previous_num_of_tickets)
            Users_tours.delete_user_tour(email, tour_dt)
    return redirect(url_for('tours.reg_tour'))

#
# @tours.route('/check', methods=['GET', 'POST'])
# def tours_list():
#      tours_list = Tours.get_all_tours()
#      return jsonify(tours_list)
