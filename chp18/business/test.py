from tkinter import *
 
class Window:
    def __init__(self, master):
        subframe = Frame(master, background="blue")
        subject = Label(subframe, text = "Subject")
        subject.place(relx=0.5, rely=0.5,anchor=CENTER)
        subframe.pack(expand = True, fill = BOTH, side=LEFT)
 
        subframe2 = Frame(master, background="red")
        message = Label(subframe2, text= "Message")
        message.place(relx=0.5, rely=0.5,anchor=CENTER)
        subframe2.pack(expand=True, fill=BOTH, side=LEFT)
 
root = Tk()
root.geometry('300x200')
window = Window(root)
root.mainloop()