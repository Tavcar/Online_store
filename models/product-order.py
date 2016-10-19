from google.appengine.ext import ndb
from models.product import Product
from models.order import Order


class OrderProduct(ndb.Model):
    product = ndb.KeyProperty(kind=Product)
    order = ndb.KeyProperty(kind=Order)
    quantity = ndb.IntegerProperty(default=1)

