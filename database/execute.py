from click import File
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Aa138484653++"
  
)

cursor = db.cursor();

cursor.execute("DROP DATABASE IF EXISTS shelfLife")

cursor.execute("CREATE DATABASE shelfLife");

cursor.execute("SHOW DATABASES")

database = cursor.fetchall();

for db in database:
    print(db);
cursor.close()
db.close();
