# -*- coding: utf-8 -*-

from odoo import fields, models


class PurchaseBundleRawMatWiz(models.TransientModel):
    _inherit = 'bundle.raw.mat.wiz'

    def prepare_purchase_order_line(self, order_id):
        """
        Prepare a dictionary of values for creating a purchase.order.line record.
        """
        return {
            'sequence': self.bundle_wizard_id.max_sequence + self.sequence,
            'product_id': self.product_id.id if self.product_id else False,
            'product_qty': self.quantity if not self.display_type else 0.0,
            'product_uom': self.uom_id.id if self.uom_id else False,
            'display_type': self.display_type,
            'name': self.name,
            'price_unit': 0,
            'order_id': order_id.id
        }
