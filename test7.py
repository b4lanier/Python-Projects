import os
# print(dir(os)) #show all functions available for os
# print(help(os))  #get help with what all os functions do

def openFile():
    with open('test.txt','r') as f:  #function that sets f as "read" "test" file
      data=f.read() #create data var with data from file
      print(data) #print the data from the test file
      f.close() #close the file

def writeData():
    data='\nHello world!'
    with open('test.txt','a') as f: #open test file, write-append at the end of the file
        f.write(data) #write string at end of test file
        f.close()  #close file

if __name__=="__main__":
    writeData()
    openFile()
