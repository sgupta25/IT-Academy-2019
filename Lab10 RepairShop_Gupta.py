# Sarvesh Gupta
# Joe's Automotive Repair Shop Lab 10
# User selects services they want, program shows total cost

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.oilChange = BooleanVar()
        Checkbutton(self,
                    text = "Oil Change - $26.00",
                    variable = self.oilChange
                    ).grid(row = 0, column = 0, columnspan = 5, sticky = W)

        self.lubeJob = BooleanVar()
        Checkbutton(self,
                    text = "Lube Job - $18.00",
                    variable = self.lubeJob
                    ).grid(row = 1, column = 0, columnspan = 5, sticky = W)
        
        self.radFlush = BooleanVar()
        Checkbutton(self,
                    text = "Radiator Flush - $30.00",
                    variable = self.radFlush
                    ).grid(row = 2, column = 0, columnspan = 5, sticky = W)
        self.transFlush = BooleanVar()
        Checkbutton(self,
                    text = "Transmission Flush - $80.00",
                    variable = self.transFlush
                    ).grid(row = 3, column = 0, columnspan = 5, sticky = W)
        self.inspection = BooleanVar()
        Checkbutton(self,
                    text = "Inspection - $15.00",
                    variable = self.inspection
                    ).grid(row = 4, column = 0, columnspan = 5, sticky = W)
        self.mufflerReplacement = BooleanVar()
        Checkbutton(self,
                    text = "Muffler Replacement - $100.00",
                    variable = self.mufflerReplacement
                    ).grid(row = 5, column = 0, columnspan = 5, sticky = W)
        self.tireRotation = BooleanVar()
        Checkbutton(self,
                    text = "Tire Rotation - $20.00",
                    variable = self.tireRotation
                    ).grid(row = 6, column = 0, columnspan = 5, sticky = W)
        Button(self,
               text = "Display Charges",
               command = self.displayCharges
               ).grid(row = 7, column = 0, sticky = W)

        Button(self,
               text = "Quit",
               command = quit
               ).grid(row = 7, column = 1, sticky = W)

        self.cost = Text(self, width = 50, height = 15, wrap = WORD)
        self.cost.grid(row = 8, column = 0, columnspan = 5)

    def displayCharges(self):
        cost = 0.00
        if self.oilChange.get():
            cost = cost + 26.00
        if self.lubeJob.get():
            cost = cost + 18.00
        if self.radFlush.get():
            cost = cost + 30.00
        if self.transFlush.get():
            cost = cost + 80.00
        if self.inspection.get():
            cost = cost + 15.00
        if self.mufflerReplacement.get():
            cost = cost + 100.00
        if self.tireRotation.get():
            cost = cost + 20.00

        dispStat = ("Your total cost is $" + str(cost))

        self.cost.delete(0.0, END)
        self.cost.insert(0.0, dispStat)


# main
root = Tk()
root.title("Joe's Automotive Repair Shop")
root.geometry("400x400")
app = Application(root)

root.mainloop()
