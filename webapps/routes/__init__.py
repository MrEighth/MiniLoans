# -*- coding: utf-8 -*-
from flask import Blueprint


router = Blueprint('router', __name__)

from webapps.routes import views, errors

