def f1():
    s=10
    def f2():
        print(s)
    f2()
f1()

def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
print(fact(8))


print("Hello DSEU !")


str1 = "python"
print(str1.upper())
str2 = "PYTHON"
print(str2.lower())
print(str1.capitalize())
print(str1.count("Y"))
str3 = "python124"
print(str3.isalnum())
print(str3.isalpha())
str4="6466876"
print(str4.isdigit())
print(str2.isupper())
print(str1.islower())
str5 = "my name is python"
print(str5.replace("python","tata"))
print(str5.split())