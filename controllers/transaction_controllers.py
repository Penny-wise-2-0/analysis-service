from models import Transaction
from flask import Blueprint, jsonify
import pandas as pd
from app import db
from sqlalchemy import text


def transactions(userID):
    query = text("SELECT * FROM transactions WHERE user_id = :user_id")
    df = pd.read_sql_query(query, params={"user_id": userID},con=db.engine)
    return df.to_json(orient='records')



def transactions_by_month(userID):
    query = text("SELECT * FROM transactions WHERE user_id = :user_id")
    df = pd.read_sql(query, params={"user_id": userID}, con=db.engine)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    monthly_expenses = df[df['amount'] < 0]['amount'].resample('M').sum()
    monthly_income = df[df['amount'] > 0]['amount'].resample('M').sum()
    monthly_expenses.index = monthly_expenses.index.strftime('%Y-%m')
    monthly_income.index = monthly_income.index.strftime('%Y-%m')
    monthly_cashflow_list = []

    for month in monthly_expenses.index.union(monthly_income.index).unique():
        expense = monthly_expenses.get(month, 0)
        income = monthly_income.get(month, 0)
        monthly_cashflow_list.append({
            'month': month,
            'expenses': float(expense),
            'income': float(income)
        })

    return jsonify(monthly_cashflow_list)