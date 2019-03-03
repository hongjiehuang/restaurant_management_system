from tkinter import Tk, Frame, Label, Button, Entry, W, E, N ,S, messagebox
import QueryFunction as QF


class givewarning:
    def __init__(self):
        self.window = Tk()
        self.mainframe = Frame(self.window)
        self.instructionL = Label(self.mainframe, text="Please fill in the fields\nwith appropriate values. ")
        self.workerL = Label(self.mainframe, text = "WORKER's ID: ")
        self.warningL = Label(self.mainframe, text = "WARNING: ")

        self.workerI = Entry(self.mainframe)
        self.warningI = Entry(self.mainframe)
        self.okayB = Button(self.mainframe, text = "OKAY")
        self.cancelB = Button(self.mainframe, text = "CANCEL", command = self.cancel)

        self.mainframe.grid(row = 0, column = 0, columnspan = 2, sticky = W + E + N +S)
        self.mainframe.propagate(0)

        self.instructionL.grid(row = 0, column = 0, columnspan = 2)
        self.workerL.grid(row = 1, column = 0)
        self.warningL.grid(row = 2, column = 0)
        self.workerI.grid(row = 1, column = 1)
        self.warningI.grid(row = 2, column = 1)
        self.okayB.grid(row = 3, column = 0)
        self.okayB.bind("<Button-1>", self.okayE)
        self.cancelB.grid(row = 3, column = 1)

    def cancel(self):
        self.window.destroy()

    def okayE(self, event):
        remove = False
        cursor = QF.cursor
        info = []
        self.warning = self.warningI.get()
        id = self.workerI.get()
        allworker = QF.showEmployee(cursor)
        try:

            for n in allworker:
                if (int(id) == int(n[0])):
                    remove = True
            info.append(id)
            info.append(self.warning)

            warning = tuple(info)
            if remove:
                if (int(self.warning) < 0):
                    messagebox.showerror("Error", "warning cannot be less than zero.")
                    return
                QF.cursor.callproc('give_warning', warning)
                QF.cnx.commit()
                messagebox.showinfo("Success", "Congratulation!\nYou have successfully given the warning to the worker.")
                self.window.destroy()
            else:
                messagebox.showerror("Error", "Not a valid employee's id!")
                self.window.destroy()
        except:
            messagebox.showerror("Error", "Something is wrong\n Check your input.")
            self.window.destroy()
