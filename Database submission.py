import os
import sqlite3

conn=sqlite3.connect('assignment1.db') #create database assignment1.db
with  conn:  #establish connection with database
    cur=conn.cursor()  #create cur variable so don't have to type conn.cursor() each time
            # cursor() operates the database when a command is given
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_name TEXT)") #\ key lets you continue in next line
    conn.commit()  #commits changes
# don't close DB until after for loop

#create list of file names
fileList=('information.docx','Hello.txt','myImage.png',\
          'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#loop through list to find files ending in .txt
for x in fileList:  #loop through fileList
    if x.endswith('.txt'):   #if txt, insert into DB
        with conn:
            curr=conn.cursor()   #(x,) makes it a single tuple instead of string
            curr.execute("INSERT INTO tbl_files (col_name) VALUES (?)", (x,))
            print(x)   #print what we inserted into the DB
conn.close()
