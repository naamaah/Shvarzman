from flask import Blueprint, render_template, request, session

from pages.productsPage.productsPage import valuesForQuantity, deleteProductifAlreadyInCart
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
    valuesDict=valuesForQuantity()
    productsIDInRecDic={}
    for rec in recipes:
        products=res_pros.get_products_by_recipes_id(rec[0]) # all the products that in this recipe
        productsInrec=[]
        for pro in products: #go every product that in this recipe
            product = Products.get_product_by_id(pro[0]) #take all the product (before we had only id)
            productsInrec.append(product[0])
            #URL
            if 'recipeId' in request.args: # if there is recipe id in the url
                if request.args['recipeId']==rec[0]: # if this recipe id in the url
                    url=str(product[0].product_id)+'quantity'
                    if url in request.args:
                        product_quantity = request.args[url]
                        if product_quantity!='0':
                            valuesDict[product[0].product_id] = product_quantity
                            new_product_in_shoppingCart = [product[0].product_id, product[0].product_name,
                                               product[0].product_price, product[0].product_picture,
                                            product_quantity]
                            old_cart = deleteProductifAlreadyInCart(product[0].product_id)
                            old_cart.append(new_product_in_shoppingCart)
                            session["shoppingCart"] = old_cart
                        else:
                            session["shoppingCart"]=deleteProductifzeroQuantity(product[0].product_id)
                            valuesDict = valuesForQuantity()
        productsIDInRecDic[rec[0]]=productsInrec
    return render_template('recipesPage.html', recipes=recipes, productsIDInRecDic=productsIDInRecDic, valuesDict=valuesDict)


# if id in cart - delete, else stay the same
def deleteProductifzeroQuantity(product_Id):
    old_cart = session["shoppingCart"]
    count = 0
    for product in old_cart:
        if product[0] == product_Id:
            del old_cart[count]
            break
        count = count + 1
    new_Cart = old_cart
    return new_Cart