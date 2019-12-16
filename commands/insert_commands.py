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
(3, 600, 4),
(4, 900, 5),
(5, 1300, 3),
(6, 1200, 5),
(7, 1700, 5);

INSERT
INTO
users
VALUES
(1, 'knmurp16@stlawu.edu ', 'Kira', 'Murphy'),
(2, 'jbpeek16@stlawu.edu', 'Jonas', 'Peek'),
(3, 'rwlebl16@stlawu.edu', 'Remi', 'LeBlanc'),
(4, 'twjone16@stlawu.edu', 'Tim', 'Jones'),
(5, 'edharcourt@stlawu.edu', 'Ed', 'Harcourt'),
(6, 'jepatt16@stlawu.edu', 'Jack', 'Pattison'),
(7, 'dmsteh16@stlawu.edu', 'David', 'Stehle');

INSERT
INTO
workers
VALUES
(1, 'owner', 100000),
(2,'ski_patrol', 20),
(5,'instructor', 20),
(7,'chairlift_operator', 20),
(3,'cook', 15);

INSERT
INTO
skiers
VALUES
(2),
(7),
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
('Wild Air', 'difficult', 'terrain_park', 1000, false),
('Twister Glades', 'difficult', 'glades', 300, false),
('Crystal', 'intermediate', 'moguls', 150, true),
('The gully', 'intermediate', 'groomer', 4400, true),
('Little Dipper', 'intermediate', 'groomer', 800, true),
('Lower Sunway', 'easy', 'groomer', 3800, true),
('Sunway', 'easy', 'groomer', 4200, true),
('Twister', 'intermediate', 'moguls', 3800, true),
('Lies', 'very_difficult', 'moguls', 2600, false),
('Open Pit', 'difficult', 'moguls', 1300, true),
('Hawk Eye', 'difficult', 'moguls', 3800, false),
('Powder Pass', 'intermediate', 'groomer', 3800, true);

INSERT
INTO
facilities
VALUES
('Base Lodge', 'lodge', 20, true),
('Northwoods Lodge', 'lodge', 20, false),
('Patrol Hut', 'ski_patrol_hut', 15, true),
('Saddle Lodge', 'lodge', 20, true),
('Straight Brook Lodge', 'lodge', 6, true),
('Warming Hut', 'lodge', 4, true),
('Tannery Pub', 'bar', 6, false),
('Ski School', 'ski_school', 40, false),
('Express Quad', 'chairlift', 5, true),
('Burnt Ridge Quad', 'chairlift', 5, true),
('Adirondack Express II', 'chairlift', 5, true),
('Hudson Chair', 'chairlift', 5, true),
('Cloud Splitter', 'chairlift', 5, false),
('Northwoods Gondola', 'chairlift', 5, true);

INSERT
INTO
rental_log
VALUES
(1, 'skis', '2019-12-12', '2019-12-13'),
(2, 'poles', '2019-12-12', '2019-12-13'),
(3, 'ski_boots', '2019-12-12', '2019-12-13'),
(4, 'helmet', '2019-12-12', '2019-12-13'),
(5, 'goggles', '2019-12-12', '2019-12-13'),
(6, 'snowboard', '2019-12-15', '2019-12-15'),
(7, 'snowboard_boots', '2019-12-15', '2019-12-15'),
(8, 'helmet', '2019-12-15', '2019-12-15'),
(9, 'goggles', '2019-12-15', '2019-12-15'),
(10, 'skis', '2019-12-15', '2019-1-26'),
(11, 'ski_boots', '2019-12-15', '2019-1-26'),
(12, 'skis', '2019-12-28', '2019-12-30'),
(13, 'poles', '2019-12-28', '2019-12-30'),
(14, 'ski_boots', '2019-12-28', '2019-12-30'),
(15, 'helmet', '2019-12-28', '2019-12-30'),
(16, 'goggles', '2019-12-28', '2019-12-30');

INSERT
INTO
rentals
VALUES
(4, 1),
(4, 2),
(4, 3),
(4, 4),
(4, 5),
(4, 12),
(4, 13),
(4, 14),
(4, 15),
(4, 16),
(6, 6),
(6, 7),
(6, 8),
(6, 9),
(4, 10),
(4, 11);

