#!/usr/bin/env python
import os
import jinja2
import webapp2
from models.order import Order
from models.product import Product
from google.appengine.api import users
from admins import ADMIN


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        user = users.get_current_user()
        params["user"] = user

        if user:
            logiran = True
            logout_url = users.create_logout_url('/')
            params["logout_url"] = logout_url
            params["logiran"] = logiran
            if user.nickname() in ADMIN:
                user.admin = True
            return self.response.out.write(template.render(params))

        else:
            logiran = False
            login_url = users.create_login_url('/')
            params["login_url"] = login_url
            params["logiran"] = logiran
            return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        list = Product.query().fetch()
        params = {"list": list}

        return self.render_template("home.html", params=params)