# program to find no of boys or girls in class
ratio_b = int(input("Enter the Ratio of boys : "))
ratio_g = int(input("Enter the Ratio of girls : "))
times = int(input("Enter the times of boys to girls: "))
x =int(times/(ratio_b-ratio_g))
print("\nNo. of boys are ",ratio_b*x)
print("No. of girls are ",ratio_g*x)
