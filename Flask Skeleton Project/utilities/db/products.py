from utilities.db.db_manager import dbManager

#Naama

class Products:
    @staticmethod
    def getAllProducts():
        return dbManager.fetch("SELECT * FROM products")

    @staticmethod
    def get_products_by_ids(product_ids):
        if not isinstance(product_ids, list):
            product_ids = [product_ids]
        return dbManager.fetch(
            f"SELECT * FROM products WHERE id IN {f'({product_ids[0]})' if len(product_ids) == 1 else tuple(product_ids)}")
