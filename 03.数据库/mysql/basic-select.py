# pip install MySQL-Python

import MySQLdb
db = MySQLdb.connect("localhost", "root", "123456", "test_db", charset='utf8')
cursor = db.cursor()

sql = "SELECT * FROM users WHERE name = '%s' and password = '%s'" % ('robin', '123456')
try:
   cursor.execute(sql)
   results = cursor.fetchall()
   for row in results:
      a = row[0]
      b = row[1]
      print a, b
except:
   print "Error: unable to fecth data"

db.close()