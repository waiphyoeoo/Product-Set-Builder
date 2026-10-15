# -*- coding: utf-8 -*-

from odoo import fields, models
from datetime import datetime, timedelta

class PurchaseBundleRawMatWiz(models.TransientModel):
    _inherit = 'bundle.raw.mat.wiz'

    def prepare_stock_move(self, picking_id):
        """
        Prepare a dictionary of values for creating a stock move
        """
        print("\n\n\n\n\n")
        print("vals--->",picking_id)
        print("\n\n\n\n\n\n\n")
        return {
            'company_id': 1,
            'date':datetime.today(),
            # 'location_dest_id': 1,
            # 'location_id': 2,
            'name':'xxxx',
            'procure_method':'make_to_stock',
            'sequence': self.bundle_wizard_id.max_sequence + self.sequence,
            'product_id': self.product_id.id if self.product_id else 1,
            'product_uom': self.uom_id.id if self.uom_id else 1,
            'product_uom_qty': self.quantity,
            'name': self.name,
            'price_unit': 0,
            'picking_id': picking_id
        }
