from utilities.db.db_manager import dbManager

#omri
#login - forget password - u have an example.
#signUp

class Users:
    @staticmethod
    def get_user(email):
        return dbManager.fetch(f"SELECT * FROM users WHERE email='{email}'")

    @staticmethod
    def insert_user(email, firstName, lastName, password, phoneNumber, address):
        return dbManager.commit(
            f"INSERT INTO users (email, first_name, last_name, password, phone_number, address) VALUES ('{email}', '{firstName}', '{lastName}', '{password}', '{phoneNumber}', '{address}')")

    @staticmethod
    def update_password(user_id, password):
        return dbManager.commit(f"UPDATE users SET password='{password}' WHERE id={user_id}")

    @staticmethod
    def delete_user(email):
        return dbManager.commit(f"DELETE FROM users WHERE email='{email}'")

