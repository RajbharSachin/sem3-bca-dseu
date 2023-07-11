import mysql.connector

# creating connection object 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password= "aqua_g_aming"
)

# printing the connection object
print(mydb)



mycursor = mydb.cursor() # fn object to execute commands
#mycursor.execute("CREATE DATABASE mydb1")
mycursor.execute("SHOW DATABASES")

mycursor.execute("")
for x in mycursor:
    print(x)



