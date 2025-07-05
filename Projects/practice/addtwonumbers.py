
def addTwoNumbers(l1:list, l2:list):
    m = ''
    n = ''
    
    l1.reverse()
    for digit in l1:
        digit = str(digit)
        m += digit
    l2.reverse()
    for digit in l2:
        digit = str(digit)
        n += digit
    
    a = int(m)
    b = int(n)
    l3=[]
    c = a+b
    c = str(c)
    for digits in c:
        digit = str(digits)
        l3.append(digits)
    l3.reverse()

    return l3

print(addTwoNumbers([1,0,2],[3,5,6]))
