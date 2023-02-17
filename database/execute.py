import psycopg2

db = psycopg2.connect(
  database = "shelflife",
  user = "shelflife",
  password = "12345",
  host = "localhost",
  port = '5432'
)

cursor = db.cursor();
def execute_sql(filename):    
    executable = "";
    with open(filename) as f:
        executable += f.read()
    cursor.execute(executable)
def printTables():
  cursor.execute("""SELECT table_name FROM information_schema.tables
  WHERE table_schema = 'public'""")
  for table in cursor.fetchall():
      print(table)

execute_sql("database\create_user_table.sql");
execute_sql('database\create_shelf_table.sql')
execute_sql('database\create_food_table.sql');
printTables()
    
cursor.close()
db.close();
