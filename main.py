#!/usr/bin/env python
import webapp2
from handlers.basic_handlers import MainHandler
from handlers.product_handlers import ProductHandler, AddProductHandler, EditProductHandler, DeleteProductHandler
from handlers.user_handlers import HistoryHandler, UserHandler
from handlers.admin_handlers import OrderListHandler, ShippingOrderHandler, ShippedOrdersHandler
from handlers.order_handlers import CartHandler, AddressHandler, CheckoutHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="home"),
    webapp2.Route('/product/<product_id:\d+>', ProductHandler),
    webapp2.Route('/cart', CartHandler, name="cart"),
    webapp2.Route('/history', HistoryHandler),
    webapp2.Route('/add-product/', AddProductHandler),
    webapp2.Route('/address', AddressHandler),
    webapp2.Route('/order/check-out', CheckoutHandler, name="checkout"),
    webapp2.Route('/user', UserHandler, name="user"),
    webapp2.Route('/edit-product/<product_id:\d+>', EditProductHandler),
    webapp2.Route('/delete-product/<product_id:\d+>', DeleteProductHandler),
    webapp2.Route('/completed', OrderListHandler),
    webapp2.Route('/shipped', ShippedOrdersHandler),
    webapp2.Route('/shipping/<order_id:\d+>', ShippingOrderHandler),
], debug=True)


