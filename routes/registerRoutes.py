from flask import render_template, request
from .transaction_routes import transaction_routes


def register_routes(app, db):
    app.register_blueprint(transaction_routes)