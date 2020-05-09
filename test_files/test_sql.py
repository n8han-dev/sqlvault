
import mysql.connector

db = mysql.connector.connect(host="localhost", user="test", passwd="pas", database="test_python")
crs = db.cursor()
cmd = "INSERT INTO test1 (name) VALUES (%s)"
val = ['nusha']
crs.executemany(cmd, val)
db.commit()
print(crs.rowcount, "record inserted.")
crs.execute("SELECT * FROM test1")
for x in crs:
    print(x)
