import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="kodokushi",
  database="movies"
)

mycursor = mydb.cursor()

sql = "INSERT INTO movies (title, genre,director,release_year) VALUES (%s, %s,%s,%s)"
val = ("Batman", "Terror", "Nolan", 2009
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")