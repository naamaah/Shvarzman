from flask import Blueprint, render_template, request, session
from utilities.db.products import Products

# shopPage blueprint definition
shopPage = Blueprint('shopPage', __name__,
                  static_folder='static',
                static_url_path='/shopPage',
                  template_folder='templates')


# Routes
@shopPage.route('/shopPage')
def index():
    if 'deleteId' in request.args:  # if there delete item in url
        product_id_delete_from_cart = request.args['deleteId']
        old_cart = session["shoppingCart"]
        count=0
        for product in old_cart:
            if product[0]==product_id_delete_from_cart:
                del old_cart[count]
                break
            count=count+1
        session["shoppingCart"] = old_cart
    if 'changeId' in request.args:  # if there change in item quantity in url
        product_id_change_from_cart = request.args['changeId']
        quantity_change_from_cart = request.args['quantity']
        print(quantity_change_from_cart)
        old_cart = session["shoppingCart"]
        count=0
        for product in old_cart:
            if product[0]==product_id_change_from_cart:
                old_cart[count][5]=quantity_change_from_cart
                break
            count=count+1
        session["shoppingCart"] = old_cart
    totalPrice=calToalPrict()
    return render_template('shopPage.html',totalPrice=totalPrice)

def calToalPrict():
    sum = 0
    if session.get("shoppingCart"):
        old_cart = session["shoppingCart"]
        for product in old_cart:
            sum=sum+product[2]*float(product[5])
    return sum;



