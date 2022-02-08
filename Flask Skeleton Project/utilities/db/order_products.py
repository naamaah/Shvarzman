from utilities.db.db_manager import dbManager

#Bar
#

class ShoppingCart:
    @staticmethod
    def insert_product_order(order_id, product_id, quantity):
        return dbManager.commit(
            # f"INSERT INTO order_products (order_id, product_id, quantity) VALUES (''{order_id}', {product_id}',  '{quantity}')")
            "INSERT INTO order_products (order_id, product_id, quantity) VALUES ('%s', '%s', '%s');" % (order_id, product_id, quantity))
