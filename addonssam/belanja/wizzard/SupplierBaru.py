from odoo import api, fields, models


class supplierbaru(models.TransientModel):
    _name = 'belanja.supplierbaru'

    name = fields.Char(string='Nama Supplier', required=False)
    alamat = fields.Char(string='Alamat', required=False)
    no_telp = fields.Char(string='No Telpon', required=False)

    def button_supplierbaru(self):
        for rec in self:
            print('test')
            vals = {
                'name': self.name,
                'alamat': self.alamat,
                'no_telp': self.no_telp
            }
            print('vals....', vals)
            self.env['belanja.supplier'].create(vals)

    

    