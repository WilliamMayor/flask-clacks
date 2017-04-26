# -*- coding: utf-8 -*-
import pytest
from flask import Flask

from flask_clacks import clacks

app = Flask(__name__)

methods = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD', 'PATCH']


@app.route('/foo/', methods=methods)
@clacks
def foo():
    return 'bar'


@app.route('/foo2/', methods=methods)
@clacks(names=('John Dearheart', ))
def foo2():
    return 'bar2'


@app.route('/foo3/', methods=methods)
def foo3():
    return 'bar3'


@pytest.mark.parametrize('verb', [m.lower() for m in methods])
def test_has_default_overhead(verb):
    with app.test_client() as c:
        resp = getattr(c, verb)('/foo/')
        assert 'X-Clacks-Overhead' in resp.headers
        assert len(resp.headers.getlist('X-Clacks-Overhead')) == 1
        assert resp.headers.get('X-Clacks-Overhead') == 'GNU Terry Pratchett'


@pytest.mark.parametrize('verb', [m.lower() for m in methods])
def test_has_extra_overhead(verb):
    with app.test_client() as c:
        resp = getattr(c, verb)('/foo2/')
        assert 'X-Clacks-Overhead' in resp.headers
        overhead = resp.headers.getlist('X-Clacks-Overhead')
        assert len(overhead) == 2
        assert 'GNU Terry Pratchett' in overhead
        assert 'GNU John Dearheart' in overhead


@pytest.mark.parametrize('verb', [m.lower() for m in methods])
def test_has_no_overhead(verb):
    with app.test_client() as c:
        resp = getattr(c, verb)('/foo3/')
        assert 'X-Clacks-Overhead' not in resp.headers
