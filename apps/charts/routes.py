# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.charts import blueprint
from flask import render_template
from apps.models import Product
from apps import config

@blueprint.route('/charts')
def charts():
    products = [{'name': product.name, 'price': product.price} for product in Product.get_list()]
    context = {
        'site_name': config.Config.SITE_NAME,
        'routes': config.Config.DYNAMIC_DATATB.keys(),
        'page_title': 'Charts',
        }
    
    return render_template('charts/index.html', segment='charts', products=products, **context)
