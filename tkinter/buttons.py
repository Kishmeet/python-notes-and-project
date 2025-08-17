from tkinter import*
#buttons=you click on them to perform an action
count=0
def click():
    global count
    count+=1
    label.config(text=count)#update the label with the new count value
    #label2.pack()#update the label with the new count value
window=Tk()
button=Button(window,text="Click Me!")
button.config(command=click)#command=action to be performed when the button is clicked
#performs call back to function
button.config(font=("Ink Free",50,"bold"))
button.config(bg="#ff6200")
button.config(fg="#fffb1f")
button.config(activebackground="#FF0000")
button.config(activeforeground="#fffb1f")
image=PhotoImage(file="image.png")
button.config(image=image,compound="bottom")#compound=position of the image relative to the text
#button.config(state=DISABLED)#DISABLED=button is not clickable, NORMAL=button is clickable
label=Label(window,text=count)
label.config(font=('Manospaced',50,"bold"))
button.pack()
label.pack()
label2=Label(window,image=image)
window.mainloop()

