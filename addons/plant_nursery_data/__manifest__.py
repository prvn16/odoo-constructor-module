# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Plant Nursery Data',
    'version': '1.0',
    'category': 'Hidden',
    'summary': 'Data for Plant Nursery',
    'depends': ['plant_nursery'],
    'data': [
        'data/mail_configuration_data.xml',
        'data/base_data.xml',
        'data/mail_configuration_data.xml',
        'data/customer_data.xml',
        'data/plant_data.xml',
        'data/order_data.xml',
    ],
    'demo': [
    ],
    'css': [],
    'auto_install': False,
    'application': False,
}
