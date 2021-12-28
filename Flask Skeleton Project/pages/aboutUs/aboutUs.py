from flask import Blueprint, render_template

# aboutUsUs blueprint definition
aboutUs = Blueprint('aboutUs', __name__,
                  static_folder='static',
                    static_url_path='/aboutUs',
                  template_folder='templates')


# Routes
@aboutUs.route('/aboutUs')
def index():
    return render_template('aboutUs.html')
