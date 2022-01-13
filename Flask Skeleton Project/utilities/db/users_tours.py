from utilities.db.db_manager import dbManager

#bar

class Users_tours:

    @staticmethod
    def insert_user_tours(email, tour_dt, num_of_tickets):
        return dbManager.commit(f"INSERT INTO users_tours (email, tour_dt, num_of_tickets) "
                                f"VALUES ('{email}', '{tour_dt}', '{num_of_tickets}')")

    @staticmethod
    def get_user_tours(email, tour_dt):
        return dbManager.fetch(f"SELECT * FROM users_tours WHERE email='{email}' and tour_dt='{tour_dt}'")

    @staticmethod
    def update_user_tours(email, tour_dt, num_of_tickets):
        return dbManager.commit(f"UPDATE users_tours SET num_of_tickets='{num_of_tickets}' WHERE email='{email}'"
                                f" and tour_dt='{tour_dt}'")





