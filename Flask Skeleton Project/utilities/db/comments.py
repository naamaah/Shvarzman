from utilities.db.db_manager import dbManager
import datetime


# Shaked

class Comments:
    @staticmethod
    def insert_comment(email, first_name, last_name, phone_number, text):
        comment_dt = datetime.datetime.now()
        return dbManager.commit(
            "INSERT INTO comments (comment_dt, email, first_name, last_name, phone_number, text) VALUES ('%s', '%s', '%s', '%s', '%s','%s');" % (
                comment_dt, email, first_name, last_name, phone_number, text))
