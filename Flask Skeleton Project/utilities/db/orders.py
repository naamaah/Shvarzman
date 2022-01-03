from utilities.db.db_manager import dbManager

#Bar

class Orders:
    @staticmethod
    def insert_order(payer_id, order_cost, date):
        date = date.strftime("%Y-%m-%d %H:%M:%S")
        insertOrder = dbManager.commit(
            f"INSERT INTO orders (payer_id, order_cost, date) VALUES ({payer_id}, {order_cost}, '{date}')")
        if insertOrder != 1:
            raise Exception(f"{insertOrder} rows was affected by the query")

        orders = dbManager.fetch(
            f"SELECT * FROM orders WHERE payer_id={payer_id} AND order_cost={order_cost} AND date='{date}'")
        if not orders:
            raise Exception("Exception occurred while selecting the order from the DB")

        return orders[0].id
