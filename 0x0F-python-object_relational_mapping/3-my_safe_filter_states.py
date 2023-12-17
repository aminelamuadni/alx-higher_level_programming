#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table
of the 'hbtn_0e_0_usa' database where the name matches the argument, with
protection against SQL injection.

Usage:
    ./3-my_safe_filter_states.py <mysql username> <mysql password>
    <database name> <state name>
"""


import MySQLdb
import sys


def safe_filter_states(username, password, db_name, state_name):
    """
    Displays all states with names matching the user input from the database,
    with protection against SQL injection.
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password,
                             db=db_name, charset="utf8")
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                    (state_name,))
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
    if len(sys.argv) == 5:
        safe_filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Usage: ./3-my_safe_filter_states.py <mysql username> "
              "<mysql password> <database name> <state name>")
