from tkinter import *

def display():
    if x.get() == 1:
        print("I like Brook")
    else:
        print("I don't like Brook")

window = Tk()

x = IntVar()

checkbox = Checkbutton(window, text = "I like Brook", variable = x, onvalue=1, offvalue=0, command=display)
checkbox.pack()

checkbox.config(font=('Ink Free', 50))
checkbox.config(bg='#000000', fg='#0000FF', activebackground='#000000', activeforeground='#0000FF')

photo = PhotoImage(file="images (1).png")
checkbox.config(image=photo, compound='left')
checkbox.config(padx=20)

window.mainloop()
