from flask import Blueprint, render_template, request, session

from pages.productsPage.productsPage import valuesForQuantity, deleteProductifAlreadyInCart
from pages.recipesPage.recipesPage import deleteProductifzeroQuantity
from utilities.db.orders import Orders
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
                if quantity_change_from_cart=='0':
                    del old_cart[count]
                    break
                else:
                    old_cart[count][4]=quantity_change_from_cart
                break
            count=count+1
        session["shoppingCart"] = old_cart

    if session.get("email"):
        valuesDict = valuesForQuantity()
        productsInOrderDict=createDictWithProductsOrder()
        if 'orderId' in request.args:  # if user add pro from prev order
            order_id = request.args['orderId']
            for k,v in productsInOrderDict.items():
                if int(order_id)==k:
                    print("inside the order")
                    for pro in v[1:]:
                        url = str(pro[0]) +'quantity'
                        print(url)
                        if url in request.args:
                            product_quantity = request.args[url]
                            if product_quantity!='0':
                                valuesDict[pro[0]] = product_quantity
                                new_product_in_shoppingCart = [pro[0], pro[1], pro[4], pro[2], product_quantity]
                                old_cart = deleteProductifAlreadyInCart(pro[0])
                                old_cart.append(new_product_in_shoppingCart)
                                session["shoppingCart"] = old_cart
                            else:
                                session["shoppingCart"]=deleteProductifzeroQuantity(pro[0])
                                valuesDict = valuesForQuantity()
        totalPrice = calToalPrict()
        return render_template('shopPage.html', totalPrice=totalPrice, productsInOrderDict=productsInOrderDict, valuesDict=valuesDict)
    totalPrice = calToalPrict()
    return render_template('shopPage.html',totalPrice=totalPrice)

def calToalPrict():
    sum = 0
    if session.get("shoppingCart"):
        old_cart = session["shoppingCart"]
        for product in old_cart:
            sum=sum+product[2]*float(product[4])
    return sum;

def createDictWithProductsOrder():
    ordersUser = Orders.get_User_orders_products(session['email'])
    orderIds = Orders.getAllUserOrders(session['email'])
    # create dict with user orders ids with a empty list
    productsInOrderDict = {}
    for i in orderIds:
        productsInOrderDict[i.order_id] = []
    for key in productsInOrderDict.keys(): #go over the new dict of specific user!
        productInOrder = []
        for i in ordersUser: #go over all products that in the user orders
            if (key == i.order_id): #specific order
                date = i.order_DT
                pro = Products.get_product_by_id(i.product_id)
                productInOrder.append([i.product_id, pro[0].product_name, pro[0].product_picture, i.quantity, pro[0].product_price])
        productInOrder.insert(0, date)
        productsInOrderDict[key] = productInOrder
    return productsInOrderDict




