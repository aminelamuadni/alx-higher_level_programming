#!/usr/bin/python3
"""
This script is designed to connect to a MySQL database and list all the states
in the database. It demonstrates basic usage of the MySQLdb module to interact
with a MySQL database from Python.

Usage:
    ./0-select_states.py <mysql username> <mysql password> <database name>

The script takes three command-line arguments:
- MySQL username
- MySQL password
- Database name

It connects to a MySQL server running on localhost at port 3306, queries
the 'states' table, and prints each state's id and name in ascending order by
id.
"""


import MySQLdb
import sys


def list_states(username, password, db_name):
    """
    Lists all states from the database.
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password,
                             db=db_name, charset="utf8")
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
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
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: ./0-select_states.py <mysql username> "
              "<mysql password> <database name>")
