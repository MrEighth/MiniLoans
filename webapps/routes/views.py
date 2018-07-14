# -*- coding: utf-8 -*-
from flask import render_template
from webapps.routes import router


@router.route('/', methods=['GET', 'POST'])
def index():
    user_info = {
        'id': '***5922',
        'nickname': 'facefaces',
        'credit_score': '753',
        'loan_ceiling': '8000',
        'loan_rest': '3000',
        'repay_date': '7月10日',
        'month_repay': '1024'
    }
    return render_template('index.html', title='微贷平台', user_info=user_info)
