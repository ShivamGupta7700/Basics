# String and its all functions

# name = 'ShivamGupta'
# print(name[7:2:-1])


# s0 = 'ABCDE'
# for i in range(1, len(s0)+1):
#     print(s0[:i])



# s1 ='ABCDE'
# for i in range(len(s1)):
#     for j in range(i+1):
#         print(s1[j], end='')
#     print()

String = input('Enter your thoughts >>>> ')
sub = 'sh'
print('capitalize()',String.capitalize())
print('count()',String.count(sub,0 , 10)) # count(substring, start, stop) 
print('find()',String.find(sub))               # find(substring, start, stop) return -1 if string not found
print('index()',String.index(sub))            #index(substring, start, stop) gives the index of the substring
print('isalnum()',String.isalnum())
print('isdigit()',String.isdigit())
print('islower()',String.islower())
print('isupper()',String.isupper())
print('lower()',String.lower())
print('upper()',String.upper())
print('lstrip()',String.lstrip())  # similar r/l/strip
print('startwith()',String.startswith(sub))  
# print('endwith()',String.endswith())  
print('title()',String.title())  
print('istitle()',String.istitle())
print('replace()',String.replace())  #replace(old sub , to new sub)
print('split()',String.split())         # list output 
print('partition()',String.partition('sh'))