INSERT
INTO
ski_log
VALUES
(5, '2019-12-12', 930, 'Ruby Run'),
(5, '2019-12-12', 950, 'Ruby Run'),
(5, '2019-12-12', 1020, 'Lower Sunway'),
(5, '2019-12-12', 1045, 'Sunway'),
(5, '2019-12-12', 1134, 'Showcase'),
(5, '2019-12-12', 1330, 'The gully'),
(5, '2019-12-12', 1355, 'Showcase'),
(5, '2019-12-12', 1428, 'The gully'),
(5, '2019-12-12', 1458, 'Open Pit'),
(4, '2019-12-13', 903, 'Wild Air'),
(4, '2019-12-13', 928, 'Wild Air'),
(4, '2019-12-13', 959, 'Wild Air'),
(4, '2019-12-13', 1013, 'Wild Air'),
(4, '2019-12-13', 1038, 'Wild Air'),
(4, '2019-12-13', 1102, 'Wild Air'),
(4, '2019-12-13', 1139, 'Wild Air'),
(6, '2019-12-15', 905, 'The Rumor'),
(6, '2019-12-15', 942, 'Open Pit'),
(6, '2019-12-15', 1030, 'The Rumor'),
(6, '2019-12-15', 1057, 'Twister Glades'),
(6, '2019-12-15', 1129, 'Showcase'),
(6, '2019-12-15', 1205, 'Showcase'),
(6, '2019-12-15', 1340, 'The Rumor'),
(6, '2019-12-15', 1405, 'Hawk Eye'),
(5, '2019-12-28', 930, 'Ruby Run'),
(5, '2019-12-28', 954, 'Twister Glades'),
(5, '2019-12-28', 1020, 'Hawk Eye'),
(5, '2019-12-28', 1045, 'Sunway'),
(5, '2019-12-28', 1136, 'Showcase'),
(5, '2019-12-28', 1339, 'Twister Glades'),
(5, '2019-12-28', 1355, 'Hawk Eye'),
(5, '2019-12-28', 1420, 'The gully'),
(5, '2019-12-28', 1458, 'Open Pit'),
(5, '2019-12-29', 930, 'Ruby Run'),
(5, '2019-12-29', 950, 'Hawk Eye'),
(5, '2019-12-29', 1015, 'Twister Glades'),
(5, '2019-12-29', 1045, 'Open Pit'),
(5, '2019-12-29', 1137, 'Hawk Eye'),
(5, '2019-12-29', 1333, 'The gully'),
(5, '2019-12-29', 1355, 'Twister Glades'),
(5, '2019-12-29', 1420, 'Hawk Eye'),
(5, '2019-12-29', 1446, 'Hawk Eye'),
(5, '2019-12-29', 1512, 'Open Pit'),
(7, '2019-2-25', 930, 'Ruby Run'),
(7, '2019-2-25', 950, 'Ruby Run'),
(7, '2019-2-25', 1020, 'Lower Sunway'),
(7, '2019-2-25', 1045, 'Sunway'),
(7, '2019-2-25', 1134, 'Showcase'),
(7, '2019-2-25', 1330, 'The gully'),
(7, '2019-2-25', 1355, 'Showcase'),
(7, '2019-2-25', 1428, 'The gully'),
(7, '2019-2-25', 1458, 'Open Pit');

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
(3, 'senior', '2019-12-12', '2019-12-12'),
(4, 'season', '2019-12-08', '2019-05-30'),
(5, 'season', '2019-11-25', '2019-05-30');

INSERT
INTO
passes
VALUES
(1, 4),
(2, 6),
(3, 5),
(4, 7),
(5, 2);

INSERT
INTO
chair_lifts
VALUES
('Express Quad', 'quad', 100, 10, 100, true),
('Burnt Ridge Quad', 'quad', 386, 17, 118, true),
('Adirondack Express II', 'quad', 391, 19, 126, true),
('Hudson Chair', 'triple', 317, 13, 97, true),
('Cloud Splitter', 'gondola', 237, 15, 134, false),
('Northwoods Gondola', 'gondola', 400, 20, 100, true);

