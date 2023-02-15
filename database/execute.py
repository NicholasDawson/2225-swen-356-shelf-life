import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Aa138484653++",
  database = "shelfLife"
)

cursor = db.cursor();
def execute_sql(filename):    
    executable = "";
    with open(filename) as f:
        executable += f.read()
    cursor.execute(executable, multi=True)

execute_sql("database\create_user_table.sql");
execute_sql('database\create_shelf_table.sql')
execute_sql('database\create_food_table.sql');

cursor.execute("SHOW DATABASES")
print(cursor.fetchall())

cursor.execute("SHOW TABLES")

print(cursor.fetchall())

cursor.close()
db.close();
