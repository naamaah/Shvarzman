from flask import Blueprint, render_template, request
from utilities.db.products import Products

# shopPage blueprint definition
shopPage = Blueprint('shopPage', __name__,
                  static_folder='static',
                static_url_path='/shopPage',
                  template_folder='templates')


# Routes
@shopPage.route('/shopPage')
def index():
    products=Products.getAllProducts()
    return render_template('shopPage.html',products=products)
