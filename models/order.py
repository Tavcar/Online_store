from google.appengine.ext import ndb
from models.product import Product
from models.user import User


class Order(ndb.Model):
    customer = ndb.KeyProperty(kind=User)
    date = ndb.StringProperty()
    total = ndb.FloatProperty()
    completed = ndb.BooleanProperty(default=False)
    shipped = ndb.BooleanProperty(default=False)
    products = ndb.StructuredProperty(Product, repeated=True)  # drugace pa KeyProperty ce to ne dela

