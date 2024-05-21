import portfolio_optimizer as po
import visualize_etf as ve

# Define the securities
securities = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'JNJ', 'PFE', 'JPM', 'BAC']

# Perform portfolio optimization
optimized_weights = po.optimize_portfolio(securities)

# Save the optimized weights to the database
po.save_to_database(securities, optimized_weights)

# Visualize the optimized ETF composition
ve.visualize_etf()
