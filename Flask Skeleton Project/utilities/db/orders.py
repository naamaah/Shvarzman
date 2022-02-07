from utilities.db.db_manager import dbManager
import datetime

#Bar

class Orders:
    @staticmethod
    def insert_order(order_id, is_delivery, user_email, order_cost):
        #date = date.strftime("%Y-%m-%d %H:%M:%S")
        date = datetime.datetime.now()
        return dbManager.commit(
            # f"INSERT INTO orders VALUES ('{order_id}, {date}, {is_delivery}, {user_email}, {order_cost}')")
            # f"INSERT INTO orders (order_id, order_DT, is_delivery, email, order_cost) VALUES ('{order_id}, {date}, {is_delivery}, {user_email}, {order_cost}')")
            "INSERT INTO orders (order_id, order_DT, is_delivery, email, order_cost) VALUES ('%s', '%s', '%s', '%s', '%s');" %(order_id, date, is_delivery, user_email, order_cost))

    @staticmethod
    def getOrderIds():
        return dbManager.fetch("SELECT order_id FROM orders")
