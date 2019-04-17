# -*- coding: utf-8 -*-
# (C) 2019 Smile (<http://www.smile.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    acc_number = fields.Char(data_mask="'acc_number_' || id::text")