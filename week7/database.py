import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="rootroot",
    database="website"
)

mycursor = mydb.cursor()

print("Database connected")
