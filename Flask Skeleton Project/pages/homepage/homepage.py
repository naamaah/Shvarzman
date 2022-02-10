from flask import Blueprint, render_template, redirect, url_for
from utilities.db.recipes import Recipes
import random


# homepage blueprint definition
homepage = Blueprint('homepage', __name__,
                     static_folder='static',
                     static_url_path='/homepage',
                     template_folder='templates')


# Routes
@homepage.route('/')
def index():
    recipes = Recipes.getAllRecipes()
    size = len(recipes)
    print(size)
    recipe_id = random.randint(0,size-1)
    print(recipe_id)
    recipe_name = recipes[recipe_id].recipe_name
    recipe_description = recipes[recipe_id].description
    recipe_pic = recipes[recipe_id].picture
    print(recipe_name)
    print(recipe_description)
    print(recipe_pic)
    return render_template('homepage.html',recipe_name = recipe_name,
                           recipe_description = recipe_description,
                           recipe_pic = recipe_pic)

@homepage.route('/homepage', defaults={'firstLog': False})
@homepage.route('/homepage')
@homepage.route('/home')
def redirect_homepage():
    return redirect(url_for('homepage.index'))
