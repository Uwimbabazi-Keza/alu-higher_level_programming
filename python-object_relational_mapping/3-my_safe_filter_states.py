#!/usr/bin/python3
""" SQL injection to delete all records of a table"""


import sys
import MySQLdb


def sql_injection():
    """avoiding MySQL injections"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.\
        execute("SELECT * FROM states WHERE name=%s;\
                ORDER BY id", (sys.argv[4],))
    collection = c.fetchall()
    for states in collection:
        print(states)


if __name__ == "__main__":
    sql_injection()
