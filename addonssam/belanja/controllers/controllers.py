from odoo import http, models, fields
from odoo.http import request
import json 

class Belanja(http.Controller):
    @http.route('/belanja/getbarang', auth='public', method=['GET'])
    def getBarang(self, **kw):
        barang = request.env['belanja.barang'].search([])
        isi = []
        for bb in barang:
            isi.append({
                'nama_barang' : bb.name,
                'harga_jual' : bb.harga_jual,
                'stok' : bb.stok 
            })
        return json.dumps(isi)

    @http.route('/belanja/getsupplier', auth='public', methode=['GET'])
    def getSupplier(self, **kw):
        supplier = request.env['belanja.supplier'].search([])
        isi = []
        for ss in supplier:
            isi.append({
                'nama_perusahaan' : ss.name,
                'alamat' : ss.alamat,
                'no_telp' : ss.no_telp
            })
        return json.dumps(isi)
