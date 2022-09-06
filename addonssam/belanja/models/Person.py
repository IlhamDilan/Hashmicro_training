from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Person(models.Model):
    _name = 'belanja.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Date(string='Tanggal Lahir')

    @api.constrains('tgl_lahir')
    def _tanggal_lahir(self):
        if self.tgl_lahir >= self.tgl_lahir.today():
            raise ValidationError('Anda Belum Lahir')
    _sql_constraints = [('name_zero', 'check (name IS NOT NULL)', 'Nama Tidak Boleh Kosong')
    ]

class Kasir(models.Model):
    _name = 'belanja.kasir'
    _inherit = 'belanja.person'
    _description = 'New Description'

    id_kasir = fields.Char(string='ID Kasir')

    @api.constrains('id_kasir')
    def _check_kasir(self):
        for rec in self:
            ids_kasir = self.env['belanja.kasir'].search([('id_kasir', '=', rec.id_kasir), ('id', '!=', rec.id)])
            if ids_kasir:
                raise ValidationError('Id Kasir {} sudah tersedia. Silahkan Diganti'.format(rec.id_kasir))

class CleaningService(models.Model):
    _name = 'belanja.cleaningservice'
    _inherit = 'belanja.person'
    _description = 'New Description'

    id_cln = fields.Char(string='ID Cleaning Service')

    @api.constrains('id_cln')
    def _check_kasir(self):
        for rec in self:
            ids_cs = self.env['belanja.cleaningservice'].search([('id_cln', '=', rec.id_cln), ('id', '!=', rec.id)])
            if ids_cs:
                raise ValidationError('ID Cleaning Service {} sudah tersedia. Silahkan Diganti'.format(rec.id_cln))
    
