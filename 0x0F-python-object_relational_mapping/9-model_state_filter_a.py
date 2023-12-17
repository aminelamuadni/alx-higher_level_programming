#!/usr/bin/python3
"""
This script lists all State objects that contain the letter 'a' from the
database 'hbtn_0e_6_usa'.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def list_states_containing_a(username, password, db_name):
    """
    Lists all states containing the letter 'a' from the database.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name
        )
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name.like('%a%'))
    states_with_a = query.order_by(State.id)

    for state in states_with_a:
        print(f"{state.id}: {state.name}")
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states_containing_a(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: ./9-model_state_filter_a.py <mysql username> "
              "<mysql password> <database name>")
