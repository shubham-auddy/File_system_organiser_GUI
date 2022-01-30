from tkinter import Tk, Label, Entry, Button
import utility

def click_func():
    utility.organise(e.get())
    lable_2 = Label(root, text="Your files have been organised!")
    lable_2.pack()

root = Tk()
root.title("File System Organizer")

lable_1 = Label(root, text="Enter your directory path :")
lable_1.pack()

e = Entry(root, width=120, border=3)
e.pack()

btn  = Button(root, text = " Organise", command = click_func )
btn.pack()

root.mainloop()



