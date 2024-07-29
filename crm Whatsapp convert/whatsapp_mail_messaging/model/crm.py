# -*- coding: utf-8 -*-

from odoo import models, _
from odoo.exceptions import UserError


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def action_send_whatsapp(self):
        """ Action for sending WhatsApp message. """
        compose_form_id = self.env.ref(
            'whatsapp_mail_messaging.whatsapp_send_message_view_form').id
        ctx = dict(self.env.context)
        message_template = self.company_id.whatsapp_message

        # Construct default message
        default_message_parts = [
            "Hi ", self.partner_id.name or '', ',\n',
            "Your quotation ", self.name or '', " amounting ",
            str(0.0), (''), ' ',
            "is ready for review. Do not hesitate to contact us if you have any questions."
        ]

        default_message = ''.join(map(str, default_message_parts))

        message = message_template if message_template else default_message

        ctx.update({
            'default_message': message,
            'default_partner_id': self.partner_id.id,
            'default_mobile': self.partner_id.mobile,
            'default_image_1920': self.partner_id.image_1920,
        })

        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'whatsapp.send.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }

    def check_customers(self, partner_ids):
        """ Check if the selected leads belong to the same customer. """
        partners = self.env['crm.lead'].browse(partner_ids)
        return len(partners.mapped('partner_id')) == 1

    def action_whatsapp_multi(self):
        """
        Initiate WhatsApp messaging for multiple leads and open a message
        composition wizard.
        """
        lead_ids = self.env['crm.lead'].browse(self.env.context.get('active_ids'))
        partner_ids = lead_ids.mapped('partner_id.id')

        if self.check_customers(partner_ids):
            lead_names = lead_ids.mapped('name')
            sale_numbers = "\n".join(lead_names)

            compose_form_id = self.env.ref(
                'whatsapp_mail_messaging.whatsapp_send_message_view_form').id

            ctx = dict(self.env.context)
            message = ("Hi " + (self.partner_id.name or '') + ',\n' +
                       "Your leads are" + '\n' + sale_numbers + ' ' + '\n' +
                       "are ready for review. Please contact us if "
                       "you have any questions.")

            ctx.update({
                'default_message': message,
                'default_partner_id': lead_ids[0].partner_id.id,
                'default_mobile': lead_ids[0].partner_id.mobile,
                'default_image_1920': lead_ids[0].partner_id.image_1920,
            })

            return {
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'whatsapp.send.message',
                'views': [(compose_form_id, 'form')],
                'view_id': compose_form_id,
                'target': 'new',
                'context': ctx,
            }
        else:
            raise UserError(_(
                'It appears that you have selected leads from multiple '
                'customers. Please select leads from a single customer.'))
