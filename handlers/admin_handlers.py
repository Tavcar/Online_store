from handlers.basic_handlers import BaseHandler
from models.order import Order
from decorators.login import admin_required


class OrdersHandler(BaseHandler):
    @admin_required
    def get(self):
        orders_list = Order.query(Order.completed == True).fetch()
        params = {"orders_list": orders_list}

        return self.render_template("history.html", params=params)


class ShippingOrderHandler(BaseHandler):
    @admin_required
    def get(self, order_id):
        order = Order.get_by_id(int(order_id))
        params = {"order": order}
        return self.render_template("shipping.html", params=params)

    @admin_required
    def post(self, order_id):
        order = Order.get_by_id(int(order_id))
        order.shipped = True
        order.put()

        return self.redirect("shipped.html")


class ShippedOrdersHandler(BaseHandler):
    @admin_required
    def get(self):
        shipped_list = Order.query(Order.shipped == True).fetch()
        params = {"shipped_list": shipped_list}

        return self.render_template("shipped.html", params=params)