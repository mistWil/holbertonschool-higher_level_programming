#!/usr/bin/python3


"""
This script filters states from the database hbtn_0e_0_usa by user input.
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
    state_name = sys.argv[4]
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

    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                   (state_name,))
    """
    Execute the SQL command
    """

    rows = cursor.fetchall()
    """
    Fetch all the rows
    """

    for row in rows:
        print(row)
        """
        Print each row
        """

    cursor.close()
    """
    Close the cursor
    """
