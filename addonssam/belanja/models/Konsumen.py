from odoo import api, fields, models


class Konsumen(models.Model):
    _inherit = 'res.partner'

    poin = fields.Integer(string='Poin')
    level = fields.Char(string='Level')
    
    