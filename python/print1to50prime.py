n=int(input("Enter the number: "))
print(1)
for i in range(2,n):
   if(n%i==0):
      print("Number is not prime")
      break
else:
      print(i," is prime")
      