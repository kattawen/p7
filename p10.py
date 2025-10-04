import sqlite3

from urllib3 import connection_from_url

connection = sqlite3.connect("istep.DB.sl3", 5)
cur = connection.cursor()
print(connection)
print(cur)
connection.close()
