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
    valuesDict=valuesForQuantity()
    print(valuesDict)
    if 'productId' in request.args:
        product_quantity = request.args['quantity']
        product_Id = request.args['productId']
        if product_quantity != '0':
            valuesDict[product_Id]=product_quantity
            new_product=Products.get_product_by_id(product_Id)
            new_product_in_shoppingCart = [new_product[0].product_id,new_product[0].product_name,new_product[0].product_price,new_product[0].product_picture,product_quantity]
            old_cart=deleteProductifAlreadyInCart(product_Id)
            old_cart.append(new_product_in_shoppingCart)
            session["shoppingCart"]=old_cart
    return render_template('productsPage.html', products=products, valuesDict=valuesDict)

# if id in cart - delete, else stay the same
def deleteProductifAlreadyInCart(product_Id):
    old_cart = session["shoppingCart"]
    count=0
    for product in old_cart:
        if product[0]==product_Id:
            del old_cart[count]
            break
        count=count+1
    new_Cart=old_cart
    return new_Cart

def valuesForQuantity():
    valuesList=Products.getAllProductsIDS()
    valuesDict={}
    for i in valuesList:
        valuesDict[i[0]]=0
    if session.get("shoppingCart"):
        old_cart=session["shoppingCart"]
        for p in old_cart:
            valuesDict[p[0]]=p[4]
    return valuesDict








# @shop.route('/shop', methods=['GET', 'POST'])
# def index():
#     if not session.get("cart"):
#         session["cart"] = {}
#     products = Products.get_all_products()
#     if request.method == "POST":
#         session["cart"][request.json["productId"]] = int(request.json["quantity"])
#     return render_template('shop.html', products=products, shopping_cart=session.get("cart"))

