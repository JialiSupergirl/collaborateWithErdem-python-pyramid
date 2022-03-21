import mariadb

def getConnection():
    dbConn = mariadb.connect( host="localhost", user="root", password="", database= "w11")
    cur = dbConn.cursor()
    return cur

def closeConn(cur):
    cur.close()