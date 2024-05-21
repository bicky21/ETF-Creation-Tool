# ETF Creation Tool

## Introduction

The ETF (Exchange-Traded Fund) Creation Tool is a Python-based application that automates the creation of ETFs based on predefined criteria. It uses historical price data to optimize the ETF composition and provides visualizations of the optimized ETFs. The tool consists of several modules, including portfolio optimization, database management, and visualization.

## Architecture Overview

The ETF Creation Tool is designed as a set of modular components that work together to perform the following tasks:

- **Data Collection:** Fetch historical price data for a predefined set of securities.
- **Portfolio Optimization:** Use the historical data to calculate the optimal weights for the securities in the ETF, considering factors such as expected return and volatility.
- **Database Management:** Store the optimized ETF compositions in a SQLite database for future reference.
- **Visualization:** Visualize the optimized ETF compositions using bar charts.

## Requirements

- Python 3.x
- `numpy`, `pandas`, `sqlite3`, `yfinance`, `cvxpy`, `matplotlib` Python libraries

## Installation

1. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/bicky21/etf-creation-tool.git

2. Run
   ```bash
   python etf_creation_tool.py
