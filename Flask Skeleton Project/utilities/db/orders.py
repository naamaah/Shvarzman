from utilities.db.db_manager import dbManager
import datetime

#Bar

class Orders:
    @staticmethod
    def insert_order(order_id, is_delivery, user_email, order_cost):
        date = datetime.datetime.now()
        return dbManager.commit(
            # f"INSERT INTO orders VALUES ('{order_id}, {date}, {is_delivery}, {user_email}, {order_cost}')")
            # f"INSERT INTO orders (order_id, order_DT, is_delivery, email, order_cost) VALUES ('{order_id}, {date}, {is_delivery}, {user_email}, {order_cost}')")
            "INSERT INTO orders (order_id, order_DT, is_delivery, email, order_cost) VALUES ('%s', '%s', '%s', '%s', '%s');" %(order_id, date, is_delivery, user_email, order_cost))

    @staticmethod
    def getOrderIds():
        return dbManager.fetch("SELECT order_id FROM orders")

    @staticmethod
    def getAllUserOrders(user_email):
        return dbManager.fetch(f"SELECT * FROM orders WHERE email='{user_email}'")

    @staticmethod
    def get_User_orders_products(email):
        return dbManager.fetch("SELECT orders.order_id, orders.order_DT, order_products.product_id, order_products.quantity FROM orders INNER JOIN order_products"
                               f" ON orders.order_id=order_products.order_id WHERE orders.email='{email}'")


