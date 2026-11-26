# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Helpdesk Stock Account CE',
    'category': 'Services/Helpdesk',
    'summary': 'Helpdesk, Stock, Account',
    'depends': ['ce_helpdesk_stock', 'ce_helpdesk_account'],
    'data': [
        'wizard/account_move_reversal_views.xml',
    ],
    'auto_install': True,
    'author': 'Odoo S.A.',
    'license': 'OEEL-1',
}
