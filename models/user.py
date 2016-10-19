from google.appengine.ext import ndb


class User(ndb.Model):
    email = ndb.StringProperty()
    full_name = ndb.StringProperty()
    street_name = ndb.StringProperty()  #Naslov tukaj razen ce kasneje dodamo Address kot svoj model?
    address_line_1 = ndb.StringProperty()
    address_line_2 = ndb.StringProperty()
    city = ndb.StringProperty()
    state = ndb.StringProperty()
    zip_number = ndb.IntegerProperty()
    country = ndb.StringProperty()

    @classmethod
    def create(cls, email, full_name, street_name, address_line_1, address_line_2, city, state, zip_number, country):
        user = cls(email=email, full_name=full_name, street_name=street_name, address_line_1=address_line_1,
                   address_line_2=address_line_2, city=city, state=state, zip_number=zip_number, country=country)
        user.put()
        return user
