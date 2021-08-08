#!/usr/bin/python3
"""cript that lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if len(sys.argv) == 4:
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    """Open database connection"""
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")

    """ prepare a cursor object using cursor() method"""
    cur = conn.cursor()
    """ execute SQL query using execute() method."""
    cur.execute(
        "SELECT * FROM states ORDER BY id ASC")

    """Fetch a single row using fetchone() method."""
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    """disconnect from server"""
    cur.close()
    conn.close()

else:
    print("Error - Introduce los argumentos correctamente")
