from tkinter import *
from distutils import extension
from fileinput import filename
import os , shutil

root = Tk()
root.title("File System Organizer")

def organise(path):
    files = os.listdir(path)

    for file in files:
        filename,extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(path + '/' + extension):
            shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
        else:
            os.makedirs(path + '/' + extension)
            shutil.move(path + '/' + file, path + '/' + extension + '/' + file)

def click_func():
    organise(e.get())
    lable_2 = Label(root, text="Your files have been organised!")
    lable_2.pack()

lable_1 = Label(root, text="Enter your directory path :")
lable_1.pack()

e = Entry(root, width=120, border=3)
e.pack()

btn  = Button(root, text = " Organise", command = click_func )
btn.pack()

root.mainloop()



