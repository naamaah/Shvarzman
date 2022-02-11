from flask import Blueprint, render_template, redirect, url_for, session
from utilities.db.recipes import Recipes
import random

# homepage blueprint definition
homepage = Blueprint('homepage', __name__,
                     static_folder='static',
                     static_url_path='/homepage',
                     template_folder='templates')


# Routes
@homepage.route('/', defaults={'msg': 0})
@homepage.route('/<msg>')
def index(msg):
    # if msg = 0 : not from login -> no message
    # if msg = 1 : from logout
    # if msg = 2 : from login
    print(msg)
    print(type(msg))
    msg = int(msg)
    print(type(msg))
    if msg==0:
        url='/'
    else:
        url = '/'+str(msg)
    recipes = Recipes.getAllRecipes()
    size = len(recipes)
    recipe_id = random.randint(0, size - 1)
    recipe_name = recipes[recipe_id].recipe_name
    recipe_description = recipes[recipe_id].description
    recipe_pic = recipes[recipe_id].picture
    # print(recipe_name)
    # print(recipe_description)
    # print(recipe_pic)


    return render_template('homepage.html', recipe_name=recipe_name,
                           recipe_description=recipe_description,
                           recipe_pic=recipe_pic,
                           msg=msg, url=url)


@homepage.route('/homepage')
@homepage.route('/home')
def redirect_homepage():
    return redirect(url_for('homepage.index'))
