add = lambda n,m:n+m
print(add(14,14))

l = [25,14,23,78,68]
even = list(filter(lambda x:x%2==0,l))
print(even)

lis= [2,4,5,10]
power=  list(map(lambda x:x**2,lis))
print(power)


import functools 
lis = [2,9,6,8,4,5,78]
print(functools.reduce(lambda a,b: a+b, lis))
print(functools.reduce(lambda a,b:a if a>b else b, lis))