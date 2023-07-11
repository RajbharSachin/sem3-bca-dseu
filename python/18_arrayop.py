import array as arr
a = arr.array('i',[1,3,4,6,7,8])
print("First element: ",a[0])
print("Second element: ",a[1])
print("Last element: ",a[-1])
print(a[2:5]) # 2th to 4th position
print(a[:-2]) # start to -3th
print(a[4:]) # 4rth to 5
print(a[:]) # begin to end
a.append(9)
print(a[:])
a.extend([10,11,12])
print(a[:])
a.remove(10)
print(a[:])
a.pop()
print(a[:])
a.pop(1)
print(a[:])

odd = arr.array('i',[1,3,5])
print(a[2:5]) # 2 to 4th
print(a[:-2])
print(a[4:]) # 4 to 5th
print(a[:])  #begin to end
a.append(9)
print(a[:])
a.extend([10,11,12])
print(a[:])
a.remove(10)
print(a[:])
a.pop()
print(a[:])
a.pop(1)
print(a[:])

odd = arr.array('i',[1,3,5])
even = arr.array('i',[2,4,6])

numbers = arr.array('i') # creating empty array of integer
numbers = odd + even 
print(numbers[:])

from array import *
x = [[0,1],[3,4],[5,6]]
# accessing elements of 2D array
print(x[0])
print(x[1][0])
#inserting
x.insert(3,[10,20])

for r in x:
    for c in r:
        print(c," ")

# updating elements of 2d array
x[2] = [30,40]
for r in x:
    for c in r:
        print(c,end=" ")
    print("")
# deleting 2nd row
del x[2]
for r in x:
    for c in r:
        print(c,end=" ")
    print("")
