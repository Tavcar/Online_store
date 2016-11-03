from handlers.basic_handlers import BaseHandler
from models.order import Order
from google.appengine.api import users

class HistoryHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        history_list = Order.query(Order.shipped == True and Order.customer == user).fetch()  #nisem siguren ce bo customer == user v redu oz delovalo
        params = {"history_list": history_list}

        return self.render_template("history.html", params=params)
