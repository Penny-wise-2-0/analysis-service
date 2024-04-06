from flask import Blueprint, jsonify
import pandas as pd
from app import db
from sqlalchemy import text

transaction_routes = Blueprint('transaction_routes', __name__, url_prefix='/transactions')

@transaction_routes.route("/by-month/<userID>")
def by_month(userID):
 
    query = text("SELECT date, amount FROM transactions WHERE user_id = :user_id")
    df = pd.read_sql(query, params={"user_id": userID}, con=db.engine)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    monthly_expenses = df[df['amount'] < 0]['amount'].resample('ME').sum()
    monthly_income = df[df['amount'] > 0]['amount'].resample('ME').sum()
    monthly_expenses.index = monthly_expenses.index.strftime('%Y-%m')
    monthly_income.index = monthly_income.index.strftime('%Y-%m')
    monthly_expenses_dict = monthly_expenses.to_dict()
    monthly_income_dict = monthly_income.to_dict()


    monthly_cashflow = {
        'expenses': monthly_expenses_dict,
        'income': monthly_income_dict
    }

    return jsonify(monthly_cashflow)