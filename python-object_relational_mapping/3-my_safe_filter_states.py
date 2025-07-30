#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor object
    cursor = db.cursor()

    # Use parameterized query to prevent SQL injection
    # %s is a placeholder that will be safely replaced by MySQLdb
    cursor.execute("SELECT * FROM states WHERE name = %s "
                   "ORDER BY id ASC", (state_name,))

    # Fetch all results
    results = cursor.fetchall()

    # Display results
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
