import sqlite3

conn = sqlite3.connect("new.db")

cursor = conn.cursor()

# create a table
cursor.execute("""
CREATE TABLE population(
city TEXT, 
state TEXT, 
population INT)
""")

# close the database connection
conn.close()