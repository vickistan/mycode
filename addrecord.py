#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","user","password","database" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "Select * from table"
cursor.execute(sql)

last_record = [x[0] for x in cursor.fetchall()][-1]
print "Your last_record is %d" % last_record

question = input('What is the question you would like to add to the database?')
answer = input('What is the answer to this question?')

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO table(id, question, answer) \
       VALUES ('%d', '%s', '%s' )" % \
       (last_record+1, question, answer)

try:
   # Execute the SQL command
   cursor.execute(sql)


   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
