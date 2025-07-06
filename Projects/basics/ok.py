i  = 0
while i<4:
    j =0
    while j<5:
        if i+1==j or j +1 ==4:
            print('o' , end=' ')
        j+=1
    else:
        print('+',end='')
    i+=1
print()