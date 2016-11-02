from handlers.basic_handlers import BaseHandler
from models.order import Order


class HistoryHandler(BaseHandler):
    def get(self):
        history_list = Order.query(Order.shipped == True).fetch()
        params = {"history_list": history_list}

        return self.render_template("history.html", params=params)
