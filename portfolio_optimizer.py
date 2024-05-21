import numpy as np
import pandas as pd
import sqlite3
import yfinance as yf
import cvxpy as cp

def optimize_portfolio(securities):
    # Fetch historical price data
    prices_df = pd.DataFrame()
    for security in securities:
        data = yf.download(security, start='2007-01-01', end='2008-01-01')
        prices_df[security] = data['Adj Close']

    # Calculate daily returns
    returns_df = prices_df.pct_change().dropna()

    # Calculate covariance matrix
    cov_matrix = returns_df.cov().values

    # Define the risk-free rate
    risk_free_rate = 0.02  # 2%

    # Define the optimization variables
    w = cp.Variable(len(securities))

    # Define the objective and constraints
    expected_return = returns_df.mean().values
    volatility = cp.quad_form(w, cov_matrix)
    objective = cp.Maximize(expected_return @ w - risk_free_rate * volatility)
    constraints = [cp.sum(w) == 1, w >= 0]

    # Solve the optimization problem
    prob = cp.Problem(objective, constraints)
    prob.solve()

    # Retrieve the optimized weights
    return w.value

def save_to_database(securities, weights):
    # Connect to the SQLite database
    conn = sqlite3.connect('etf.db')
    c = conn.cursor()

    # Insert the optimized weights into the database
    c.execute('''CREATE TABLE IF NOT EXISTS optimized_etf (
                    Security TEXT,
                    Weight REAL
                 )''')
    for i in range(len(securities)):
        c.execute("INSERT INTO optimized_etf (Security, Weight) VALUES (?, ?)", (securities[i], weights[i]))

    conn.commit()
    conn.close()
