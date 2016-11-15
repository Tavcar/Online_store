from google.appengine.ext import ndb


class Customer(ndb.Model):
    email = ndb.StringProperty()
    full_name = ndb.StringProperty()
    address_line_1 = ndb.StringProperty()
    address_line_2 = ndb.StringProperty()
    city = ndb.StringProperty()
    state = ndb.StringProperty()
    zip_number = ndb.IntegerProperty()
    country = ndb.StringProperty()
