# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ProductSetRawMat(models.TransientModel):
    _name = 'product_set.raw.mat.wiz'
    _description = 'Components of a product set'

    sequence = fields.Integer(string='sequence', default=10)
    product_set_wizard_id = fields.Many2one('add.product_set.product', string='Product Set', required=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', string="Product")
    unit_quantity = fields.Float(string='Unit Quantity', default=1.0)
    quantity = fields.Float(string='Quantity', default=1.0)
    packing_list = fields.Float(string='Packing List')
    uom_id = fields.Many2one('uom.uom', string='Unit Of Measure', domain="[('category_id', '=', product_uom_category_id)]")
    product_uom_category_id = fields.Many2one(related='product_id.uom_id.category_id', readonly=True)
    display_type = fields.Selection([
        ('line_section', "Section"),
        ('line_note', "Note")], default=False, help="Technical field for UX purpose.")
    name = fields.Text(string="Name")
