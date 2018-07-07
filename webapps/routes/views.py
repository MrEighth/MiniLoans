# -*- coding: utf-8 -*-
from flask import render_template
from webapps.routes import router


@router.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
