from handlers.basic_handlers import BaseHandler
from models.order import Order
from models.user import Customer
from google.appengine.api import users
from operator import attrgetter


class HistoryHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        orders = Order.query(Order.email == user.email(), Order.completed == True).fetch()
        orders_list = sorted(orders, key=attrgetter("date"), reverse=True)

        for order in orders_list:
            products = order.products
            params = {"orders": orders, "products": products, "user": user}

            return self.render_template("history.html", params=params)


class UserHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        customer = Customer.query(Customer.email == user.email()).get()

        params = {"customer": customer}

        return self.render_template("user.html", params=params)

    def post(self):
        user = users.get_current_user()
        customer = Customer.query(Customer.email == user.email()).get()

        full_name = self.request.get("full_name")
        address_line_1 = self.request.get("address_line_1")
        address_line_2 = self.request.get("address_line_2")
        city = self.request.get("city")
        state = self.request.get("state")
        zip_number = int(self.request.get("zip_number"))
        country = self.request.get("country")

        customer.full_name = full_name
        customer.address_line_1 = address_line_1
        customer.address_line_2 = address_line_2
        customer.city = city
        customer.state = state
        customer.zip_number = zip_number
        customer.country = country
        customer.put()

        return self.redirect_to("home")