# -*- coding: utf-8 -*-
# from odoo import http


# class JoinetPagos(http.Controller):
#     @http.route('/joinet_pagos/joinet_pagos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/joinet_pagos/joinet_pagos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('joinet_pagos.listing', {
#             'root': '/joinet_pagos/joinet_pagos',
#             'objects': http.request.env['joinet_pagos.joinet_pagos'].search([]),
#         })

#     @http.route('/joinet_pagos/joinet_pagos/objects/<model("joinet_pagos.joinet_pagos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('joinet_pagos.object', {
#             'object': obj
#         })
