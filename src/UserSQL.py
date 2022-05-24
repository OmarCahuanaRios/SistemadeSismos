import mysql.connector as sql
db=sql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="tdp"
)
cursorUser=db.cursor()
cursorUser.execute("SELECT * FROM user")
dataUsers=cursorUser.fetchall()

print(dataUsers)


def obtenerDistrito(distrito):
    return 