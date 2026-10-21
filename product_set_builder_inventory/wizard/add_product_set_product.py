# -*- coding: utf-8 -*-

from odoo import fields, models, api


class InventoryProductSetRawMat(models.TransientModel):
    _inherit = 'add.product_set.product'

    @api.model
    def default_get(self, fields):
        """ Allow support of active_id / active_model
        to ease window action definitions, and be backward compatible. """
        result = super(InventoryProductSetRawMat, self).default_get(fields)
        if self.env.context.get('active_model') == 'stock.picking':
            result['product_set_model'] = 'stock'
        if self.env.context.get('active_id') and self.env.context.get('active_model') == 'stock.picking':
            result['picking_id'] = self.env.context.get('active_id')
            
            
            sequence = self.env['stock.move'].search([('picking_id', '=', result['picking_id'])], order='sequence desc', limit=1)
            result['max_sequence'] = sequence.sequence if sequence else 0
            
        return result

    picking_id = fields.Many2one('stock.picking', string="Stock Picking")

    @api.model_create_multi
    def create(self, values):
        """
        Add product_set components to the related
        """
        add_product_sets = super(InventoryProductSetRawMat, self).create(values)
        
        for add_product_set in add_product_sets:
            if add_product_set.product_set_model == 'stock':
                
                
                for line in add_product_set.product_set_raw_mat_ids:
                    values = line.prepare_stock_move(add_product_set.picking_id.id)

                    stock_move = self.env['stock.move'].create(values)
                    # stock_move.onchange_product_id()
                    stock_move.write(values)
        return add_product_sets
