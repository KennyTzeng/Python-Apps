import sqlite3

conn = sqlite3.connect("api")

# create table
'''
sql_create = "CREATE TABLE Accounts (\
            id integer primary key AUTOINCREMENT,\
            name varchar(255) NOT NULL,\
            email varchar(255) NOT NULL\
            );"
conn.execute(sql_create)
conn.commit()
'''

cursor = conn.cursor()
sql_select = "select * from Accounts"
cursor.execute(sql_select)
result = cursor.fetchall()

print("show the table : ")
for row in result:
    print("{} {} {}".format(row[0], row[1],row[2]))

print("====================")

print("register an account : ")
name = input("input your name : ")
email = input("input your email : ")
sql_insert = "insert into Accounts (name, email) values ('{}', '{}')".format(name, email)
conn.execute(sql_insert)
conn.commit()

conn.close()