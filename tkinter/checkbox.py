from tkinter import *
#checkbox=used to select or deselect an option
def display():
    if(x.get()==1)&(y.get()==0):
        print("I like Python")
    elif(x.get()==0)&(y.get()==1):
        print("I like dog")
    elif(x.get()==1)&(y.get()==1):
        print("I like both Python & dog")
    else:
        print("I don't like either")
window=Tk()
x=IntVar()#IntVar() is a variable class that holds an integer value
y=IntVar()
checkbox=Checkbutton(window,text="Python",variable=x,onvalue=1,offvalue=0,command=display)#onvalue=1 means checkbox is checked, offvalue=0 means checkbox is unchecked
checkbox.pack()
checkbox.config(font=("Arial",20))
checkbox.config(bg="black")
checkbox.config(fg="blue")
checkbox.config(activeforeground="blue")
checkbox.config(activebackground="black")
photo=PhotoImage(file="python.png").subsample(2,2).subsample(2,2)#subsample() method is used to resize the image
checkbox.config(image=photo,compound="left")#compound=position of the image relative to the text
checkbox.config(padx=25,pady=10,width=250,height=50)
checkbox.config(anchor="w")#anchor=position of the checkbox in the window
checkbox2=Checkbutton(window,text="DOG",variable=y,onvalue=1,offvalue=0,command=display)#onvalue=1 means checkbox is checked, offvalue=0 means checkbox is unchecked
checkbox2.pack()
checkbox2.config(font=("Arial",20))
checkbox2.config(bg="black")
checkbox2.config(fg="blue")
checkbox2.config(activeforeground="blue")
checkbox2.config(activebackground="black")
photo2=PhotoImage(file="icon.png").subsample(2,2).subsample(2,2)#subsample() method is used to resize the image
checkbox2.config(image=photo2,compound="left")#compound=position of the image relative to the text
checkbox2.config(padx=25,pady=10,width=250,height=50)
checkbox2.config(anchor="w")#anchor=position of the checkbox in the window
window.mainloop()