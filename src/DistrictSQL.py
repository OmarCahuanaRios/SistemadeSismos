import mysql.connector as sql
db=sql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="tdp"
)

cursorDistrict=db.cursor()
cursorDistrict.execute("SELECT * FROM distrito")
dataDistricts=cursorDistrict.fetchall()
print(dataDistricts)