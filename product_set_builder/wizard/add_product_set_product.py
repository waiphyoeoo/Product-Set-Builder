# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.tools import float_is_zero


class ProductSetRawMat(models.TransientModel):
    _name = 'add.product_set.product'
    _description = 'Add components of a product set'

    product_tmpl_id = fields.Many2one('product.template', string='Product Set', required=True, domain=[('is_a_product_set', '=', True)], ondelete='cascade')
    quantity = fields.Float(string="Quantity", default=1.0)
    product_set_raw_mat_ids = fields.One2many('product_set.raw.mat.wiz', 'product_set_wizard_id', string='Components')
    product_set_model = fields.Selection([('purchase', 'Purchase'), ('sale', 'Sale'),('stock', 'Stock')], string='Model', required=True)
    max_sequence = fields.Integer(string='Max Sequence')

    def _prepare_product_set_raw_mat(self):
        """
        Prepare a list of values for creating the component lines of the product_set.
        """
        self.ensure_one()
        values_list = []
        if not self.product_tmpl_id:
            return values_list
        for raw_mat in self.product_tmpl_id.product_set_raw_material_ids:
            values = raw_mat.prepare_raw_mat_wiz(quantity=self.quantity)
            values_list.append(values)
        return values_list

    @api.onchange('product_tmpl_id')
    def generate_components_lines(self):
        """
        Depending on the product chosen, fulfill the component lines of the product_set's wizard.
        """
        self.update({'product_set_raw_mat_ids': [(5, 0, 0)]})
        if not self.product_tmpl_id:
            return
        rounding = self.product_tmpl_id.uom_id.rounding
        if float_is_zero(self.quantity, precision_rounding=rounding):
            return
        values_list = self._prepare_product_set_raw_mat()
        create_values = [(0, 0, values) for values in values_list]
        self.update({'product_set_raw_mat_ids': create_values})

    @api.onchange('quantity')
    def update_components_qty(self):
        """
        Depending on the quantity of product_set, adapt the quantity of product_set's components.
        """
        if not self.product_tmpl_id:
            return
        rounding = self.product_tmpl_id.uom_id.rounding
        if float_is_zero(self.quantity, precision_rounding=rounding):
            return
        for raw_mat in self.product_set_raw_mat_ids:
            raw_mat.quantity = raw_mat.unit_quantity * self.quantity * raw_mat.packing_list
