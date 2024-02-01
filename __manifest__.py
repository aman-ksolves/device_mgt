{
    'name': 'Device Management',
    'description': 'Device management system',
    'author': 'Aman',
    'version': '1.0',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_view_inherited.xml',
        'views/device_view.xml',
        'views/device_model_view.xml',
        'views/device_assignment.xml',
        'views/device_brand_view.xml',
        'views/device_type_sequence.xml',
        'views/device_type_view.xml',
        'views/device_attribute_view.xml',
        'views/device_attribute_value_view.xml',
        'views/device_attribute_assignment_view.xml',
        'views/menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'device_mgt/static/src/xml/tree_view.xml',
            'device_mgt/static/src/js/tree_button.js',
        ],

    },
}
