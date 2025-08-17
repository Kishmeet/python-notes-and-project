from tkinter import *
#widgets=GUI elements:buttons, labels, textboxes, etc.
#windows=serves as a container for widgets
#Tk() creates a window object
window=Tk()#instantiate the Tk class to create a window object
#mainloop() method is an infinite loop that runs until the window is closed
window.geometry("400x400")#set the size of the window to 400x400 pixels
window.title("My First GUI")#set the title of the window to "My First GUI"  
icon=PhotoImage(file="icon.png")#load an image file to use as an icon
window.iconphoto(True,icon)#set the icon of the window to the loaded image
window.config(background="black")#set the background color of the window to light blue(bg)
window.mainloop()#place the window on the screen and wait for user interaction
#The window will remain open until the user closes it.
#The program will not terminate until the window is closed.