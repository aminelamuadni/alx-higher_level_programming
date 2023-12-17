#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N' from the database
'hbtn_0e_0_usa'. It uses the MySQLdb module to connect to a MySQL database,
and prints each relevant state's id and name in ascending order by id.

Usage:
    ./1-filter_states.py <mysql username> <mysql password> <database name>
"""


import MySQLdb
import sys


def filter_states(username, password, db_name):
    """
    Lists all states with names starting with 'N' from the database.
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password,
                             db=db_name)
        cur = db.cursor()
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cur.execute(query)
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
        filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: ./1-filter_states.py <mysql username> "
              "<mysql password> <database name>")
