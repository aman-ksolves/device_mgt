from odoo import fields, models


class Employee(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'

    device_assignment_ids = fields.One2many('device.assignment', 'employee_id', string="Device ids")


class DeviceAssignment(models.Model):
    _name = 'device.assignment'

    name = fields.Char(string="name")
    device_id = fields.Many2one('device.device', string="device id")
    employee_id = fields.Many2one('hr.employee', string="employee id")
    date_start = fields.Date(string="start date")
    date_expire = fields.Date(string="expire date")
    state = fields.Selection([('new', 'New'), ('draft', 'Draft'), ('approved', 'Approved'),
                              ('returned', 'Returned'), ('rejected', 'Rejected')], string="state")
