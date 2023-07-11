# program to sort words in alphabetical order USING sort()
my_str = input("Enter a string: ")
words = my_str.split() # list of words
words.sort()           # sort the list of words
for word in words:
    print(word)        # display word one by one