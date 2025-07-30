#!/usr/bin/python3
"""
Script that deletes all State objects'
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get all states first, then delete those containing 'a'
    all_states = session.query(State).all()
    for state in all_states:
        if 'a' in state.name:
            session.delete(state)

    session.commit()
    session.close()
