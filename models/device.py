from odoo import _,fields, models


class Device(models.Model):
    _name = 'device.device'
    _description = 'Device'

    name = fields.Char(string='device name')
    shared = fields.Boolean(string='shared')
    device_type_id = fields.Many2one('device.type', string="device type id")
    device_brand_id = fields.Many2one('device.brand', string="device brand id")
    device_model_id = fields.Many2one('device.model', string="device model id")
    attribute_assignment_ids = fields.One2many('device.attribute.assignment', 'device_id',
                                               string="device assignment ids")


class DeviceModel(models.Model):
    _name = 'device.model'
    _description = 'Device model'

    name = fields.Char(string="device model name")
    device_type_id = fields.Many2one('device.type', string="device type id")
    device_brand_id = fields.Many2one('device.brand', string="device brand id")


class DeviceType(models.Model):
    _name = 'device.type'
    _description = 'Device model'

    name = fields.Char(string="device type name")
    code = fields.Char(string="code")
    sequence = fields.Char(string="Order Reference", readonly=True, default=lambda self: _('New'))
    device_attribute_ids = fields.One2many('device.attribute', 'device_type_id', string="device attribute ids")
    device_model_ids = fields.One2many('device.model', 'device_type_id', string="device model id")
    device_ids = fields.One2many('device.device', 'device_type_id', string="device_ids")

    def create(self,vals):
        vals['sequence'] = self.env['ir.sequence'].next_by_code('device.type') or _('New')
        return super().create(vals)


class DeviceBrand(models.Model):
    _name = 'device.brand'
    _description = 'Device brand'

    name = fields.Char(string="brand name")
    device_ids = fields.One2many('device.device', 'device_brand_id', string="device ids")
