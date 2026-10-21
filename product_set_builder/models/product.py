from odoo import models, fields, api
from odoo.addons.l10n_ch import init_settings


class Product(models.Model):
    _inherit = 'product.product'
    # if is_a_product_set or product_set_raw_material_ids --> !product_set_id

    product_set_id = fields.Many2one('product.template', string='Product Set', compute="_compute_product_set_id",store=True,readonly=False)
    description = fields.Char(related='product_tmpl_id.description',string='Description')

    def _compute_product_set_id(self):
        for product in self:
            # ဘာမှမရှိရင် အရင်ဆုံး False ပေးထားမယ်
            product.product_set_id = False
            # ၎င်း product ကို သုံးထားတဲ့ Raw Material ရှိမရှိ ရှာမယ်
            BRM = self.env['product_set.raw.mat'].search([('product_id', '=', product.id)], limit=1)
            if BRM:
                product.product_set_id = BRM.product_tmpl_id.id
