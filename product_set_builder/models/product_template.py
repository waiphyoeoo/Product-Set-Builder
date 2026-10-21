# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_a_product_set = fields.Boolean(string='Is a Product Set',
                                 help='Define a product set and its components for use with compatible sales or purchase extensions.')
    product_set_raw_material_ids = fields.One2many('product_set.raw.mat', 'product_tmpl_id', string="Product Set Components")
    description = fields.Char(string='Description')

    @api.constrains('type')
    def check_product_set_validity(self):
        for product in self:
            if product.is_a_product_set and not product.type == 'consu':
                raise ValidationError(_("Product set products must be of type consumable."))

    @api.onchange('type')
    def onchange_is_a_product_set(self):
        """
        Only consumable product can be a product_set.
        """
        if not self.type == 'consu' and self.is_a_product_set:
            self.is_a_product_set = False

    @api.constrains('name')
    def _check_unique_name(self):
        for rec in self:
            if not rec.name:
                continue

            duplicate = self.search([
                ('id', '!=', rec.id),
                ('name', '=', rec.name),
            ], limit=1)

            if duplicate:
                raise ValidationError(_("The product name must be unique."))
