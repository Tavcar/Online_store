from google.appengine.ext import ndb


class Product(ndb.Model):
    name = ndb.StringProperty()
    price = ndb.IntegerProperty()
    year = ndb.IntegerProperty()
    genre = ndb.StringProperty(choices=('Horror', 'Action', 'Comedy', 'Drama', 'Thriller', 'Animated')) #dodaj se druge ce treba
    image = ndb.StringProperty()
    text = ndb.TextProperty()
    orders = ndb.KeyProperty(kind="Order", repeated=True) #za tole bo treba se probat, tako da nisem 100%


    @classmethod
    def create(cls, name, price, year, genre, image, text):
        product = cls(name=name, price=price, year=year, genre=genre, image=image, text=text)
        product.put()
        return product
