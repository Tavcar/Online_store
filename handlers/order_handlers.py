from handlers.basic_handlers import BaseHandler
from models.order import Order
from google.appengine.api import users
from models.user import Customer
from datetime import datetime



class CartHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        order = Order.query(Order.email == user.email(), Order.completed == False).get()
        list = order.products

        total = 0
        for product in list:
            price = product.price
            total += price

        params = {"order": order, "list": list, "total": total}

        return self.render_template("cart.html", params=params)

    def post(self):
        user = users.get_current_user()
        order = Order.query(Order.email == user.email(), Order.completed == False).get()

        delete = self.request.get("delete")
        a = [i for i in order.products if i.name == delete][0]
        order.products.remove(a)
        order.put()

        return self.redirect("cart")


class AddressHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        customer = Customer.query(Customer.email == user.email()).get()
        params = {"customer": customer}
        return self.render_template("address.html", params=params)

    def post(self):
        user = users.get_current_user()
        order = Order.query(Order.email == user.email(), Order.completed == False).get()
        list = order.products

        total = 0
        for product in list:
            price = product.price
            total += price

        full_name = self.request.get("full_name")
        address_line_1 = self.request.get("address_line_1")
        address_line_2 = self.request.get("address_line_2")
        city = self.request.get("city")
        state = self.request.get("state")
        zip_number = int(self.request.get("zip_number"))
        country = self.request.get("country")

        order.email = user.email()
        order.total = total
        order.full_name = full_name
        order.address_line_1 = address_line_1
        order.address_line_2 = address_line_2
        order.city = city
        order.state = state
        order.zip_number = zip_number
        order.country = country
        order.put()

        return self.redirect_to("checkout")


class CheckoutHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        order = Order.query(Order.email == user.email(), Order.completed == False).get()
        list = order.products
        params = {"order": order, "list": list}

        return self.render_template("checkout.html", params=params)

    def post(self):
        user = users.get_current_user()
        date = datetime.now().strftime("%d-%m-%Y at %H.%M.%S")
        order = Order.query(Order.email == user.email(), Order.completed == False).get()
        order.date = date
        order.completed = True
        order.put()

        return self.redirect_to("home")