#!/usr/bin/python3


"""
This script filters states from the database hbtn_0e_0_usa that start with 'N'.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    """
    This block is executed when the script is run directly, not imported.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE states.name "
            "LIKE BINARY 'N%' ORDER BY states.id")

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
