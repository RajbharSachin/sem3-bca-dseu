# open the file
text_file = open('student.txt','w')

#iterate 10 times
print("Enter Records:-")
for i in range (1,11):
    print("Student data ",i,": ")
    line = input() #take input
    text_file.write(line + "\n")

text_file.close #close the file



#open the file
text_file = open('student.txt','r')

#for each line from the file, print the line
print("\nStored Records:-")
for line in text_file.readlines():
    print(line)

text_file.close() #close the file



import shutil
shutil.copy2('/Users/offic/OneDrive/semester 3/python/student.txt','D:\Study\student_copy.txt')
print("File Copy Done")