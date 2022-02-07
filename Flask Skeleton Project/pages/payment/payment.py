from flask import Blueprint, render_template, request, session, redirect, url_for
from pages.shopPage.shopPage import calToalPrict
from utilities.db.orders import Orders

# payment blueprint definition
payment = Blueprint('payment', __name__,
                  static_folder='static',
                    static_url_path='/payment',
                  template_folder='templates')

# Routes

@payment.route('/payment', methods=['GET', 'POST'])
def paymentPage():
    print("inside payment function")
    print(request.method)
    if request.method == 'POST':
        user_email = session["email"]
        order_cost=calToalPrict()
        is_delivery = request.form.get("isDelivery")
        order_id=findKey()
        result = Orders.insert_order(order_id, int(is_delivery), user_email, order_cost)
        print(result)
        print("back from insert")
        return redirect('/')
    return render_template('payment.html')

def findKey():
    order_ids=Orders.getOrderIds()
    print(order_ids)
    maxvalue=max(order_ids)
    print(maxvalue)
    new_order_id=(int(maxvalue.order_id))+1
    return new_order_id

