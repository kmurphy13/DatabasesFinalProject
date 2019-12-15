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


commands = '''
INSERT
INTO
time_slots
VALUES
(1, 800, 8),
(2, 800, 4),
(3, 1200, 5);

INSERT
INTO
users
VALUES
(1, 'knmurp16@stlawu.edu ', 'Kira', 'Murphy'),
(2, 'jbpeek16@stlawu.edu', 'Jonas', 'Peek'),
(3, 'rwlebl16@stlawu.edu', 'Remi', 'LeBlanc'),
(4, 'twjone16@stlawu.edu', 'Tim', 'Jones'),
(5, 'edharcourt@stlawu.edu', 'Ed', 'Harcourt'),
(6, 'jepatt16@stlawu.edu', 'Jack', 'Pattison');

INSERT
INTO
workers
VALUES
(1, 'owner', 100000),
(2,'ski_patrol', 20),
(3,'chairlift_operator', 15);

INSERT
INTO
data_base_manager
VALUES
(1),
(2),
(3);


INSERT
INTO
skiers
VALUES
(4),
(5),
(6);

INSERT
INTO
trails
VALUES
('The Rumor', 'very_difficult', 'groomer', 500, true),
('Ruby Run', 'easy', 'groomer', 1600, true),
('Showcase', 'intermediate', 'groomer', 2000, true),
('Wild Air', 'difficult', 'terrain_park', 1000, false);

INSERT
INTO
facilities
VALUES
('Base Lodge', 'lodge', 500, true),
('Northwoods Lodge', 'lodge', 200, false),
('Patrol Hut', 'ski_patrol_hut', 15, true),
('Tannery Pub', 'bar', '150', false);

INSERT
INTO
rental_log
VALUES
(1, 'skis', '12/12/2019', '2019-12-13'),
(2, 'snowboard', '12/15/2019', '2019-12-15'),
(3, 'ski_boots', '12/15/2019', '2019-12-15');

INSERT
INTO
rentals
VALUES
(6, 1),
(4, 2),
(4, 3);

INSERT
INTO
ski_log
VALUES
(6, '2019-12-15', 0805, 'The Rumor'),
(6, '2019-12-15', 1030, 'Showcase'),
(4, '2019-12-13', 0900, 'Wild Air');

INSERT
INTO
pass_type
VALUES
('season', 300),
('day', 75),
('half_day', 40),
('student', 60),
('child', 30),
('senior', 30);

INSERT
INTO
pass_log
VALUES
(1, 'season', '2019-11-29', '2020-05-30'),
(2, 'half_day', '2019-12-12', '2019-12-12'),
(3, 'senior', '2019-12-12, '2019-12-12');

INSERT
INTO
passes
VALUES
(1, 4),
(2, 6),
(3, 5);

INSERT
INTO
chair_lifts
VALUES
('Express Quad', 'quad', 100, 10, 100, true),
('Cloud Splitter', 'gondola', 237, 15, 134, false),
('Northwoods Gondola', 'gondola', 400, 20, 100, true);

INSERT
INTO
schedule
VALUES
('Base Lodge', 1, '2019-12-25', 1),
('Tannery Pub', 2, '2019-12-12', 2),
('Patrol Hut', 3, '2019-12-12', 3);

INSERT
INTO
conditions
VALUES
('2019-12-12', 1, 3, 'packed_powder', 'powder', 5),
('2019-12-25', 1, 0, 'packed_powder', 'powder', 8),
('2019-12-31', 2, 10, 'powder', 'packed_powder', 20);

INSERT
INTO
ski_patrol_report
VALUES
(2, '2019-12-25', 800,'Merry Christmas!'),
(1, '2019-12-12', 1200, 'Blue bird day.'),
(1, '2019-12-13', 800, 'All good.');

INSERT
INTO
lessons
VALUES
(2, 4,'2019-12-12', 2),
(2, 6, '2019-12-12', 3),
(2, 6, '2019-12-13', 3);
'''

# of a query
cur = conn.cursor()
cur.execute(commands)

conn.commit()
