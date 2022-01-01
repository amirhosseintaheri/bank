import sqlite3

db = sqlite3.connect('Bank.db')

query_file = open('/CreateQuery.sql', 'r')

db.executescript(query_file.read())

query_file.close()