# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ProductSetRawMat(models.Model):
    _name = 'product_set.raw.mat'
    _description = 'Component of a product set'

    sequence = fields.Integer(string='sequence', default=10)
    product_tmpl_id = fields.Many2one('product.template', string='Product Set', required=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', string="Product")
    # parts_type = fields.Selection([
    #     ('main', "Main"),
    #     ('major', "Major"),
    #     ('minor', "Minor")], default=False, help="Technical field for UX purpose.")
    quantity = fields.Float(string='Quantity', default=1.0)
    packing_list = fields.Float(string='Packing List')
    uom_id = fields.Many2one('uom.uom', string='Unit Of Measure', domain="[('category_id', '=', product_uom_category_id)]")
    product_uom_category_id = fields.Many2one(related='product_id.uom_id.category_id', readonly=True)
    display_type = fields.Selection([
        ('line_section', "Section"),
        ('line_note', "Note")], default=False, help="Technical field for UX purpose.")
    name = fields.Text(string="Name", required=True)

    def prepare_raw_mat_wiz(self, quantity=1.0):
        """
        Create a dictionary of values for creating product_set.raw.mat.wiz records.
        """
        self.ensure_one()
        return {
            'sequence': self.sequence,
            'product_id': self.product_id.id if self.product_id else False,
            'unit_quantity': self.quantity,
            'packing_list': self.packing_list,
            'quantity': self.quantity * quantity * self.packing_list,
            'uom_id': self.uom_id.id if self.uom_id else False,
            'display_type': self.display_type,
            'name': self.name,
        }

    @api.constrains('product_id', 'display_type')
    def none_section_line_product_mandatory(self):
        """
        Line which are not a section or a comment must have a product.
        """
        for line in self:
            if not line.display_type and not line.product_id:
                raise ValidationError(_("Product set components must have a product."))

    @api.onchange('product_id')
    def onchange_product_id(self):
        if self.product_id:
            self.uom_id = self.product_id.uom_id
            self.name = self.product_id.get_product_multiline_description_sale()

    def name_get(self):
        """
        Compute the raw mat name.
        """
        result = []
        for line in self.sudo():
            name = '%s - %s' % (line.product_tmpl_id.name, line.product_id.name)
            result.append((line.id, name))
        return result

    @api.model
    def _prepare_add_missing_fields(self, values):
        """ Deduce missing required fields"""
        res = values.copy()
        onchange_fields = ['name']
        if any(f not in values for f in onchange_fields):
            if 'product_id' in res:
                product = self.env['product.product'].browse(res['product_id'])
                res['name'] = product.name
        return res

    @api.model_create_multi
    def create(self, vals_list):
        """ အသစ်ဆောက်ရင် Product ထဲက product_set_id ကို update လုပ်မယ် """
        for values in vals_list:
            values.update(self._prepare_add_missing_fields(values))

        records = super().create(vals_list)

        # Product ရဲ့ compute function ကို အတင်းအလုပ်လုပ်ခိုင်းခြင်း
        for record in records:
            if record.product_id:
                record.product_id._compute_product_set_id()
        return records

    def write(self, vals):
        """ ပြင်ဆင်မှုလုပ်ရင် Product ထဲက product_set_id ကို update လုပ်မယ် """
        # မပြင်ခင်က ရှိခဲ့တဲ့ product_ids တွေကို မှတ်ထားမယ်
        old_products = self.mapped('product_id')

        res = super().write(vals)

        # ပြင်ပြီးသွားရင် အဟောင်းကော၊ အသစ်ပြောင်းသွားတဲ့ product ကော နှစ်ခုလုံးကို update လုပ်မယ်
        new_products = self.mapped('product_id')
        for product in (old_products | new_products):
            if product:
                product._compute_product_set_id()
        return res

    def unlink(self):
        """ ဖျက်လိုက်ရင် Product ထဲက product_set_id ကို ပြန်ဖျက်ပေးမယ် """
        products = self.mapped('product_id')
        res = super().unlink()
        for product in products:
            if product:
                product._compute_product_set_id()
        return res