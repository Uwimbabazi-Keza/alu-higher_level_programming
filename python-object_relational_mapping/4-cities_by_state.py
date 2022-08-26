#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""


import sys
import MySQLdb


def cities_by_states():
    """ lists all cities"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.\
        execute("SELECT cities.id, cities.name, states.name FROM cities\
                JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id")
    collection = c.fetchall()
    for state in collection:
        print(state)


if __name__ == "__main__":
    cities_by_states()
