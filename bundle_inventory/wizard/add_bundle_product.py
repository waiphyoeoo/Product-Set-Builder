# -*- coding: utf-8 -*-

from odoo import fields, models, api


class InventoryBundleRawMat(models.TransientModel):
    _inherit = 'add.bundle.product'

    @api.model
    def default_get(self, fields):
        """ Allow support of active_id / active_model
        to ease window action definitions, and be backward compatible. """
        result = super(InventoryBundleRawMat, self).default_get(fields)
        if self.env.context.get('active_model') == 'stock.picking':
            result['bundle_model'] = 'stock'
        if self.env.context.get('active_id') and self.env.context.get('active_model') == 'stock.picking':
            result['picking_id'] = self.env.context.get('active_id')
            
            
            sequence = self.env['stock.move'].search([('picking_id', '=', result['picking_id'])], order='sequence desc', limit=1)
            result['max_sequence'] = sequence
            
        return result

    picking_id = fields.Many2one('stock.picking', string="Stock Picking")

    @api.model_create_multi
    def create(self, values):
        """
        Add bundle components to the related
        """
        print("\n\n\n\n\n\n\n")
        print(values)
        print("\n\n\n\n\n\n\n")
        add_bundles = super(InventoryBundleRawMat, self).create(values)
        
        for add_bundle in add_bundles:
            if add_bundle.bundle_model == 'stock':
                
                
                for line in add_bundle.bundle_raw_mat_ids:
                    values = line.prepare_stock_move(add_bundle.picking_id.id)

                    stock_move = self.env['stock.move'].create(values)
                    # stock_move.onchange_product_id()
                    stock_move.write(values)
        return add_bundles
