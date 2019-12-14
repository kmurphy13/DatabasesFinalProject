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

cmd = '''
    DROP TYPE IF EXISTS pass_type;
    DROP TYPE IF EXISTS worker_type;
    DROP TYPE IF EXISTS equipment_type;
    DROP TYPE IF EXISTS trail_type;
    DROP TYPE IF EXISTS trail_difficulty;
    DROP TYPE IF EXISTS facilities_type;
    
    CREATE TYPE pass_type AS ENUM ('season', 'day', 'half_day', 'student', 'child', 'senior');
    CREATE TYPE worker_type AS ENUM ('worker', 'skier', 'DBM');
    CREATE TYPE equipment_type AS ENUM ('skis', 'poles', 'helmet', 'goggles', 'snowboard', 'snowboard_boots', 'ski_boots');
    CREATE TYPE trail_type AS ENUM ('glades', 'terrain_park','moguls','groomer');
    CREATE TYPE trail_difficulty AS ENUM ('easy','intermediate','difficult','very_difficult') ;
    CREATE TYPE facilities_type AS  ENUM ('lodge', 'chairlift', 'ski_patrol_hut', 'bar');
    
    DROP TABLE IF EXISTS users;
    CREATE TABLE users(
        user_id INT NOT NULL,
        email VARCHAR NOT NULL,
        password VARCHAR NOT NULL,
        first_name VARCHAR NOT NULL,
        last_name VARCHAR NOT NULL,
        type WORKER_TYPE NOT NULL,
        PRIMARY KEY(user_id)
    );
    
    DROP TABLE IF EXISTS trails;
    CREATE TABLE trails(
        trail_name VARCHAR NOT NULL,
        difficulty TRAIL_DIFFICULTY NOT NULL,
        type TRAIL_TYPE NOT NULL,
        length INT NOT NULL,
        status  BOOLEAN NOT NULL, 
        PRIMARY KEY(trail_name)
    );
    
    DROP TABLE IF EXISTS facilities;
    CREATE TABLE facilities(
        facility_name VARCHAR NOT NULL,
        type FACILITIES_TYPE NOT NULL,
        capacity NUMERIC(10) NOT NULL, 
        status BOOLEAN NOT NULL,
        PRIMARY KEY (facility_name)
    );
    
    DROP TABLE IF EXISTS rentals;
    CREATE TABLE equipment(
    equipment_id  INT NOT NULL,
        type EQUIPMENT_TYPE NOT NULL,
        PRIMARY KEY(user_id, rental_id)
    );
    
    DROP TABLE IF EXISTS passes;
    CREATE TABLE passes(
        type pass_id NOT NULL,
        type user_id NOT NULL,
        price NUMERIC(10),
        PRIMARY KEY(user_id, pass_id),
        FOREIGN KEY (user_id) REFERENCES skiers(user_id),
        FOREIGN KEY (pass_id) REFERENCES pass_log(pass_id)
    );
    
    
    DROP TABLE IF EXISTS time_slots;
    CREATE TABLE time_slots(
        time_slot NUMERIC(10) NOT NULL,
        start_time VARCHAR NOT NULL,
        length NUMERIC(10) NOT NULL,
        PRIMARY KEY (time_slot)
    );


    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO rwlebl16, knmurp16;
    '''

# every query needs a cursor, a cursor is a reference to the result
# of a query
cur = conn.cursor()
cur.execute(cmd)

conn.commit()
