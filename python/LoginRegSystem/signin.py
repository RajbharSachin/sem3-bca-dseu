from tkinter import *
from PIL import ImageTk, Image #Python Image Library (for jpg files) 


#Functionality Part

def on_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)



#GUI Part
root=Tk() #obj variable from class
root.geometry('990x660+50+50') #for place method
bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(root,image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(root,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=605,y=120)

usernameEntry=Entry(root,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',on_enter) # to clear Entry on click
root.mainloop()