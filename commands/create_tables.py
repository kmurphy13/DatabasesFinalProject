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
    DROP TYPE IF EXISTS pass_types CASCADE;
    DROP TYPE IF EXISTS worker_type CASCADE;
    DROP TYPE IF EXISTS equipment_type CASCADE;
    DROP TYPE IF EXISTS trail_type CASCADE;
    DROP TYPE IF EXISTS trail_difficulty CASCADE;
    DROP TYPE IF EXISTS facilities_type CASCADE;
    DROP TYPE IF EXISTS position_type CASCADE;
    DROP TYPE IF EXISTS surface_type CASCADE;
    DROP TYPE IF EXISTS chair_lift_type CASCADE;
    
    CREATE TYPE pass_types AS ENUM ('season', 'day', 'half_day', 'student', 'child', 'senior');
    CREATE TYPE position_type AS ENUM ('owner', 'manager', 'ski_patrol', 'cook', 'bartender',
    'chairlift_operator', 'groomer', 'instructor');
    CREATE TYPE equipment_type AS ENUM ('skis', 'poles', 'helmet', 'goggles', 'snowboard', 'snowboard_boots', 'ski_boots');
    CREATE TYPE trail_type AS ENUM ('glades', 'terrain_park','moguls','groomer');
    CREATE TYPE trail_difficulty AS ENUM ('easy','intermediate','difficult','very_difficult') ;
    CREATE TYPE facilities_type AS  ENUM ('lodge', 'ski_patrol_hut', 'bar', 'ski_school', 'chairlift');
    CREATE TYPE surface_type AS ENUM('packed_powder','powder','frozen_granular','loose_granular');
    CREATE TYPE chair_lift_type AS ENUM('gondola','quad','t_bar','magic_carpet','triple','double');
    
    
    DROP TABLE IF EXISTS users CASCADE;
    CREATE TABLE users(
        user_id NUMERIC NOT NULL,
        email VARCHAR NOT NULL,
        first_name VARCHAR NOT NULL,
        last_name VARCHAR NOT NULL,
        PRIMARY KEY(user_id)
    );
    
    DROP TABLE IF EXISTS trails CASCADE;
    CREATE TABLE trails(
        trail_name VARCHAR NOT NULL,
        difficulty TRAIL_DIFFICULTY NOT NULL,
        type TRAIL_TYPE NOT NULL,
        length NUMERIC NOT NULL,
        status BOOLEAN NOT NULL,
        PRIMARY KEY(trail_name)
    );
    
    DROP TABLE IF EXISTS time_slots CASCADE;
    CREATE TABLE time_slots(
        time_slot NUMERIC NOT NULL,
        start_time NUMERIC NOT NULL,
        length NUMERIC NOT NULL,
        PRIMARY KEY (time_slot)
    );
    
    DROP TABLE IF EXISTS facilities CASCADE;
    CREATE TABLE facilities(
        facility_name VARCHAR NOT NULL,
        type FACILITIES_TYPE NOT NULL,
        capacity NUMERIC NOT NULL,
        status BOOLEAN NOT NULL,
        PRIMARY KEY (facility_name)
    );
    
    DROP TABLE IF EXISTS pass_type CASCADE;
    CREATE TABLE pass_type(
        type PASS_TYPES NOT NULL,
        price NUMERIC NOT NULL,
        length NUMERIC NOT NULL
        PRIMARY KEY(type)
    );
    
    DROP TABLE IF EXISTS rentals CASCADE;
    CREATE TABLE rentals(
        rental_id NUMERIC NOT NULL,
        user_id NUMERIC NOT NULL,
        start_date DATE NOT NULL,
        end_date DATE NOT NULL,
        PRIMARY KEY(user_id, start_date, end_date),
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    );

    DROP TABLE IF EXISTS workers CASCADE;
    CREATE TABLE workers(
        user_id NUMERIC NOT NULL,
        position POSITION_TYPE NOT NULL,
        PRIMARY KEY(user_id, position),
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (position) REFERENCES jobs(position)
    );
    
    DROP TABLE IF EXISTS jobs CASCADE;
    CREATE TABLE jobs(
        position POSITION_TYPE NOT NULL, 
        wage NUMERIC NOT NULL,
        PRIMARY KEY (position)
    );
    
    DROP TABLE IF EXISTS equipment_log CASCADE;
    CREATE TABLE equipment_log(
        rental_id NUMERIC NOT NULL,
        equipment_type EQUIPMENT_TYPE NOT NULL,
        PRIMARY KEY(rental_id, equipment_type),
        FOREIGN KEY (rental_id) REFERENCES rentals(rental_id)
    );
    
    DROP TABLE IF EXISTS ski_log CASCADE;
    CREATE TABLE ski_log(
        user_id NUMERIC NOT NULL,
        date DATE NOT NULL,
        time NUMERIC(4) NOT NULL,
        trail_name VARCHAR NOT NULL,
        PRIMARY KEY(user_id, date, time),
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (trail_name) REFERENCES trails(trail_name)
    );
    
    DROP TABLE IF EXISTS lessons CASCADE;
    CREATE TABLE lessons(
        teacher_id NUMERIC NOT NULL,
        user_id NUMERIC NOT NULL,
        date DATE NOT NULL,
        time_slot NUMERIC NOT NULL,
        PRIMARY KEY(teacher_id, user_id, date, time_slot),
        FOREIGN KEY (teacher_id) REFERENCES workers(user_id),
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (time_slot) REFERENCES time_slots(time_slot)
    );
    
    DROP TABLE IF EXISTS conditions CASCADE;
    CREATE TABLE conditions(
        date DATE NOT NULL,
        reporter NUMERIC NOT NULL,
        snowfall NUMERIC,
        primary_surface SURFACE_TYPE,
        secondary_surface SURFACE_TYPE,
        base_depth NUMERIC,
        PRIMARY KEY (date),
        FOREIGN KEY (reporter) REFERENCES workers(user_id)
    );
    
    DROP TABLE IF EXISTS ski_patrol_report CASCADE;
    CREATE TABLE ski_patrol_report(
        user_id NUMERIC NOT NULL,
        date DATE NOT NULL,
        time NUMERIC NOT NULL,
        description VARCHAR NOT NULL,
        PRIMARY KEY (worker_id, date, time),
        FOREIGN KEY (user_id) REFERENCES workers(user_id)
    );
    
    DROP TABLE IF EXISTS passes CASCADE;
    CREATE TABLE passes(
        user_id NUMERIC NOT NULL,
        pass_type PASS_TYPES NOT NULL,
        start_date DATE NOT NULL,
        PRIMARY KEY(user_id, start_date),
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    );
    
   
    DROP TABLE IF EXISTS chair_lifts CASCADE;
    CREATE TABLE chair_lifts(
        name VARCHAR NOT NULL,
        type CHAIR_LIFT_TYPE NOT NULL,
        length NUMERIC NOT NULL,
        num_poles NUMERIC NOT NULL,
        num_chairs NUMERIC NOT NULL,
        status BOOLEAN NOT NULL,
        PRIMARY KEY(name),
        FOREIGN KEY (name) REFERENCES facilities(facility_name)
    );
    
    DROP TABLE IF EXISTS schedule CASCADE;
    CREATE TABLE schedule(
        user_id NUMERIC NOT NULL,
        time_slot NUMERIC NOT NULL,
        date DATE NOT NULL,
        facility_name VARCHAR NOT NULL,
        PRIMARY KEY(user_id, date, time_slot),
        FOREIGN KEY (time_slot) REFERENCES time_slots(time_slot),
        FOREIGN KEY (facility_name) REFERENCES facilities(facility_name),
        FOREIGN KEY (user_id) REFERENCES workers(user_id)
    );
    
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO rwlebl16, knmurp16;

    '''

# every query needs a cursor, a cursor is a reference to the result
# of a query
cur = conn.cursor()
cur.execute(cmd)

conn.commit()
