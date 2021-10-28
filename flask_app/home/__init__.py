from flask import Blueprint

# Blueprint configuration
# https://exploreflask.com/en/latest/blueprints.html

home_blueprint = Blueprint(
    'home_blueprint',
     __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/home/static'
)

from . import views