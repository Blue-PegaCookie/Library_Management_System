# Lesson 1

import tkinter as tk

from tkinter import *

# Widgets = GUI Elements: Buttons, Labels, Textboxes, Images, etc.
# Widgets are added to the window

# Window = Serves as a container to hold or contain these widgets
# Window is the main GUI element

window = Tk() # instantiate an instance of a window

window.geometry("420x420") # Set window size
window.title("The title for my first GUI programme") # Set window title

icon = PhotoImage(file="image 1.png") # Create an icon
window.iconphoto(True, icon) # Set window icon
window.config(background="cyan") # Set window background
window.config(background="#5cfcff") # Set window background # You can also use hex

window.mainloop() # Place window on computer screen, listen for events (mouse, keyboard, etc.)



# Lesson 2
# Label = A widget used to display text or an image within a window

from tkinter import *

window = Tk()

photo = PhotoImage(file="image 1.png") # Create an image

label = Label(window, text="YOHOHOHOHO -Brook",
              font=('Arial', 40, 'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom') # Create a label
label.pack() # Add label to window
# label.place(x=100, y=100) # Set label position


window.mainloop()



# Lesson 3
# Button = A widget used to display a clickable button within a window

from tkinter import *

window = Tk()

def click():
    print("Button was clicked")

button = Button(window, text="click me!!!!!")
button.config(command=click) # Set button click event

button.config(font=('Ink Free', 50, 'bold'))
button.config(bg='#ff6200', fg='#fffb1f', activebackground='#FF0000', activeforeground='#fffb1f')

image = PhotoImage(file="image 1.png")
button.config(image=image, compound='bottom', state=DISABLED)
button.pack()

window.mainloop()

# Mini Project
# Create a GUI programme that displays a button that when clicked, A counter increases by 1

from tkinter import *

count = 0

def click():
    global count
    count += 1
    label.config(text=count)
    label2.pack()


window = Tk()

button = Button(window, text="click me!!!!!")
button.config(command=click) # Set button click event

button.config(font=('Ink Free', 50, 'bold'))
button.config(bg='#ff6200', fg='#fffb1f', activebackground='#FF0000', activeforeground='#fffb1f')

image = PhotoImage(file="image 1.png")
button.config(image=image, compound='bottom') # button.condifg(state=DISABLED) # disabled button (ACTIVE/DISABLED)

label = Label(window, text="Count")
label.config(font=('Ink Free', 50, 'bold'))
label.pack()
button.pack()
label2 = Label(window, image=image)

window.mainloop()



# Lesson 4

# Entry widget = A widget used to display a single-line text field for user input

from tkinter import *


def submit():
    username = entry.get()
    print("Username: " + username)

def delete():
    entry.delete(0, END)
    print("Deleted")

def backspace():
    entry.delete(len(entry.get()) - 1, END) # Delete the last character
    print("Backspace")

window = Tk()

submit = Button(window, text='Submit', command=submit)
submit.pack(side = RIGHT)

delete = Button(window, text='Delete', command=delete)
delete.pack(side = RIGHT)

backspace = Button(window, text='Backspace', command=backspace)
backspace.pack(side = RIGHT)

entry = Entry()
entry.config(font=('Ink free', 50, 'italic'), bg='#111111', fg='#00FF00', width=10)
             #  show='*'  It changes everything into a * character, useful for hidden passwords

# entry.insert(0, "Laugh like Brook") # Insert text into entry
# entry.config(state=DISABLED) # Disabled entry

entry.pack()
window.mainloop()



# Lesson 5

