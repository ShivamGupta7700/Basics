def cal(n):
    if n == 1:
        return 1
    else:
        return ((n-1)/n)*cal(n-1)


print(cal(20))