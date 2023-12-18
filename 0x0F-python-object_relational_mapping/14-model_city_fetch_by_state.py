#!/usr/bin/python3
"""
This script prints all City objects from the database 'hbtn_0e_14_usa'.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from model_state import Base, State
from model_city import City
import sys


def list_cities_by_state(username, password, db_name):
    """
    Prints all City objects from the database.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name
        )
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).join(State).order_by(City.id).all()
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: ./14-model_city_fetch_by_state.py <mysql username> "
              "<mysql password> <database name>")
