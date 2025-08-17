from tkinter import *
#label=an area of the window that displays text or images
window=Tk()
photo=PhotoImage(file="icon.png")
label=Label(window,text="Hello World!",font=("Arial",40,"bold"),bg="black",fg="white",
            relief=RAISED,bd=10,padx=20,pady=20,image=photo,compound="bottom")
label.pack()#pack() method is used to add the label to the window
#label.place(x=0,y=0) #place() method is used to place the label at specific coordinates in the window
window.mainloop()
