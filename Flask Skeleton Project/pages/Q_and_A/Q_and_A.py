from flask import Blueprint, render_template

# Q_and_A blueprint definition
Q_and_A = Blueprint('Q_and_A', __name__,
                  static_folder='static',
                    static_url_path='/QA',
                  template_folder='templates')




# Routes
@Q_and_A.route('/QA')
def QAPage():
    return render_template('Q_and_A.html')
