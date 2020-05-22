
import mysql.connector

db = mysql.connector.connect(host="localhost", user="test", passwd="pas", database="test2")
crs = db.cursor()
cmd = "INSERT INTO three_fields (name, owner) VALUES (%s, %s)"
val = [
    ("xps13", 'Eugene'),
    ("xps15", 'Alex')
]
crs.executemany(cmd, val)
db.commit()
