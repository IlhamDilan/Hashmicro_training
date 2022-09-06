from odoo import api, fields, models


class Supplier(models.Model):
    _name = 'belanja.supplier'
    _description = 'New Description'

    name = fields.Char(string='Nama Perusahaan')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No Telpon')
    barang_id = fields.Many2many(comodel_name='belanja.barang', string='Barang')
    
    
    
