#entry Widget=text box that accepts single of user input
from tkinter import *
def submit():
  username=entry.get()#get() method retrieves the text entered in the entry widget
  print(username)#print the username to the console
def delete():
  entry.delete(0,END)#delete() method deletes the text from index 0 to the end of the entry widget
def backspace():
  entry.delete(len(entry.get())-1,END)
window=Tk()
submit=Button(window,text="Submit",command=submit)
submit.pack(side=RIGHT)
delete=Button(window,text="Delete",command=delete)
delete.pack(side=RIGHT)
backspace=Button(window,text="backspace",command=backspace)
backspace.pack(side=RIGHT)
entry=Entry()
entry.config(font=('Ink free',50,"bold"))
entry.config(bg="#111111")
entry.config(fg="#00FF00")
#entry.insert(0,"Enter your name")#insert text at index 0
#entry.config(state=DISABLED)#DISABLED=entry is not editable, NORMAL=entry is editable
#entry.config(show="*")#show="*" hides the text entered in the entry widget
entry.config(width=10)#set the width of the entry widget to 30 characters
entry.pack()
window.mainloop()