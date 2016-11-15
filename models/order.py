from google.appengine.ext import ndb
from models.product import Product


class Order(ndb.Model):
    email = ndb.StringProperty()
    date = ndb.StringProperty()
    total = ndb.FloatProperty(default=0)
    completed = ndb.BooleanProperty(default=False)
    shipped = ndb.BooleanProperty(default=False)
    products = ndb.StructuredProperty(Product, repeated=True)
    full_name = ndb.StringProperty()
    address_line_1 = ndb.StringProperty()
    address_line_2 = ndb.StringProperty()
    city = ndb.StringProperty()
    state = ndb.StringProperty()
    zip_number = ndb.IntegerProperty()
    country = ndb.StringProperty()