INSERT
INTO
schedule
VALUES
('Base Lodge', 3, '2019-12-25', 2),
('Base Lodge', 3, '2019-12-26', 2),
('Base Lodge', 3, '2019-12-27', 2),
('Base Lodge', 3, '2019-12-28', 2),
('Base Lodge', 3, '2019-12-29', 2),
('Base Lodge', 3, '2019-12-30', 2),
('Base Lodge', 3, '2019-12-31', 2),
('Base Lodge', 3, '2020-1-1', 2),
('Base Lodge', 3, '2019-12-25', 5),
('Base Lodge', 3, '2019-12-26', 5),
('Base Lodge', 3, '2019-12-27', 5),
('Base Lodge', 3, '2019-12-28', 5),
('Base Lodge', 3, '2019-12-29', 5),
('Base Lodge', 3, '2019-12-30', 5),
('Base Lodge', 3, '2019-12-31', 5),
('Base Lodge', 3, '2020-1-1', 5),
('Patrol Hut', 2, '2020-1-1', 3),
('Patrol Hut', 2, '2020-1-2', 3),
('Patrol Hut', 2, '2020-1-4', 3),
('Patrol Hut', 2, '2020-1-6', 3),
('Patrol Hut', 2, '2020-1-7', 3),
('Patrol Hut', 2, '2020-1-8', 3),
('Patrol Hut', 2, '2020-1-10', 3),
('Patrol Hut', 2, '2020-1-11', 3),
('Patrol Hut', 2, '2020-1-12', 3),
('Patrol Hut', 2, '2020-1-14', 3),
('Express Quad', 7, '2019-12-29', 2),
('Express Quad', 7, '2019-12-30', 5),
('Northwoods Gondola', 7, '2019-12-31', 5),
('Adirondack Express II', 7, '2020-1-1', 2),
('Adirondack Express II', 7, '2020-1-1', 5),
('Northwoods Gondola', 7, '2020-1-2', 2),
('Express Quad', 7, '2020-1-4', 2),
('Adirondack Express II', 7, '2020-1-6', 2),
('Express Quad', 7, '2020-1-7', 5),
('Northwoods Gondola', 7, '2020-1-8', 5),
('Express Quad', 7, '2020-1-10', 5),
('Adirondack Express II', 7, '2020-1-11', 2),
('Northwoods Gondola', 7, '2020-1-12', 2),
('Express Quad', 7, '2020-1-14', 5),q
('Ski School', 5, '2020-01-02', 5),
('Ski School', 5, '2020-01-03', 5),
('Ski School', 5, '2020-01-04', 5),
('Ski School', 5, '2020-01-05', 5),
('Ski School', 5, '2020-01-06', 5),
('Ski School', 5, '2020-01-07', 5),
('Ski School', 5, '2020-01-08', 5),
('Ski School', 5, '2020-01-09', 5),
('Ski School', 5, '2020-01-10', 5),
('Ski School', 5, '2020-01-11', 5),
('Ski School', 5, '2020-01-12', 5),
('Ski School', 5, '2020-01-13', 5),
('Ski School', 5, '2020-01-14', 5),
('Ski School', 5, '2020-01-15', 5);

