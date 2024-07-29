# -*- coding: utf-8 -*-
{
    'name': "Project Report",

    'summary': """
        Project Report""",

    'description': """
        Project Report
    """,

    'author': "HAK Technologies",
    'website': "http://www.HAK Technologies.com",
    'images':['static/description/icon.png'],

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'crm', 'project', 'product','project_enterprise'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'wizard/stock_wizard.xml',
        'report/stock_report.xml',
    ],

}
