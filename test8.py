import os
import sqlite3

conn=sqlite3.connect('test.db') #create database test.db
with  conn:  #establish connection with database
    cur=conn.cursor()  #create cur variable so don't have to type conn.cursor() each time
            # cursor() operates the database when a command is given
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT)") #\ key lets you continue in next line
    conn.commit()  #commits changes
conn.close()  #closes the database connection after editing

conn=sqlite3.connect('test.db') 
with  conn:  #establish connection with database again
    cur=conn.cursor()  
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES(?,?,?)", \
                ('Bob', 'Smith', 'bsmith@gmail.com'))
    conn.commit()
conn.close()

conn=sqlite3.connect('test.db') 
with  conn:  #establish connection with database again
    cur=conn.cursor()  
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES(?,?,?)", \
                ('Sarah', 'Jones', 'sjones@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES(?,?,?)", \
                ('Sally', 'May', 'sallymay@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES(?,?,?)", \
                ('kevin', 'bacon', 'kbacon@rocketmail.com'))
    conn.commit()
conn.close()

conn=sqlite3.connect('test.db') #create database test.db
with  conn:  #establish connection with database
    cur=conn.cursor()  #create cur variable so don't have to type conn.cursor() each time
            # cursor() operates the database when a command is given
    cur.execute("SELECT col_fname,col_lname,col_email FROM tbl_persons WHERE col_fname='Sarah'")
    varPerson=cur.fetchall()
    for item in varPerson:
        msg="First Name: ()\nLast Name: ()\nEmail: ()".format(item[0],item[1],item[2])
    print(msg)        




        
