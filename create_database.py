import sqlite3

conn = sqlite3.connect('etf.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS optimized_etf (
                Security TEXT,
                Weight REAL
             )''')

conn.commit()
conn.close()
