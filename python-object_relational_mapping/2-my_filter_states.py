#!/usr/bin/python3
"""script that takes in an argument and
displays all values in the states table of
hbtn_0e_0_usa where name matches the argument."""


import sys
import MySQLdb


def state_name_searched():
    """ values in the states table of
    hbtn_0e_0_usa where name matches the argument.
    """
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.\
            execute("SELECT * FROM states WHERE BINARY name = '{}' \
                   ORDER BY id".format(sys.argv[4]))
    collection = c.fetchall()
    for state in collection:
        print(state)


if __name__ == "__main__":
    state_name_searched()
