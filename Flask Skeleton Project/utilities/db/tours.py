from utilities.db.db_manager import dbManager
import pandas as pd

# Bar check

class Tours:
    @staticmethod
    def get_tour(tour_dt):
        return dbManager.fetch(f"SELECT * FROM tours WHERE tour_dt='{tour_dt}'")

    @staticmethod
    def get_all_tours():
        return dbManager.fetch("SELECT *  FROM tours")

    @staticmethod
    def get_tours_dictinct():
        return dbManager.fetch("SELECT distinct tour_name, description,ticket_price, picture FROM tours")

    @staticmethod
    def update_places_left(tour_dt, num_of_tickets):
        places_left = dbManager.fetch(f"SELECT places_left FROM tours WHERE tour_dt='{tour_dt}'")
        current_places_left = int(places_left[0][0]) - int(num_of_tickets)
        if current_places_left >= 0:
            dbManager.commit(f"UPDATE tours SET places_left='{current_places_left}' WHERE tour_dt='{tour_dt}'")
        return current_places_left

    @staticmethod
    def get_ordered_dates(email):
        return dbManager.fetch("SELECT tours.tour_dt, tours.tour_name FROM tours INNER JOIN users_tours"
                               f" ON tours.tour_dt=users_tours.tour_dt WHERE users_tours.email='{email}'")

    @staticmethod
    def get_all_dates():
        return dbManager.fetch("SELECT tour_dt, tour_name FROM tours")

