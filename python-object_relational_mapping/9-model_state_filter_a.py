#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter 'a'
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

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query State objects that contain the letter 'a' in their name
    # Filter states where name contains 'a', ordered by id
    states = session.query(State).filter(State.name.contains('a')) \
        .order_by(State.id).all()

    # Display results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
