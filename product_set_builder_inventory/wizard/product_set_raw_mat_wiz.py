# -*- coding: utf-8 -*-

from odoo import fields, models
from datetime import datetime, timedelta

class InventoryProductSetRawMatWiz(models.TransientModel):
    _inherit = 'product_set.raw.mat.wiz'

    def prepare_stock_move(self, picking_id):
        """
        Prepare a dictionary of values for creating a stock move
        """
        return {
            'company_id': 1,
            'date':datetime.today(),
            # 'location_dest_id': 1,
            # 'location_id': 2,
            'procure_method':'make_to_stock',
            'sequence': self.product_set_wizard_id.max_sequence + self.sequence,
            'product_id': self.product_id.id if self.product_id else 1,
            'product_uom': self.uom_id.id if self.uom_id else 1,
            'product_uom_qty': self.quantity,
            'name': self.name,
            'price_unit': 0,
            'picking_id': picking_id
        }
