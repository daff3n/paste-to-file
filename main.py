import pyperclip
from tkinter import *
import os
import getpass
from getpass import getuser

def makefile(event):

	user = getuser()
	basedir = "C:/Users/"+user+"/Desktop/"
	
	text = pyperclip.paste()
	f = open(basedir+e.get(), "w")
	f.write(text)
	f.close()
	#print(e.get())
	root.destroy()

root = Tk()
root.title("Creates a file with what you have copied")
root.geometry("150x60")

l = Label(root, text="Enter filename")
l.pack()

e = Entry(root)
e.pack()
e.focus_set()

root.bind('<Return>', makefile)

root.mainloop()
