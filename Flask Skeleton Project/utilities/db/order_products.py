from utilities.db.db_manager import dbManager

#Bar
#

class ShoppingCart:

    @staticmethod
    def insert_product_order(order_id, product_id, quantity):
        return dbManager.commit(
            f"INSERT INTO shopping_cart (product_id, order_id, quantity) VALUES ('{product_id}', '{order_id}', '{quantity}')")
