class Solution:
    def factorial(self, n:int):
        fact = 1
        for i in range(2, n+1):
            fact *= i

        return fact


def recur_Factorial(n):
    if n == 1:
        return n 
    else:
        temp = recur_Factorial(n-1)
        temp = temp * n
    return temp
    
def recur_Fact(n):
    if n==1: return n
    else: return n*recur_Fact(n-1)

def permute(string, packet = ''):
    if len(string) == 0:
        print(packet)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front +back
            permute(together, letter+packet)


def getPermutation( n, k):
        s = ''.join(str(i) for i in range(1, n + 1))
        def permute(string, packet = ''):
            if len(string) == 0:
                print(packet)
            else:
                for i in range(len(string)):
                    letter = string[i]
                    front = string[0:i]
                    back = string[i+1:]
                    together = front +back
                    permute(together, letter+packet)
        return print(permute(s,''))




print(permute('123',''))