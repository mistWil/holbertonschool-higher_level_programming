#!/usr/bin/python3


"""
This script takes in the name of a state as an
argument and lists all cities of that state.
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
    query = """
    SELECT cities.name 
    FROM cities 
    JOIN states ON cities.state_id = states.id 
    WHERE states.name = %s
"""
    cursor.execute(query, (state_name,))
    """
    Execute the SQL command
    """
