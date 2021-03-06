from tkinter import Tk, Frame, Label, Button, Entry, W, E, N ,S
import QueryFunction as QF
from tkinter import messagebox

class removefood:

    def __init__(self):
        self.window = Tk()
        self.mainframe = Frame(self.window)

        self.instructionL = Label(self.mainframe, text="Please fill in the fields\nwith appropriate values. ")
        self.noL = Label(self.mainframe, text = "No: ")

        self.foodnameI = Entry(self.mainframe)
        self.noI = Entry(self.mainframe)


        self.okayB = Button(self.mainframe, text="OKAY")
        self.cancelB = Button(self.mainframe, text="CANCEL", command=self.cancel)
        self.mainframe.grid(row = 0, column = 0, columnspan = 2, sticky = W + E + N +S)
        self.mainframe.propagate(0)

        self.instructionL.grid(row = 0, column = 0, columnspan = 2)
        self.noL.grid(row = 3, column = 0)
        self.noI.grid(row = 3, column = 1)


        self.okayB.grid(row = 5, column = 0)
        self.okayB.bind("<Button-1>", self.okayE)
        self.cancelB.grid(row = 5, column = 1)

    def cancel(self):
        self.window.destroy()

    def okayE(self, event):
        removable = False
        cursor = QF.cursor
        query = ("SELECT No FROM Foods2;")
        cursor.execute(query)
        info = []
        no = self.noI.get()
        info.append(no)
        food = tuple(info)
        mylist = []

        for allfood in cursor:
            mylist.append(allfood[0])

        for n in mylist:
            if int(n) == int(no):
                removable = True

        if removable == True:
            QF.cursor.callproc('remove_food', food)
            QF.cnx.commit()
            messagebox.showinfo("Success", "Congratulation!\nYou have successfully removed a food.")
            self.window.destroy()
        else:
            messagebox.showerror("Error", "Not a valid food!")
            return




