# Copyright (C) 2019 Odoo
# Copyright (C) 2019 Open Source Integrators
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import api, models


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"
    _description = "Sales Advance Payment Invoice"

    @api.multi
    def _create_invoice(self, order, so_line, amount):
        invoice = super(SaleAdvancePaymentInv, self)._create_invoice(
            order, so_line, amount)
        invoice.write({
            'exemption_code': order.exemption_code or '',
            'exemption_code_id': order.exemption_code_id.id or False,
            'location_code': order.location_code or '',
            'tax_on_shipping_address': order.tax_on_shipping_address,
        })
        # invoice.compute_taxes()
        return invoice
