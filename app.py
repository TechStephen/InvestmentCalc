from tkinter import *
from tkinter import ttk

class Tkinter:
    
    answer = []
    
    def __init__(self):
        root = Tk()
        root.title("Interest Calculator")

        frm = ttk.Frame(root, padding=100)
        frm.grid()
        
        ttk.Label(frm, text="Interest App").grid(column=1, row=0)

        inputInitialAmount = IntVar()
        inputInterestRate = DoubleVar()
        inputYears = IntVar()
        self.output = StringVar()

        ttk.Label(frm, text="Initial Investment").grid(column=0, row=1)
        ttk.Entry(frm, width=20, textvariable=inputInitialAmount).grid(column=1, row=1)
        
        ttk.Label(frm, text="Annual Return (0.08 = 8%)").grid(column=0, row=2)
        ttk.Entry(frm, width=20, textvariable=inputInterestRate).grid(column=1, row=2)

        ttk.Label(frm, text="Years Invested").grid(column=0, row=3)
        ttk.Entry(frm, width=20, textvariable=inputYears).grid(column=1, row=3)

        ttk.Button(frm, text="Calculate", command=lambda: self.calcInterest(
            inputInitialAmount.get(), inputInterestRate.get(), inputYears.get()
        )).grid(column=1, row=4)
        
        ttk.Label(frm, text='Results Per Year:' + '\n').grid(column=3, row=0)
        ttk.Label(frm, textvariable=self.output, justify=LEFT, anchor='w').grid(column=3, row=1, rowspan=10, sticky='nw')

        root.mainloop()

    def returnAnswerText(answer):
        print('ran')

    # Calculate the interest over a number of years
    def calcInterest(self, initialAmount, interestRate, years):
        amountPerYears = []
        initAmount = initialAmount
        
        # Loop through each year to calculate the interest
        for i in range(int(years)):
            initAmount += initAmount * interestRate
            initAmount = round(initAmount, 2)
            amountPerYears.append('year ' + str(i + 1) + ' value with interest: $' + str(initAmount))
        
        # print('*****Initial Investment: $' + str(initialAmount) + ' with an interest rate of ' + str(Tkinter.getPercent(interestRate)) + ' over ' + str(years) + ' years*****' + '\n')
        
        self.answer = amountPerYears
        self.output.set('\n'.join(amountPerYears))  
        print(amountPerYears)
    
    # Get the percent value from a decimal
    @staticmethod 
    def getPercent(decimal):
        percent = decimal * 100
        striptPercent = str(percent).rstrip('0').rstrip('.')
        return str(striptPercent) + '%'

if __name__ == "__main__":
    # calcInterest(10000, 0.08, 10)
    tk = Tkinter()