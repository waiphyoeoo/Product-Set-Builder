# -*- coding: utf-8 -*-

from odoo import fields, models, api


class PurchaseProductSetRawMat(models.TransientModel):
    _inherit = 'add.product_set.product'

    @api.model
    def default_get(self, fields):

        """ Allow support of active_id / active_model
        to ease window action definitions, and be backward compatible. """
        result = super(PurchaseProductSetRawMat, self).default_get(fields)
        if self.env.context.get('active_model') == 'purchase.order':
            result['product_set_model'] = 'purchase'
        if self.env.context.get('active_id') and self.env.context.get('active_model') == 'purchase.order':
            result['purchase_order_id'] = self.env.context.get('active_id')
            sequence = self.env['purchase.order.line'].search([('order_id', '=', self.env.context.get('active_id'))], order='sequence desc', limit=1)
            result['max_sequence'] = sequence.sequence if sequence else 0
        return result

    purchase_order_id = fields.Many2one('purchase.order', string="Purchase Order")

    @api.model_create_multi
    def create(self, values):
        """
        Add product_set components to the related purchase order
        """
        add_product_sets = super(PurchaseProductSetRawMat, self).create(values)
        for add_product_set in add_product_sets:
            if add_product_set.product_set_model == 'purchase':
                for line in add_product_set.product_set_raw_mat_ids:
                    values = line.prepare_purchase_order_line(add_product_set.purchase_order_id)
                    po_line = self.env['purchase.order.line'].create(values)
                    po_line.onchange_product_id()
                    po_line.write(values)
        return add_product_sets
