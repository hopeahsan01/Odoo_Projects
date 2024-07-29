# -*- coding: utf-8 -*-
from odoo import models, fields, api

class StockValReport(models.AbstractModel):
    _name = "report.inventory_customer_report.stock_val_pdf_report"

    def _get_report_values(self, docids, data=None):
        model = self.env.context.get('active_model')
        rec_model = self.env[model].browse(self.env.context.get('active_id'))
        lines = self.env['stock.move.line'].search([])
        return {
            'doc_ids': self.ids,
            'doc': self.ids,
            'rec_model': rec_model,
            'doc_model': 'stock.val.wizard',
            'lines': lines,
            'data': data,
        }
