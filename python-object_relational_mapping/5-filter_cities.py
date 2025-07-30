#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
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

    # Execute SQL query with JOIN and parameterized query for SQL injection prevention
    # Using only one execute() call as required
    cursor.execute("""
        SELECT cities.name 
        FROM cities 
        JOIN states ON cities.state_id = states.id 
        WHERE states.name = %s 
        ORDER BY cities.id ASC
    """, (state_name,))

    # Fetch all results
    results = cursor.fetchall()

    # Format and display results as comma-separated values
    if results:
        city_names = [row[0] for row in results]
        print(", ".join(city_names))

    # Close cursor and database connection
    cursor.close()
    db.close()
