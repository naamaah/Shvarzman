import pandas as pd
from flask import Blueprint, render_template, request

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
    check_list = [True, 0, True, True, True, False]
    tours_list = Tours.get_all_tours()
    tour_dates = Tours.get_all_dates()
    if request.method == 'POST':
        email = request.form['emailaddress']
        tour_dt = request.form.get("tour date")
        num_of_tickets = request.form['numOfTickets']
        current_places_left = Tours.update_places_left(tour_dt, num_of_tickets)
        if current_places_left < 0:
            check_list[0] = False
            check_list[1] = abs(current_places_left)
        check_user_email = Users.get_user(email)
        if len(check_user_email) != 1:
            check_list[2] = False
        check_tour_dt = Tours.get_tour(tour_dt)
        if check_tour_dt == []:
            check_list[3] = False
        check_user_tour = Users_tours.get_user_tours(email, tour_dt)
        if len(check_user_tour) == 1:
            Users_tours.update_user_tours(email, tour_dt, num_of_tickets)
            check_list[4] = False
        else:
            check_list[5] = True
            Users_tours.insert_user_tours(email, tour_dt, num_of_tickets)
    return render_template('tours.html', tours_list=tours_list, tour_dates=tour_dates, check_list=check_list)


# @tours.route('/tours', methods=['GET', 'POST'])
# def tours_list():
#     tours_list = Tours.get_all_tours()
#     return render_template('tours.html', tours_list=tours_list)


