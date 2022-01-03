from flask import Blueprint, render_template
from utilities.db.recipes import Recipes

# recipesPage blueprint definition
recipesPage = Blueprint('recipesPage', __name__,
                  static_folder='static',
                    static_url_path='/recipesPage',
                  template_folder='templates')


# Routes
@recipesPage.route('/recipesPage')
def index():
    recipes = Recipes.getAllRecipes()
    return render_template('recipesPage.html', recipes=recipes)
