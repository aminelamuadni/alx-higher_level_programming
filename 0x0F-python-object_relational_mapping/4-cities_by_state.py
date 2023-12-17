#!/usr/bin/python3
"""
This script lists all cities along with their corresponding state names
from the 'hbtn_0e_4_usa' database. It demonstrates joining tables and sorting
results.

Usage:
    ./4-cities_by_state.py <mysql username> <mysql password> <database name>
"""


import MySQLdb
import sys


def list_cities(username, password, db_name):
    """
    Lists all cities along with state names from the database.
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password,
                             db=db_name, charset="utf8")
        cur = db.cursor()
        cur.execute("SELECT cities.id, cities.name, states.name "
                    "FROM cities JOIN states ON cities.state_id = states.id "
                    "ORDER BY cities.id ASC")
        for row in cur.fetchall():
            print(row)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if db:
            db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: ./4-cities_by_state.py <mysql username> "
              "<mysql password> <database name>")
