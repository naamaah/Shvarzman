from utilities.db.db_manager import dbManager


#Naama

class Products:
    @staticmethod
    def getAllProducts():
        return dbManager.fetch("SELECT * FROM products")

    @staticmethod
    def getAllProductsIDS():
        return dbManager.fetch("SELECT product_id FROM products")

    @staticmethod
    def get_product_by_id(product_id):
        return dbManager.fetch(f"SELECT * FROM products WHERE product_id='{product_id}'")
