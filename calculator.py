import tkinter as tk
from tkinter import ttk


class Calculator(tk.Tk):
    def __init__(self, name=""):
        super().__init__()

        self.name = name

        self.valueList = []
        self.opList = []

        self.title(f"{name}'s Calculator")

        e = ttk.Entry(self)
        prevCalc = ttk.Button(self, text="History", command=lambda: self.prev(PrevScreen, self.name))

        self.b9 = ttk.Button(self, text="9", command=lambda: self.enterNum("9", e))
        self.b8 = ttk.Button(self, text="8", command=lambda: self.enterNum("8", e))
        self.b7 = ttk.Button(self, text="7", command=lambda: self.enterNum("7", e))
        self.b6 = ttk.Button(self, text="6", command=lambda: self.enterNum("6", e))
        self.b5 = ttk.Button(self, text="5", command=lambda: self.enterNum("5", e))
        self.b4 = ttk.Button(self, text="4", command=lambda: self.enterNum("4", e))
        self.b3 = ttk.Button(self, text="3", command=lambda: self.enterNum("3", e))
        self.b2 = ttk.Button(self, text="2", command=lambda: self.enterNum("2", e))
        self.b1 = ttk.Button(self, text="1", command=lambda: self.enterNum("1", e))
        self.b0 = ttk.Button(self, text="0", command=lambda: self.enterNum("0", e))
        self.badd = ttk.Button(self, text="+", command=lambda: self.operator("+", self.valueList, self.opList, e))
        self.bsub = ttk.Button(self, text="-", command=lambda: self.operator("-", self.valueList, self.opList, e))
        self.bmul = ttk.Button(self, text="*", command=lambda: self.operator("*", self.valueList, self.opList, e))
        self.bdiv = ttk.Button(self, text="/", command=lambda: self.operator("/", self.valueList, self.opList, e))
        self.bequ = ttk.Button(self, text="=", command=lambda: self.getResult(self.valueList, self.opList, e))
        self.bclear = ttk.Button(self, text="C", command=lambda: self.clear(e))

        e.grid(row=0, column=0, columnspan=3, ipadx=50, ipady=10)
        prevCalc.grid(row=0, column=3, columnspan=4, ipadx=5, ipady=5)

        self.b9.grid(row=1, column=2, ipadx=20, ipady=20)
        self.b8.grid(row=1, column=1, ipadx=20, ipady=20)
        self.b7.grid(row=1, column=0, ipadx=20, ipady=20)
        self.b6.grid(row=2, column=2, ipadx=20, ipady=20)
        self.b5.grid(row=2, column=1, ipadx=20, ipady=20)
        self.b4.grid(row=2, column=0, ipadx=20, ipady=20)
        self.b3.grid(row=3, column=2, ipadx=20, ipady=20)
        self.b2.grid(row=3, column=1, ipadx=20, ipady=20)
        self.b1.grid(row=3, column=0, ipadx=20, ipady=20)
        self.b0.grid(row=4, column=1, ipadx=20, ipady=20)

        self.badd.grid(row=1, column=3, ipadx=20, ipady=20)
        self.bsub.grid(row=2, column=3, ipadx=20, ipady=20)
        self.bmul.grid(row=3, column=3, ipadx=20, ipady=20)
        self.bdiv.grid(row=4, column=3, ipadx=20, ipady=20)
        self.bequ.grid(row=4, column=2, ipadx=20, ipady=20)

        self.bclear.grid(row=4, column=0, ipadx=20, ipady=20)

    # Opens the Calculation History screen
    def prev(self, _class, name):
        _class(name)

    # Enters the number into the calculator based on the button pressed
    def enterNum(self, value, e):
        e.insert("end", value)

    # Gets the number entered into the calculator
    def getValue(self, e):
        return e.get()

    # Clears the number entered into the calculator
    def clear(self, e):
        e.delete(0, "end")

    # Clears all stored numbers and operators
    def clearAll(self, valueList, opList):
        for x in valueList:
            valueList.remove(x)

        for x in opList:
            opList.remove(x)

    # Adds a number into the number list
    def storeValue(self, valueList, e):
        value = int(e.get())
        valueList.append(value)

    # Adds an operator into the operator list
    def addToOpList(self, opList, value):
        opList.append(value)

    # Stores the value and the operator into their respective lists
    def operator(self, value, valueList, opList, e):
        self.storeValue(valueList, e)
        self.addToOpList(opList, value)
        self.clear(e)

    # Performs the calculation in order of multiply, divide, add, minus
    def calculate(self, valueList, opList):
        for x in opList:
            if x == "*":
                sum = valueList[opList.index(x)] * valueList[opList.index(x) + 1]
                valueList[opList.index(x)] = sum
                del valueList[opList.index(x) + 1]
                opList.remove(x)

        for x in opList:
            if x == "/":
                sum = valueList[opList.index(x)] / valueList[opList.index(x) + 1]
                valueList[opList.index(x)] = sum
                del valueList[opList.index(x) + 1]
                opList.remove(x)

        for x in opList:
            if x == "+":
                sum = (valueList[opList.index(x)] + valueList[opList.index(x) + 1])
                valueList[opList.index(x)] = sum
                del valueList[opList.index(x) + 1]
                opList.remove(x)

        for x in opList:
            if x == "-":
                sum = valueList[opList.index(x)] - valueList[opList.index(x) + 1]
                valueList[opList.index(x)] = sum
                del valueList[opList.index(x) + 1]
                opList.remove(x)

        return valueList[0]

    # After equals is pressed, finds the result & record the calculation
    def getResult(self, valueList, opList, e):
        lastItem = e.get()
        self.storeValue(valueList, e)
        writeList = [item for sublist in zip(valueList, opList) for item in sublist]
        writeList.append(lastItem)
        result = self.calculate(valueList, opList)
        self.writeHistory(writeList, result, self.name)
        self.clear(e)
        e.insert([0], result)
        self.clearAll(valueList, opList)

    # Writes the calculation to the user's history file
    def writeHistory(self, writeList, result, name):
        writeList = writeList + ["=", result]

        with open(f"{name}_history", "a+") as file:
            file.seek(0)
            data = file.read(100)
            if len(data) > 0:
                file.write("\n")
            for x in writeList:
                if writeList.index(x) == (len(writeList) - 1):
                    file.write(str(x))
                else:
                    file.write(str(x) + " ")

        for x in writeList:
            writeList.remove(x)


# Screen to display the user's calculation history
class PrevScreen(tk.Tk):
    def __init__(self, name):
        super().__init__()

        self.name = name
        self.title("Calculation History")

        with open(f"{name}_history", "r") as file:
            calcList = file.readlines()
        calcs = "\n".join([str(item) for item in calcList])

        self.label = ttk.Label(self, text="Below are your most recent calculations:", anchor="center")
        self.history = ttk.Label(self, text=calcs, anchor="center")

        self.label.grid(row=0, column=0, ipadx=10, pady=20, sticky="we")
        self.history.grid(row=1, column=0, ipadx=10, pady=10, sticky="we")


if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
