import psycopg2
import gc

# connect to our database
try:
    conn = psycopg2.connect(
        dbname="finalproject_jonas_remi_kira",  # kwarg
        user="jbpeek16",
        host="cs-linuxlab-02.stlawu.local",
        password="Vnr7mr86"
    )
    gc.collect()
    print("Successfully connected to database")
except psycopg2.Error:
    print("Cannot connect to database")
    exit()

# issue query

# cmd = '''
# DROP TABLE IF EXISTS users;
# create table users (
#     first varchar not null,
#     last varchar not null,
#     id int not null,
#     primary key(id)
# );
# '''

cmd = "DROP TABLE IF EXISTS users;" \
      "CREATE TABLE test3(val1 VARCHAR NOT NULL, val2 VARCHAR NOT NULL);" \
      "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO rwlebl16, knmurp16;"

# every query needs a cursor, a cursor is a reference to the result
# of a query
cur = conn.cursor()
cur.execute(cmd, ())

conn.commit()
