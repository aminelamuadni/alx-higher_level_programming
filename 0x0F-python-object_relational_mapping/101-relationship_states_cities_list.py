#!/usr/bin/python3
"""
This script lists all State objects, and corresponding City objects,
contained in the database 'hbtn_0e_101_usa'.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
import sys


def list_states_and_cities(username, password, db_name):
    """
    Lists all State objects and their corresponding City objects from the
    database.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states_and_cities(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: ./101-relationship_states_cities_list.py "
              "<mysql username> <mysql password> <database name>")
