from tkinter import *


class Calculator(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creates the buttons displayed
        self.displayText = StringVar()
        self.display = Entry(root, textvariable=self.displayText, justify="right")
        self.display.grid(row=0, column=0, columspan=4, padx=10, pady=10)

    # Creating the clear button
        for clearButton in (["C"]):
            for ichar in clearButton:
                button(root, text=buttonText,
                       command=lambda number=buttonText: self.)

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Calculator")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)
        file.add_command(label="About", command=self.popup_message)

        # added "file" to our menu
        menu.add_cascade(label="File", menu=file)

    def client_exit(self):
        exit()

    def popup_message(self):
        popup = Tk()
        popup.wm_title("About")
        label = Label(popup, text="Fully designed and developed by Tiago Lopes\n\n\n" + "P.S. A bit with the help of "
                                                                                        "my friends over the internet "
                                                                                       "shhhhh")
        label.pack(side="top", fill="x", pady=10)
        popup.mainloop()

    def button(source, side, text, command=None):
        storeobj = Button(source, text=text, command=command)
        storeobj.pack(side=side, expand=YES, fill=BOTH)
        return storeobj




# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("370x600")

# creation of an instance
app = Window(root)

# mainloop
root.mainloop()
