import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1973'
)

cursorobject = database.cursor()

cursorobject.execute("CREATE DATABASE elderco")
print("All done")