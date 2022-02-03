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
    #if "email" in session:
    if not session.get("shoppingCart"):
    #if 'shoppingCart' not in session:
        session["shoppingCart"] = []
    if 'quantity' in request.args:
        product_quantity = request.args['quantity']
        product_Id = request.args['productId']
        new_product=Products.get_product_by_id(product_Id)
        new_product_in_shoppingCart = [new_product[0].product_id,new_product[0].product_name,new_product[0].product_price,new_product[0].product_picture,new_product[0].product_inv,product_quantity]
        session["shoppingCart"].append(new_product_in_shoppingCart)
        #session["shoppingCart"][new_product[0].product_id]=[new_product[0].product_name, new_product[0].product_price,new_product[0].product_picture, product_quantity]
        #return render_template("productsPage.html", product_quantity=product_quantity,product_Id=product_Id,new_product=new_product, products=products)
    return render_template('productsPage.html', products=products)








# @shop.route('/shop', methods=['GET', 'POST'])
# def index():
#     if not session.get("cart"):
#         session["cart"] = {}
#     products = Products.get_all_products()
#     if request.method == "POST":
#         session["cart"][request.json["productId"]] = int(request.json["quantity"])
#     return render_template('shop.html', products=products, shopping_cart=session.get("cart"))

