# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Website Helpdesk CE',
    'category': 'Services/Helpdesk',
    'sequence': 57,
    'summary': 'Bridge module for helpdesk modules using the website.',
    'description': 'Bridge module for helpdesk modules using the website.',
    'depends': [
        'ce_helpdesk',
        'website',
    ],
    'data': [
        'data/helpdesk_data.xml',
        'views/helpdesk_views.xml',
        'views/helpdesk_templates.xml',
        'security/website_helpdesk_security.xml',
    ],
    'auto_install': True,
    'author': 'Odoo S.A.',
    'license': 'OEEL-1',
    'post_init_hook': '_configure_teams',
    'assets': {
        'web.assets_frontend': [
            'ce_website_helpdesk/static/**/*',
            ('remove', 'ce_website_helpdesk/static/src/js/website_helpdesk_form_editor.js'),
            ('remove', 'ce_website_helpdesk/static/src/js/website_helpdesk_edit_menu.js'),
            ('remove', 'ce_website_helpdesk/static/tests/tours/**/*'),
        ],
        'website.website_builder_assets': [  # Should use website.website_builder
            'ce_website_helpdesk/static/src/js/website_helpdesk_form_editor.js',
        ],
        'website.assets_editor': [
            'ce_website_helpdesk/static/src/js/website_helpdesk_edit_menu.js',
        ],
        'web.assets_tests': [
            'ce_website_helpdesk/static/tests/tours/**/*',
        ],
    }
}
