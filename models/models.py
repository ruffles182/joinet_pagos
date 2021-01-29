# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date
from odoo.modules.module import get_module_resource

class joinet_pagos(models.Model):
    _name = 'joinet_pagos.joinet_pagos'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'joinet_pagos.joinet_pagos'

    origen = fields.Many2one('joinet_pagos.joinet_pagos_origen_pedidos', "Origen")
    name = fields.Char("Pedido")
    fecha_del_pago = fields.Date("Fecha del pago")
    banco = fields.Many2one('joinet_pagos.joinet_pagos_bancos', "Banco")
    monto = fields.Integer("Monto")
    subido_por = fields.Many2one('res.users','Subido por', default=lambda self: self.env.user, readonly=True)
    fecha_validacion = fields.Date("Fecha validación")
    fecha_impresion = fields.Date("Fecha impresión")
    nombre_archivo = fields.Char("nombre archivo")
    archivo = fields.Binary("Imagen")

    @api.onchange('origen')
    def _onchange_partner(self):
        f = open(get_module_resource('joinet_pagos', 'static/', 'conf.txt'), "r")
        siguiente = int(f.readline()) + 1
        if self.origen.nomenclatura:
            self.name = self.origen.nomenclatura + str("-") + str("{:04d}".format(siguiente))
        f.close()
        

    @api.onchange('name')
    def _onchange_name(self):
        self.nombre_archivo = self.name + str(date.today())

    @api.model
    def create(self,values):
        rtn = super(joinet_pagos, self).create(values)

        f = open(get_module_resource('joinet_pagos', 'static/', 'conf.txt'), "r")
        secuencia = int(f.readline()) + 1
        f.close()

        f = open(get_module_resource('joinet_pagos', 'static/', 'conf.txt'), "w")
        f.write(str(secuencia))
        f.close()

        return rtn
    
    @api.model
    def default_get(self, fields):
        res = super(joinet_pagos, self).default_get(fields)
        res['origen'] = 1
        return res

class joinet_pagos_bancos(models.Model):
    _name = 'joinet_pagos.joinet_pagos_bancos'
    _description = 'joinet_pagos.joinet_pagos_bancos'

    name = fields.Char("Banco")

class joinet_pagos_orgien_pedido(models.Model):
    _name = 'joinet_pagos.joinet_pagos_origen_pedidos'
    _description = 'joinet_pagos.joinet_pagos_origen_pedidos'

    name = fields.Char("Origen de pedido")
    nomenclatura = fields.Char("Nomenclatura")

class joinet_pagos_secuencia(models.Model):
    _name = 'joinet_pagos.joinet_pagos_secuencia'
    _description = 'joinet_pagos.joinet_pagos_secuencia'

    name = fields.Integer("Secuencia")
