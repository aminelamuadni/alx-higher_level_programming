#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table
of the 'hbtn_0e_0_usa' database where the name matches the argument.

Usage:
    ./2-my_filter_states.py <mysql username> <mysql password> <database name>
    <state name>
"""


import MySQLdb
import sys


def filter_states_by_input(username, password, db_name, state_name):
    """
    Displays all states with names matching the user input from the database.
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password,
                             db=db_name, charset="utf8")
        cur = db.cursor()
        query = ("SELECT * FROM states WHERE name = '{}' "
                 "ORDER BY id ASC").format(state_name)
        cur.execute(query)
        for row in cur.fetchall():
            if row[1] == state_name:
                print(row)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if db:
            db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        filter_states_by_input(sys.argv[1], sys.argv[2], sys.argv[3],
                               sys.argv[4])
    else:
        print("Usage: ./2-my_filter_states.py <mysql username> "
              "<mysql password> <database name> <state name>")
