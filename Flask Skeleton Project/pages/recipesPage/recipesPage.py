from flask import Blueprint, render_template
from utilities.db.recipes import Recipes
from utilities.db.recipe_products import res_pros
from utilities.db.products import Products

# recipesPage blueprint definition
recipesPage = Blueprint('recipesPage', __name__,
                  static_folder='static',
                    static_url_path='/recipesPage',
                  template_folder='templates')


# Routes
@recipesPage.route('/recipesPage')
def index():
    recipes = Recipes.getAllRecipes()
    productsIDInRec=res_pros.get_All_products() #only products ids
    print(productsIDInRec)
    productsInrec=[]
    for i in productsIDInRec[0]:
        product=Products.get_product_by_id(i)
        productsInrec.append(product[0])
    print(len(productsInrec))
    return render_template('recipesPage.html', recipes=recipes, productsInrec=productsInrec)
