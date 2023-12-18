#!/usr/bin/python3
"""
This script lists all City objects from the database 'hbtn_0e_101_usa'.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


def list_cities(username, password, db_name):
    """
    Lists all City objects and the State object linked to each City.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name
        )
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: ./102-relationship_cities_states_list.py "
              "<mysql username> <mysql password> <database name>")
