#!/usr/bin/python3
"""script that lists all states
from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

def states():
    """list of states"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id")
    collection = c.fetchall()
    for state in collection:
        print(state)

if __name__ == "__main__":
    states()
