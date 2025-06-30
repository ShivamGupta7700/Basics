# with open("file/sample.txt", "w+") as file:
#     print(file.tell())
    
#     file.write('I am shivam gupta')
#     file.seek(0)
#     print(file.readline())
#     print(file.tell())
a = 0
with open("file/sample.txt", "r") as file:
    lines = file.readlines()
    for words in lines:
        for letter in words:
            if letter in 'aeiou':
                a+=1

print(a)

