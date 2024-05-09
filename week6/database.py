import mysql.connector

# 连接到数据库
mydb = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="rootroot",
    database="website"
)

mycursor = mydb.cursor()

print("Database connected")
