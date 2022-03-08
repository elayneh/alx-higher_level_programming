#!/usr/bin/python3
"""Script lists all states from database hbtn_0e_0_usa
Takes three arguments:
    mysql username
    mysql password
    database name
Connects to default host (localhost) and port (3306)
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user='root', passwd='bela@Sware77', db='hbtn_0e_0_usa')
    c = db.cursor()
    c.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
