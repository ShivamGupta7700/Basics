with open("file/sample.txt", 'r+') as f:
    f.seek(6, 0)
    data = f.read()
    print(data)
    print(f.tell())
    
with open("file/sample.txt", 'w') as f:
    f.write('Hello I am Shivam')