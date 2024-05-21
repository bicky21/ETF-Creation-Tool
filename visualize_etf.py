import sqlite3
import matplotlib.pyplot as plt

def visualize_etf():
    conn = sqlite3.connect('etf.db')
    c = conn.cursor()

    c.execute("SELECT * FROM optimized_etf")
    data = c.fetchall()
    securities = [row[0] for row in data]
    weights = [row[1] for row in data]

    plt.figure(figsize=(12, 6))
    plt.bar(securities, weights)
    plt.xlabel('Security')
    plt.ylabel('Weight')
    plt.title('Optimized ETF Composition')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    conn.close()
