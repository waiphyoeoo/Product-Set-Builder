from odoo import fields, models, api


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    bundle_id = fields.Many2one('product.template', string='Bundle', store=True,
                                readonly=False, related='product_id.bundle_id')


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    bundle_id = fields.Many2one('product.template', string='Bundle', store=True,
                                readonly=False, related='product_id.bundle_id')


class StockMove(models.Model):
    _inherit = 'stock.move'

    bundle_id = fields.Many2one('product.template', string='Bundle', store=True,
                                readonly=False, related='product_id.bundle_id')

class StockLayerValuation(models.Model):
    _inherit = 'stock.valuation.layer'

    bundle_id = fields.Many2one('product.template', string='Bundle', store=True,
                                readonly=False, related='product_id.bundle_id')
