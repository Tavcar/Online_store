from google.appengine.ext import ndb


class Product(ndb.Model):
    name = ndb.StringProperty()
    price = ndb.FloatProperty()
    year = ndb.IntegerProperty()
    genre = ndb.StringProperty()
    image = ndb.StringProperty()
    text = ndb.TextProperty()


    @classmethod
    def create(cls, name, price, year, genre, image, text):
        product = cls(name=name, price=price, year=year, genre=genre, image=image, text=text)
        product.put()
        return product
