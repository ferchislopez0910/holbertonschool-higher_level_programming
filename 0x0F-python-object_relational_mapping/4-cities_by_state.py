#!/usr/bin/python3
"""cript that lists all states from the database hbtn_0e_0_usa"""

from sys import argv
import MySQLdb
if __name__ == "__main__":
    if len(argv) == 4:
        username = argv[1]
        password = argv[2]
        database = argv[3]
        server = "localhost2"
        """Open database connection"""
        conn = MySQLdb.connect(host=server, port=3306, user=username,
                               passwd=password, db=database, charset="utf8")

        """ prepare a cursor object using cursor() method"""
        cur = conn.cursor()
        """ execute SQL query using execute() method."""
        cur.execute(
            "SELECT cities.id,cities.name, states.name FROM  \
                cities INNER JOIN states ON cities.state_id =  \
                    states.id ORDER BY id ASC")

        """Fetch a single row using fetchone() method."""
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

        """disconnect from server"""
        cur.close()
        conn.close()

    else:
        print("Error - Introduce los argumentos correctamente")
