# program to find no. of boys and girls in class
def check_voter(age):
    if(age>=18):
        print("You can Vote!")
    else: 
        print("You cant Vote!")
age = int(input("Enter your age: "))
check_voter(age)