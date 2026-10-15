from odoo import models, fields, api
from odoo.addons.l10n_ch import init_settings


class Product(models.Model):
    _inherit = 'product.product'
    # if is_a_bundle or bundle_raw_material_ids --> !bundle_id

    bundle_id = fields.Many2one('product.template', string='Bundle', compute="_compute_bundle_id",store=True,readonly=False)
    description = fields.Char(related='product_tmpl_id.description',string='Description')

    def _compute_bundle_id(self):
        for product in self:
            # ဘာမှမရှိရင် အရင်ဆုံး False ပေးထားမယ်
            product.bundle_id = False
            # ၎င်း product ကို သုံးထားတဲ့ Raw Material ရှိမရှိ ရှာမယ်
            BRM = self.env['bundle.raw.mat'].search([('product_id', '=', product.id)], limit=1)
            if BRM:
                product.bundle_id = BRM.product_tmpl_id.id
