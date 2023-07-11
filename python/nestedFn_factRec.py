def print_even(lst):
    def find_even(num):
        if num%2 == 0:
            return True
        else:
            return False
    new_list = []
    for num in lst:
        if find_even(num) == True:
            new_list.append(num)
    print("Final list: ",new_list)

mylist = [1,2,4,5,6,7,10,11,12]
print_even(mylist)



def factorial(n):
    print("Factorial has been called with n = "+str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result for ",n, " * factorial(" ,n-1, "):",res)
        return res
print("Result: ",factorial(3))