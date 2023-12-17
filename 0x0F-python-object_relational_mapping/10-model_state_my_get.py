#!/usr/bin/python3
"""
This script prints the State object with the specified name from the
database 'hbtn_0e_6_usa'.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def get_state(username, password, db_name, state_name):
    """
    Prints the State object with the specified name from the database.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name
        )
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        get_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Usage: ./10-model_state_my_get.py <mysql username> "
              "<mysql password> <database name> <state name>")
