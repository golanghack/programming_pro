#! /usr/bin/env python3 

"""Creating blueprint with flask blueprints."""

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors