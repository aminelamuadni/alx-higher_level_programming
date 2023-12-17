#!/usr/bin/python3
"""
This script prints the first State object from the database 'hbtn_0e_6_usa'.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def fetch_first_state(username, password, db_name):
    """
    Fetches and prints the first state from the database.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name
        )
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        fetch_first_state(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: ./8-model_state_fetch_first.py <mysql username> "
              "<mysql password> <database name>")
