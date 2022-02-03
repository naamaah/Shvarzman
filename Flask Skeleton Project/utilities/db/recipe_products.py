from utilities.db.db_manager import dbManager

#Naama

class res_pros:
    @staticmethod
    def get_All_products():
        return dbManager.fetch(f"SELECT product_id FROM recipe_products")

    @staticmethod
    def get_products_by_recipes_id(recipe_id):
        return dbManager.fetch(f"SELECT * FROM recipe_products WHERE recipe_id='{recipe_id}'")
