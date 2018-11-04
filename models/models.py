# -*- coding: utf-8 -*-
from odoo import models, fields, api, tools


class AccountAccount(models.Model):
    _inherit = "account.account"

    is_rent = fields.Boolean(string='Is Rent')
  
