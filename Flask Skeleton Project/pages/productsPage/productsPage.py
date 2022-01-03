from flask import Blueprint, render_template
from utilities.db.products import Products

# productsPage blueprint definition
productsPage = Blueprint('productsPage', __name__,
                  static_folder='static',
                  template_folder='templates')


# Routes
@productsPage.route('/productsPage')
def index():
    products=Products.get_all_products()
    return render_template('productsPage.html', products=products)
