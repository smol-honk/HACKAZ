# Hack AZ Basic GUI

from tkinter import *
from tkinter.ttk import *

class TimeManager(Frame):
    def __init__(self, root, **options):
        super().__init__()
        self.root = root
        self.root.title(options['title'])
        self.root.resizable(0,0)
        self.grid(row=0, column=0, sticky='nesw')
        
# Data attributes

    # String Variables
        self.choice_text        = StringVar()
        self.friend_text        = StringVar()
        self.choice_box_text    = StringVar()
        self.friend_box_text    = StringVar()
        self.choose_bttn_text   = StringVar()
        self.add_bttn_text      = StringVar()
        self.out_text           = StringVar()

    # Labels
        self.choice             = Label(self, textvariable = self.choice_text)
        self.choice_text.set("Priority")
        self.friend             = Label(self, textvariable = self.friend_text)
        self.friend_text.set("Add friends")

        self.l1 = Label(self)
        self.l2 = Label(self)
        self.l3 = Label(self)
        self.l4 = Label(self)
        self.l5 = Label(self)

        self.l1.grid            (row=2, column=0, columnspan=3, sticky="nesw")
        self.l2.grid            (row=3, column=0, columnspan=3, sticky="nesw")
        self.l3.grid            (row=4, column=0, columnspan=3, sticky="nesw")
        self.l4.grid            (row=5, column=0, columnspan=3, sticky="nesw")
        self.l5.grid            (row=6, column=0, columnspan=3, sticky="nesw")
        
    # Option Menu
        self.choice_box         = OptionMenu(self, self.choice_box_text, "1", "2", "3")
        self.choice_box_text.set("Choice")
        self.friend_box         = OptionMenu(self, self.friend_box_text, "1", "2", "3")
        self.friend_box_text.set("Friend")
    
    # Entrys
        self.out_entry          = Entry(self, textvariable = self.out_text, state="readonly")

    # Buttons
        self.choose             = Button(self, text = "Choose")
        self.add                = Button(self, text="Add")

# Graphics
        self.choice.grid            (row=0, column=0, sticky="nw")
        self.friend.grid            (row=1, column=0, sticky="nw")
        self.choice_box.grid        (row=0, column=1, sticky="nw")
        self.friend_box.grid        (row=1, column=1, sticky="nw")
        self.choose.grid            (row=0, column=2, sticky="new")
        self.add.grid               (row=1, column=2, sticky="new")
        self.out_entry.grid         (row=7, column=0, columnspan=3, sticky="esw")
        
def main():
    root = Tk()
    TimeManager(root, title="Time Manager v1.0")
    root.mainloop()

if __name__ == "__main__":
    main()
