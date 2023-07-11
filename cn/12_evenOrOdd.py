# Parity is no. of 1's

# Function to check odd parity
# It returns 1 if n has odd parity,else returns 0 
def getParity( n ):
	parity = 0
	while n:
		parity = ~parity
		n = n & (n - 1)
	return parity

# Driver program 
n = int(input("Enter a number: "))
print ("Parity of ", n," = ",
	( "odd" if getParity(n) else "even"))
