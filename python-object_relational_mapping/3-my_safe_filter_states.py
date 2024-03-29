#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. Safe from MySQL injections"""
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY
                %s ORDER BY states.id""", (sys.argv[4],))
    fetchs = cur.fetchall()
    for i in fetchs:
        print(i)
    cur.close()
    db.close()
