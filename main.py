#!/usr/bin/env python
import webapp2
from handlers.basic_handlers import MainHandler
from handlers.product_handlers import ProductHandler, AddProductHandler, EditProductHandler, DeleteProductHandler


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="home"),
    webapp2.Route('/product/<product_id:\d+>', ProductHandler),
    webapp2.Route('/add-product', AddProductHandler),
    webapp2.Route('/edit-product/<product_id:\d+>', EditProductHandler),
    webapp2.Route('/delete-product/<product_id:\d+>', DeleteProductHandler),
], debug=True)
