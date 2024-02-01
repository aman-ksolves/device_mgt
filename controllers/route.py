from odoo import http


class MyModuleController(http.Controller):
    @http.route('/test', type='json', auth='user', website=True)
    def object(self, **kw):
        return http.request.render('device_mgt.device_assignment_tree_view', {
            # 'value': kw.get('value', 0),
        })
