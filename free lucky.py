def factorial(n):
    for i in range (1,n):
        factorial(0)=1
        factorial(i)=i * factorial(i-1)
    return factorial(n)
    





print factorial(0)
#>>> 1

print factorial(5)
#>>> 120

print factorial(10)
#>>> 3628800
