# -*- coding: utf-8 -*-
from functools import wraps

from flask import make_response

__author__ = 'William Mayor'
__email__ = 'mail@williammayor.co.uk'
__version__ = '1.0.0'


class Clacks(object):

    def __init__(self, app=None, names=None):
        if names is None:
            names = []
        self.names = list(names) + ['Terry Pratchett']
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.after_request(self.add_headers)

    def add_headers(self, resp):
        for n in self.names:
            resp.headers.add('X-Clacks-Overhead', 'GNU ' + n)
        return resp


def clacks(names=None):
    _names = names

    def decorator(f):
        c = Clacks(names=_names)

        @wraps(f)
        def wrapper(*args, **kwargs):
            resp = make_response(f(*args, **kwargs))
            return c.add_headers(resp)

        return wrapper

    if callable(names):
        _names = None
        return decorator(names)
    return decorator
