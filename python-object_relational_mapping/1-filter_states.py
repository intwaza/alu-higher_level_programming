#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
       user=sys.argv[1],
       password=sys.argv[2],
       db=sys.argv[3],
       host="localhost",
       port=3306
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states \
        WHERE name LIKE BINARY 'N%' \
        ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
