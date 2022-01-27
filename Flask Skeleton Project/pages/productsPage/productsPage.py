from flask import Blueprint, render_template, session, request
from utilities.db.products import Products


# productsPage blueprint definition
productsPage = Blueprint('productsPage', __name__,
                  static_folder='static',
                static_url_path='/productsPage',
                  template_folder='templates')


# Routes
@productsPage.route('/productsPage', methods=['GET'])
def product():
    products = Products.getAllProducts()
    # if not session.get("shoppingCart"):
    #     session["shoppingCart"] = {}
    #product_id_Quantity='product_id={{ product.product_id}} quantity'
    if 'quantity' in request.args:
        new_product = request.args['quantity']
        # session["shoppingCart"].append(new_product)
        return render_template("productsPage.html", new_product=new_product,products=products)
    return render_template('productsPage.html', products=products)






# @shop.route('/shop', methods=['GET', 'POST'])
# def index():
#     if not session.get("cart"):
#         session["cart"] = {}
#     products = Products.get_all_products()
#     if request.method == "POST":
#         session["cart"][request.json["productId"]] = int(request.json["quantity"])
#     return render_template('shop.html', products=products, shopping_cart=session.get("cart"))