INSERT
INTO
conditions
VALUES
('2019-12-12', 1, 3, 'packed_powder', 'powder', 5),
('2019-12-25', 1, 0, 'packed_powder', 'powder', 8),
('2019-12-31', 2, 10, 'powder', 'packed_powder', 18),
('2020-01-01', 2, 2, 'powder', 'packed_powder', 20),
('2020-01-02', 2, 0, 'packed_powder', 'packed_powder', 20),
('2020-01-03', 2, 0, 'packed_powder', 'packed_powder', 20),
('2020-01-04', 2, 7, 'powder', 'packed_powder', 27),
('2020-01-05', 1, 0, 'powder', 'packed_powder', 27),
('2020-01-06', 2, 12, 'powder', 'powder', 39),
('2020-01-07', 2, 4, 'powder', 'powder', 43),
('2020-01-08', 2, 1, 'powder', 'packed_powder', 44),
('2020-01-09', 2, 0, 'packed_powder', 'packed_powder', 44),
('2020-01-10', 1, 0, 'packed_powder', 'packed_powder', 44),
('2020-01-11', 1, 0, 'packed_powder', 'frozen_granular', 44),
('2020-01-12', 2, 0, 'packed_powder', 'frozen_granular', 44),
('2020-01-13', 2, 0, 'packed_powder', 'frozen_granular', 44),
('2020-01-14', 1, 0, 'packed_powder', 'frozen_granular', 44),
('2020-01-15', 1, 0, 'packed_powder', 'frozen_granular', 44),
('2020-01-16', 2, 0, 'packed_powder', 'frozen_granular', 44),
('2020-01-17', 2, 0, 'frozen_granular', 'frozen_granular', 44),
('2020-01-18', 1, 0, 'frozen_granular', 'frozen_granular', 44),
('2020-01-19', 1, 0, 'frozen_granular', 'frozen_granular', 44),
('2020-01-20', 2, 0, 'frozen_granular', 'frozen_granular', 44),
('2020-01-21', 2, 3, 'powder', 'frozen_granular', 47),
('2020-01-22', 2, 6, 'powder', 'packed_powder', 53),
('2020-01-22', 2, 2, 'powder', 'powder', 55),
('2020-01-22', 2, 7, 'powder', 'powder', 62),
('2020-01-22', 2, 3, 'powder', 'powder', 65);

INSERT
INTO
ski_patrol_report
VALUES
(2, '2019-12-25', 950,'Broken arm halfway down Showcase. Skier was transported to the base via a toboggan.'),
(2, '2019-12-12', 1200, 'Unexperienced skier unable to make their way down the trail on Lies, snow mobile was called to 
transport skier to the base.'),
(2, '2019-12-13', 1000, 'Concussion on Lies, the skier was transported to the base via toboggan.'),
(2, '2019-12-14', 1100, 'Hurt knee on Wild Air. Skier was transported to the base via a toboggan for further inspection.'),
(2, '2019-12-13', 1350, 'Skier hit tree on Twister Glades, they appear to be fine but were frightened. Advised to go home.')
(2, '2020-01-25', 950,'Broken arm halfway down Showcase. Skier was transported to the base via a toboggan.'),
(2, '2020-02-12', 1200, 'Unexperienced skier unable to make their way down the trail on Lies, snow mobile was called to 
transport skier to the base.'),
(2, '2020-02-13', 1000, 'Concussion on Lies, the skier was transported to the base via toboggan.'),
(2, '2020-02-16', 1100, 'Hurt leg on Wild Air. Skier was transported to the base via a toboggan for further inspection.'),
(2, '2020-03-03', 1350, 'Skier hit tree on Twister Glades, they appear to be fine but were frightened. Advised to go home.');

INSERT
INTO
lessons
VALUES
(5, 4, '2020-01-02', 5),
(5, 4, '2020-01-03', 5),
(5, 4, '2020-01-04', 5),
(5, 4, '2020-01-05', 5),
(5, 4, '2020-01-06', 5),
(5, 4, '2020-01-07', 5),
(5, 4, '2020-01-08', 5),
(5, 4, '2020-01-09', 5),
(5, 4, '2020-01-10', 5),
(5, 4, '2020-01-11', 5),
(5, 4, '2020-01-12', 5),
(5, 4, '2020-01-13', 5),
(5, 4, '2020-01-14', 5),
(5, 4, '2020-01-15', 5),
(5, 6, '2020-02-02', 5),
(5, 6, '2020-02-03', 5),
(5, 6, '2020-02-04', 5),
(5, 6, '2020-02-05', 5),
(5, 6, '2020-02-06', 5),
(5, 6, '2020-02-07', 5),
(5, 6, '2020-02-08', 5),
(5, 6, '2020-02-09', 5),
(5, 6, '2020-02-10', 5),
(5, 6, '2020-02-11', 5),
(5, 6, '2020-02-12', 5),
(5, 6, '2020-02-13', 5),
(5, 6, '2020-02-14', 5),
(5, 6, '2020-02-15', 5);

'''

# of a query
cur = conn.cursor()
cur.execute(commands)

conn.commit()
