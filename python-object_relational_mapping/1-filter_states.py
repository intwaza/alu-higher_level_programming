#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server on localhost at port 3306
    db = MySQLdb.connect(
       user=sys.argv[1],
       password=sys.argv[2],
       db=sys.argv[3],
       host="localhost",
       port=3306
    )

    # Create cursor object
    cursor = db.cursor()

    # Execute SQL query to select states starting with 'N' ordered by id
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all results
    results = cursor.fetchall()

    # Display results
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
