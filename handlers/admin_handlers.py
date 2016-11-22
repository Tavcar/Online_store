from handlers.basic_handlers import BaseHandler
from models.order import Order
from decorators.login import admin_required
from operator import attrgetter


class OrderListHandler(BaseHandler):

    def get(self):
        orders = Order.query(Order.completed == True, Order.shipped == False).fetch()
        orders_list = sorted(orders, key=attrgetter("date"), reverse=True)

        for order in orders_list:
            products = order.products
            params = {"orders": orders_list, "products": products}

            return self.render_template("admin_orders.html", params=params)


class ShippingOrderHandler(BaseHandler):
    @admin_required
    def get(self, order_id):
        order = Order.get_by_id(int(order_id))
        params = {"order": order}
        return self.render_template("admin_orders_shipping.html", params=params)

    @admin_required
    def post(self, order_id):
        order = Order.get_by_id(int(order_id))
        order.shipped = True
        order.put()

        return self.redirect_to("shipped")


class ShippedOrdersHandler(BaseHandler):
    @admin_required
    def get(self):
        shipped_list = Order.query(Order.shipped == True).fetch()
        params = {"shipped_list": shipped_list}

        return self.render_template("admin_orders_shipped.html", params=params)