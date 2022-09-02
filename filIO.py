import os

fileName='test.txt'
filePath='C:\\Users\\b4lan\\OneDrive\\Documents\\GitHub\\Python-Projects\\'
 #need two escape characters in the path for it to work right

dirList=os.listdir(filePath)  #list all files in directory
print(dirList)
abPath=os.path.join(filePath,fileName)  #concat path and file name
print(abPath)
for i in dirList:
    #getting error, can't create list with str?
    thisPath=os.path.join(filePath,dirList[i])
    modTime=os.path.getmtime(thisPath)
    print("{} {}".format(dirList[i], modTime))

