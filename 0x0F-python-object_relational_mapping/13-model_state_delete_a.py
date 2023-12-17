#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter 'a'
from the database 'hbtn_0e_6_usa'.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def delete_states_containing_a(username, password, db_name):
    """
    Deletes all states with names containing the letter 'a'.
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
    states_to_delete = query.all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        delete_states_containing_a(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: ./13-model_state_delete_a.py <mysql username> "
              "<mysql password> <database name>")
