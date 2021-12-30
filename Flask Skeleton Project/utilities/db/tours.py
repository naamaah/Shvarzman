from utilities.db.db_manager import dbManager

#Omri

class CookingClass:

    @staticmethod
    def insert_cooking_class(email, first_name, last_name, phone_number, group_size):
        return dbManager.commit(f"INSERT INTO cooking_class (email, first_name, last_name, phone_number, group_size) "
                                f"VALUES ('{email}', '{first_name}', '{last_name}', '{phone_number}', {group_size})")
