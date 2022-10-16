year = int(input("Enter the year: "))
if(year%4==0) or (year%400==0):
    if(year%100!=0):
            print("Entered year is leap")
    else:
            print("Entered year isn't leap")    
else:
            print("Entered year isn't leap")    