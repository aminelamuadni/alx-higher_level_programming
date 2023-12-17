#!/usr/bin/python3
"""
This script changes the name of the State object with id = 2 to 'New Mexico'
in the database 'hbtn_0e_6_usa'.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def update_state(username, password, db_name):
    """
    Updates the name of the State with id = 2 to 'New Mexico'.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name
        )
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_update = session.query(State).filter(State.id == 2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        update_state(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: ./12-model_state_update_id_2.py <mysql username> "
              "<mysql password> <database name>")
