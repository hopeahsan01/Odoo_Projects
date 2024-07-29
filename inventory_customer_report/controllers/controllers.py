# -*- coding: utf-8 -*-


import logging
from odoo import http

from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager


class ControllerInh(CustomerPortal):

    @http.route('/my/task/project/<model("project.project"):project_id>', type='http', auth="user")
    def project_task_report(self, project_id, **kw):
        return self._show_report(
            model=project_id,
            report_type='pdf',
            report_ref='inventory_customer_report.action_report_project_portal',
            download=True,
        )