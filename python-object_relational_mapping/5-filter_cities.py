#!/usr/bin/python3
"""script that takes in the name of a state as an
argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""


import sys
import MySQLdb


def all_cities_by_state():
    """lists all cities of respective state"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.\
        execute("SELECT * FROM cities JOIN states\
                ON cities.state_id = states.id ORDER BY cities.id")

    collection = c.fetchall()
    for state in collection:
        print(', '.join(state))


if __name__ == "__main__":
    all_cities_by_state()
