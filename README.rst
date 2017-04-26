===============================
Flask-Clacks
===============================


.. image:: https://img.shields.io/pypi/v/flask-clacks.svg
        :target: https://pypi.python.org/pypi/flask-clacks

.. image:: https://img.shields.io/travis/WilliamMayor/flask-clacks.svg
        :target: https://travis-ci.org/WilliamMayor/flask-clacks

.. image:: https://readthedocs.org/projects/flask-clacks/badge/?version=latest
        :target: https://flask-clacks.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/WilliamMayor/flask-clacks/shield.svg
     :target: https://pyup.io/repos/github/WilliamMayor/flask-clacks/
     :alt: Updates


A man is not dead while his name is still spoken.

This is a very simple Flask extension that adds 'X-Clacks-Overhead' headers to
your website's responses.


* Free software: MIT license
* Documentation: https://flask-clacks.readthedocs.io.


Features
--------

This package exposes a Flask extension which by default adds the header
``X-Clacks-Overhead: GNU Terry Pratchett`` on all routes, for all origins and
methods.

* You can add extra names to your overhead
* You can decorate individual routes to have the overhead


Installation
------------

Install the extension with using pip, or easy\_install.

.. code:: console

    $ pip install -U flask-clacks

Usage
-----

Apply to all routes, sending only Terry Pratchett's name in the overhead.

.. code:: python

    from flask import Flask
    from flask-clacks import Clacks

    app = Flask(__name__)
    Clacks(app)

    @app.route("/")
    def index():
        # Will have the header added to the response
        return "OK"

Apply to all routes, sending Terry Pratchett and John Dearheart's names in the
overhead.

.. code:: python

    from flask import Flask
    from flask-clacks import Clacks

    app = Flask(__name__)
    Clacks(app, names=('John Dearheart', ))

    @app.route("/")
    def index():
        # Will have the the clacks overhead header for both Terry and John
        return "OK"


Apply to specific routes, sending different names back on different responses.

.. code:: python

    from flask import Flask
    from flask-clacks import clacks

    app = Flask(__name__)

    @app.route("/terry/")
    @clacks
    def terry():
        # Will have a clacks overhead header for Terry
        return "OK"

    @app.route("/terry-and-john/")
    @clacks(names=('John Dearheart', ))
    def terry_and_john():
        # Will have a clacks overhead header for both Terry and John
        return "OK"

    @app.route("/no-one/")
    def no_one():
        # Will not have clacks overhead headers
        return "OK"


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

Thanks go to the `Flask-CORS`_ extension for providing decent examples of how to
package an extension.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`Flask-CORS`: https://github.com/corydolphin/flask-cors
