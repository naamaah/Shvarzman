from utilities.db.db_manager import dbManager


class Recipes:
    @staticmethod
    def getAllRecipes():
        return dbManager.fetch("SELECT * FROM recipes")

    @staticmethod
    def getRecipeIds():
        return dbManager.fetch("SELECT recipe_id FROM recipes")