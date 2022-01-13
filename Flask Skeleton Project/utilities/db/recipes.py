from utilities.db.db_manager import dbManager


class Recipes:
    @staticmethod
    def getAllRecipes():
        return dbManager.fetch("SELECT * FROM recipes")