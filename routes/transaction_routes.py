from controllers.transaction_controllers import transactions_by_month, transactions
from flask import Blueprint, jsonify
import pandas as pd
from app import db
from sqlalchemy import text

transaction_routes = Blueprint('transaction_routes', __name__, url_prefix='/transactions')


@transaction_routes.route("/<userID>")
def get_transactions(userID):
    return transactions(userID)




@transaction_routes.route("/by-month/<userID>")
def by_month(userID):
    return transactions_by_month(userID)



