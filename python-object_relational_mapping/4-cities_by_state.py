#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
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
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor object
    cursor = db.cursor()

    # Execute SQL query with JOIN to get cities with their state names
    # Using only one execute() call as required
    cursor.execute("""
                   SELECT cities.id, cities.name, states.name
                   FROM cities
                   JOIN states ON cities.state_id = states.id
                   ORDER BY cities.id ASC
    """)

    # Fetch all results
    results = cursor.fetchall()

    # Display results
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
