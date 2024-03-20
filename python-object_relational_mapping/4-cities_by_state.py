#!/usr/bin/python3


"""
This script lists all cities from the database hbtn_0e_4_usa.
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

    """
    Get the command line arguments
    """

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    """
    Establish a database connection
    """

    cursor = db.cursor()
    """
    Get the cursor
    """

    cursor.execute()

    """
    Execute the SQL command
    """