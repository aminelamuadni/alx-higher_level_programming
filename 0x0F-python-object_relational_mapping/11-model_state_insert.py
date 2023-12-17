#!/usr/bin/python3
"""
This script adds the State object 'Louisiana' to the database 'hbtn_0e_6_usa'
and prints the new state's id after creation.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def add_louisiana(username, password, db_name):
    """
    Adds the State 'Louisiana' to the database.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name
        )
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        add_louisiana(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: ./11-model_state_insert.py <mysql username> "
              "<mysql password> <database name>")
