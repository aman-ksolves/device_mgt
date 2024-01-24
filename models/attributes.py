from odoo import fields, models


class DeviceAttribute(models.Model):
    _name = 'device.attribute'

    name = fields.Char(string="attribute name")
    required = fields.Boolean(string="required")

    device_type_id = fields.Many2one('device.type', string="device type id")
    device_attribute_value_id = fields.One2many('device.attribute.value', 'device_attribute_id',
                                                string="device attribute id")


class DeviceAttributeValue(models.Model):
    _name = 'device.attribute.value'

    name = fields.Char(string="attribute value name")
    device_attribute_id = fields.Many2one('device.attribute', string="device attribute id")


class DeviceAttributeAssignment(models.Model):
    _name = 'device.attribute.assignment'

    device_id = fields.Many2one('device.device', string="device id")
    device_attribute_id = fields.Many2one('device.attribute', string="device attribute id")
    device_attribute_value_id = fields.Many2one('device.attribute.value', string="device attribute value id")
