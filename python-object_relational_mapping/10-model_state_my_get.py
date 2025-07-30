#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query State object with the specified name
    # Using filter() for SQL injection protection
    state = session.query(State).filter(State.name == state_name).first()

    # Display result
    if state is None:
        print("Not found")
    else:
        print(state.id)

    # Close the session
    session.close()
