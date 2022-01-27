from utilities.db.db_manager import dbManager

#Bar check

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
        result = dbManager.fetch(f"SELECT places_left FROM tours WHERE tour_dt='{tour_dt}'")
        for tour in result:
            current_places_left = int(tour.places_left) - int(num_of_tickets)
        if current_places_left >= 0:
            dbManager.commit(f"UPDATE tours SET places_left='{current_places_left}' WHERE tour_dt='{tour_dt}'")
        return current_places_left


    @staticmethod
    def get_all_dates():
        return dbManager.fetch("SELECT tour_dt FROM tours")





