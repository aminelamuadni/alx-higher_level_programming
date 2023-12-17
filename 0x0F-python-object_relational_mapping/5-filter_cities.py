#!/usr/bin/python3
"""
This script takes the name of a state as an argument and lists all cities of
that state from the 'hbtn_0e_4_usa' database, ensuring protection against
SQL injection.

Usage:
    ./5-filter_cities.py <mysql username> <mysql password> <database name>
    <state name>
"""


import MySQLdb
import sys


def list_cities_by_state(username, password, db_name, state_name):
    """
    Lists all cities of a given state from the database, SQL injection free.
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password,
                             db=db_name, charset="utf8")
        cur = db.cursor()
        cur.execute("SELECT cities.name FROM cities "
                    "JOIN states ON cities.state_id = states.id "
                    "WHERE states.name = %s "
                    "ORDER BY cities.id ASC", (state_name,))
        cities = [row[0] for row in cur.fetchall()]
        print(", ".join(cities))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if db:
            db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        list_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3],
                             sys.argv[4])
    else:
        print("Usage: ./5-filter_cities.py <mysql username> "
              "<mysql password> <database name> <state name>")
