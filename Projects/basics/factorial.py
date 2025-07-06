import math 

num = int(input('Enter the number (n)>>> '))
print('Factorial', math.factorial(num))


#method 2

num1 = int(input('Enter the number (n) >> '))
if num1 > 0 :
    result =1
    
    for i in range(1, num1+1):
        result *= i
    print(result)