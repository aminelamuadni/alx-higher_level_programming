#!/usr/bin/python3
"""
This script creates the State 'California' with the City 'San Francisco'
in the database 'hbtn_0e_100_usa'.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


def create_state_and_city(username, password, db_name):
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name
        )
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    session.add(new_state)
    session.commit()
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        create_state_and_city(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: ./100-relationship_states_cities.py <mysql username> "
              "<mysql password> <database name>")
