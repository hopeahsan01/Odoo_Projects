from odoo import models, fields, api


class PriceListRule(models.Model):
    _name = 'price.list.rule'
    _description = 'Price List Rule'

    product_tmpl_id = fields.Many2one('product.template', string='Product Template', required=True)
    maximum = fields.Float(string='Max')
    minimum = fields.Float(string='Mini')
    price = fields.Float(string='Price')


class ProductTemplateExt(models.Model):
    _inherit = 'product.template'

    price_list_rules = fields.One2many('price.list.rule', 'product_tmpl_id', string='Price List Rules')


class SaleOrderExt(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_uom_qty')
    def _onchange_quantity(self):
        for line in self:
            product = line.product_id
            product_tmpl_id = self.env['product.template.attribute.value'].search(
                [('product_tmpl_id', '=', line.product_template_id.id)])
            for attrs in product_tmpl_id:
                if attrs.id in line.product_id.product_template_variant_value_ids.ids:
                    price_list = product.price_list_rules.filtered(
                        lambda rule: rule.minimum <= line.product_uom_qty <= rule.maximum)
                    line.price_unit = price_list.price + attrs.price_extra
