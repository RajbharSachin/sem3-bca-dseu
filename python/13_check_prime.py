n=int(input("Enter the number: "))
for i in range(n-1,1,-1):
   if(n%i==0):
      print("Number is not prime")
      break
else:
      print("Number is prime")
      