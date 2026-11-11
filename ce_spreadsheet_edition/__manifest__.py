# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Spreadsheet CE',
    'version': '1.0',
    'category': 'Productivity/Dashboard',
    'summary': 'Spreadsheet',
    'description': 'Spreadsheet',
    'depends': ['spreadsheet', 'mail', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/spreadsheet_views.xml',
        'data/mail_template_layouts.xml',
    ],
    'installable': True,
    'auto_install': True,
    'author': 'Odoo S.A.',
    'license': 'OEEL-1',
    'assets': {
        'spreadsheet.o_spreadsheet': [
            'ce_spreadsheet_edition/static/src/bundle/**/*.js',
            'ce_spreadsheet_edition/static/src/bundle/**/filter_editor_side_panel.xml',
            'ce_spreadsheet_edition/static/src/bundle/**/*.xml',
            ('remove', 'ce_spreadsheet_edition/static/src/bundle/pivot/pivot.xml'),
        ],
        'spreadsheet.assets_print': [
            'ce_spreadsheet_edition/static/src/print_assets/**/*',
        ],
        'web.assets_backend': [
            'ce_spreadsheet_edition/static/src/**/*.scss',
            ('remove', 'ce_spreadsheet_edition/static/src/**/*.dark.scss'),
            'ce_spreadsheet_edition/static/src/assets/**/*',
            ('remove', 'ce_spreadsheet_edition/static/src/assets/graph_view/**'),
            ('remove', 'ce_spreadsheet_edition/static/src/assets/pivot_view/**'),
        ],
        'web.assets_web_dark': [
            'ce_spreadsheet_edition/static/src/**/*.dark.scss',
        ],
        'web.assets_backend_lazy': [
            'ce_spreadsheet_edition/static/src/assets/graph_view/**',
            'ce_spreadsheet_edition/static/src/assets/pivot_view/**',
            'ce_spreadsheet_edition/static/src/bundle/pivot/pivot.xml',
        ],
        'web.assets_unit_tests': [
            'ce_spreadsheet_edition/static/tests/**/*',
        ],
    }
}
