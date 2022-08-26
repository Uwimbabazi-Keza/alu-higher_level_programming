#!/usr/bin/python3
"""
script that lists all states with a
name starting with N (upper N) from the
database hbtn_0e_0_usa
"""


import sys
import MySQLdb


def states_starting_with_N():
    """
    lists states starting with N
    """
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'" "ORDER BY id")
    collect_N_states = c.fetchall()
    for state in collect_N_states:
        print(state)


if __name__ == "__main__":
    states_starting_with_N()
