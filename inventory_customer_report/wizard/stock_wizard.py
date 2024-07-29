from odoo import models, fields
from datetime import datetime, timedelta
from odoo.tools import format_datetime
class StockLocationWizard(models.TransientModel):
    _name = 'stock.val.wizard'

    date_from = fields.Date()
    date_to = fields.Date()
    partner_ids = fields.Many2many('res.partner',string="Customer")

    def print_report(self):
        print("1")
        data = {'partner_ids': self.partner_ids.ids, 'date_from': self.date_from, 'date_to': self.date_to}
        return self.env.ref('inventory_customer_report.action_stock_val_pdf_report').report_action(self, data)

