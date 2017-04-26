# -*- coding: utf-8 -*-
import pytest
from flask import Flask

from flask_clacks import Clacks

app = Flask(__name__)
Clacks(app)

methods = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD', 'PATCH']


@app.route('/foo/', methods=methods)
def foo():
    return 'bar'


@pytest.mark.parametrize('verb', [m.lower() for m in methods])
def test_has_default_overhead(verb):
    with app.test_client() as c:
        resp = getattr(c, verb)('/foo/')
        assert 'X-Clacks-Overhead' in resp.headers
        assert len(resp.headers.getlist('X-Clacks-Overhead')) == 1
        assert resp.headers.get('X-Clacks-Overhead') == 'GNU Terry Pratchett'
