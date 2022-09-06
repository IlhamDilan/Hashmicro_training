from odoo import api, fields, models


class Barang(models.Model):
    _name = 'belanja.barang'
    _description = 'New Description'

    name = fields.Char(string='Nama Barang')
    harga_barang = fields.Integer(string='Harga Barang', required=True) 
    harga_jual = fields.Integer(string='Harga Jual', required=True) # Required jika True harus diisi
    kelompokbarang_id = fields.Many2one(comodel_name='belanja.kelompokbarang', 
                                        string='Kelompok Barang',
                                        ondelete='cascade')
    supplier_id = fields.Many2many(comodel_name='belanja.supplier', string='Supplier')
    stok = fields.Integer(string='Stok')
    
    