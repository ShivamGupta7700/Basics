#file = open("File_Name","mode")
#default is Read mode

file = open("file/sample.txt","r")
lineFirst = file.readline() 
data = file.read()
print(data)
print(type(data))

file.close()

'''
"r" ----> Read mode.(Default)
"w" ----> Write mode.
"x" ----> Creating new file and open it for writing.
"a" ----> Opening filr for writing, appeding to the end of the file if it exist.
"b" ----> Binary mode.
"t" ----> Text mode.(Default)
"+" ----> updating read and writing.

'''