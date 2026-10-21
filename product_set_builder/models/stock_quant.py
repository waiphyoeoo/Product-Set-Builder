from odoo import fields, models, api


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    product_set_id = fields.Many2one('product.template', string='Product Set', store=True,
                                readonly=False, related='product_id.product_set_id')


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    product_set_id = fields.Many2one('product.template', string='Product Set', store=True,
                                readonly=False, related='product_id.product_set_id')


class StockMove(models.Model):
    _inherit = 'stock.move'

    product_set_id = fields.Many2one('product.template', string='Product Set', store=True,
                                readonly=False, related='product_id.product_set_id')

class StockLayerValuation(models.Model):
    _inherit = 'stock.valuation.layer'

    product_set_id = fields.Many2one('product.template', string='Product Set', store=True,
                                readonly=False, related='product_id.product_set_id')
