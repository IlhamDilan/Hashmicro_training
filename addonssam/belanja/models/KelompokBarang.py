from odoo import api, fields, models

# Model membuat tabel
class kelompokbarang(models.Model):
    _name = 'belanja.kelompokbarang' # Buat nama tabel
    _description = 'New Description'
   
    
    name = fields.Selection([
        ('sampoo', 'Sampoo'), 
        ('makananinstant', 'Makanan Instant'), 
        ('minuman', 'Minuman')
    ], string='Nama Kelompok')
    kode_kelompok = fields.Char(string='kode_kelompok')
    
    @api.onchange('name')
    def _compute_kode_kelompok(self):
        if (self.name == 'sampoo'):
            self.kode_kelompok = 'samp-01'
        elif(self.name == 'makananinstant'):
            self.kode_kelompok = 'makins-01'
        elif(self.name == 'minuman'):
            self.kode_kelompok = 'minuman-01'
            

    # name = fields.Char(string='Nama Kelompok') # fields membuat kolom
    # kode_kelompok = fields.Char(string='Kode Kelompok') 
    kode_rak = fields.Char(string='Kode Nomor Rak')
    barang_ids = fields.One2many(comodel_name='belanja.barang', 
                                inverse_name='kelompokbarang_id', 
                                string='Daftar Barang')
    
    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Item')
    daftar = fields.Char(string='Daftar Isi')
    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['belanja.barang'].search([('kelompokbarang_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftar = a

    
    