#!/usr/bin/python3


"""Write a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """including the guard clause"""

    """connection to the MySQLdb database"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3])

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE states.name = %s ORDER BY states.id",
        (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db.close()
