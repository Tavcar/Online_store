from handlers.basic_handlers import BaseHandler
from models.product import Product
from decorators.login import admin_required


class AddProductHandler(BaseHandler):
    @admin_required
    def get(self):
        return self.render_template("add-product.html")

    @admin_required
    def post(self):
        name = self.request.get("name")
        year = int(self.request.get("year"))
        genre = self.request.get("genre")
        price = int(self.request.get("price"))
        image = self.request.get("image")
        text = self.request.get("text")

        product = Product(name=name, year=year, genre=genre, price=price, image=image, text=text)
        product.put()
        return self.redirect_to("home")


class EditProductHandler(BaseHandler):
    @admin_required
    def get(self, product_id):
        product = Product.get_by_id(int(product_id))
        params = {"product": product}
        return self.render_template("edit-product.html", params=params)

    @admin_required
    def post(self, product_id):
        name = self.request.get("name")
        year = int(self.request.get("year"))
        genre = self.request.get("genre")
        price = int(self.request.get("price"))
        image = self.request.get("image")
        text = self.request.get("text")
        product = Product.get_by_id(int(product_id))
        product.name = name
        product.price = price
        product.year = year
        product.genre = genre
        product.image = image
        product.text = text
        product.put()
        return self.redirect_to("home")


class DeleteProductHandler(BaseHandler):
    @admin_required
    def get(self, product_id):
        product = Product.get_by_id(int(product_id))
        params = {"product": product}
        return self.render_template("delete-product.html", params=params)

    @admin_required
    def post(self, product_id):
        product = Product.get_by_id(int(product_id))
        product.key.delete()
        return self.redirect_to("home")


class ProductHandler(BaseHandler):

    def get(self, product_id):
        product = Product.get_by_id(int(product_id))
        params = {"product": product}
        return self.render_template("product.html", params=params)
