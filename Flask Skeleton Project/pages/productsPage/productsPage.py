from flask import Blueprint, render_template, session, request
from utilities.db.products import Products


# productsPage blueprint definition
productsPage = Blueprint('productsPage', __name__,
                  static_folder='static',
                static_url_path='/productsPage',
                  template_folder='templates')


# Routes
@productsPage.route('/productsPage', methods=['GET', 'POST'])
def index():
    if not session.get("shpingCart"):
        session["shpingCart"] = {}
    # if request.method == "POST":
    #     session["cart"][request.json["productId"]] = int(request.json["quantity"])
    products=Products.getAllProducts()
    return render_template('productsPage.html', products=products)


# @shop.route('/shop', methods=['GET', 'POST'])
# def index():
#     if not session.get("cart"):
#         session["cart"] = {}
#     products = Products.get_all_products()
#     if request.method == "POST":
#         session["cart"][request.json["productId"]] = int(request.json["quantity"])
#     return render_template('shop.html', products=products, shopping_cart=session.get("cart"))

