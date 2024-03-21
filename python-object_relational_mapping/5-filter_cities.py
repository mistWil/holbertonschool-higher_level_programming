#!/usr/bin/python3


"""
This script takes in the name of a state as an
argument and lists all cities of that state.
"""


import MySQLdb
import sys
import os

username = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
database = os.getenv('DB_NAME')


if __name__ == "__main__":

    """
    This block is executed when the script is run directly, not imported.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    """
    Get the command line arguments
    """

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()
    cmd = ("SELECT cities.name FROM cities "
           "INNER JOIN states ON cities.state_id = states.id "
           "WHERE states.name = %s ORDER BY cities.id")
    cursor.execute(cmd, (sys.argv[4],))

    rows = cursor.fetchall()
    to_string = ', '.join(map(" ".join, rows))
    print(to_string)

    db.close()
