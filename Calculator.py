import tkinter as tk

darkGrey = "#A9A9A9"
labelColour = "#202020"
labelFont = ("Arial", 16)
largeFont = ('Arial', 40, "bold")
digitColour = ('#FFFFFF')
digitFont = ("Arial", 24, "bold")
defaultFont = ("Arial", 20)
offWhite = "#F8FAFF"
lightBlue = "#ADD8E6"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")
        self.totalExpression = ""
        self.currentExpression = ""

        self.display_frame = self.displayFrame()

        self.totalLabels, self.Labels = self.displayLabels()
        self.buttons_frame = self.buttonsFrame()
        self.buttons_frame.rowconfigure(0, weight=1)

        for z in range(1,5):
            self.buttons_frame.rowconfigure(z, weight=1)
            self.buttons_frame.columnconfigure(z, weight=1)


        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,2), '.':(4,1)
        }

        self.operators = { "/":"\u00F7", "*":"\u00D7", "-": "-", "+":"+"}

        self.digitButton()
        self.operatorButtons()
        self.specialButtons()
        

    def specialButtons(self):
        self.clearButton()
        self.equalButton()
        self.squaringButton()
        self.squareRootButton()
        
        
        

    def displayLabels(self):
        totalLabels = tk.Label(self.display_frame, text = self.totalExpression, anchor = tk.E, bg = darkGrey, fg = labelColour, padx = 24, font = labelFont)
        totalLabels.pack(expand = True, fill = "both")

        Labels = tk.Label(self.display_frame, text = self.currentExpression, anchor = tk.E, bg = darkGrey, fg = labelColour, padx = 24, font = largeFont)
        Labels.pack(expand = True, fill = "both")
        
        return totalLabels, Labels
    

    def displayFrame(self):
        frame = tk.Frame(self.window, height = 221, bg = darkGrey)
        frame.pack(expand = True, fill = "both")
        return frame


    def addExpression(self, value):
        self.currentExpression += str(value)
        self.updateLabel()


    def addOperator(self, operator):
        self.currentExpression += operator
        self.totalExpression += self.currentExpression
        self.currentExpression = ""
        self.updateTotalLabel()
        self.updateLabel()

    def digitButton(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text = str(digit), bg = digitColour, fg = labelColour, font = digitFont, borderwidth=0, command = lambda x = digit: self.addExpression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)


    def buttonsFrame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand = True, fill = "both")
        return frame

    def operatorButtons(self):
        i = 0
        for operator, symbol in self.operators.items():
            button = tk.Button(self.buttons_frame, text = symbol, bg = offWhite, fg = labelColour, font = defaultFont, borderwidth=0, command = lambda x= operator: self.addOperator(x))
            button.grid(row = i, column=4, sticky = tk.NSEW)
            i+=1


    def clear(self):
        self.currentExpression = ""
        self.totalExpression = ""
        self.updateLabel()
        self.updateTotalLabel()

    def clearButton(self):
            button = tk.Button(self.buttons_frame, text = "C", bg = offWhite, fg = labelColour, font = defaultFont, borderwidth=0, command = self.clear)
            button.grid(row = 0, column=1, sticky = tk.NSEW)

    def square(self):
        self.currentExpression = str(eval(f"{self.currentExpression}**2"))
        self.updateLabel()

    def squaringButton(self):
            button = tk.Button(self.buttons_frame, text = "x\u00b2", bg = offWhite, fg = labelColour, font = defaultFont, borderwidth=0, command = self.square)
            button.grid(row = 0, column=2, sticky = tk.NSEW)

    def sqrt(self):
        self.currentExpression = str(eval(f"{self.currentExpression}**0.5"))
        self.updateLabel()

    def squareRootButton(self):
            button = tk.Button(self.buttons_frame, text = "\u221ax", bg = offWhite, fg = labelColour, font = defaultFont, borderwidth=0, command = self.sqrt)
            button.grid(row = 0, column=3, sticky = tk.NSEW)


    def evaluate(self):
        self.totalExpression += self.currentExpression
        self.updateTotalLabel()

        try:
            self.currentExpression = str(eval(self.totalExpression))
            self.totalExpression = ""
        
        except Exception as e:
            self.currentExpression = "Error mate"
        
        finally:
            self.updateLabel()


        self.updateLabel()


    def equalButton(self):
            button = tk.Button(self.buttons_frame, text = "=", bg = lightBlue, fg = labelColour, font = defaultFont, borderwidth=0, command = self.evaluate)
            button.grid(row = 4, column=3, columnspan=2,  sticky = tk.NSEW)


    def updateTotalLabel(self):
        expression = self.totalExpression
        for operator, symbol in self.operators.items():
            expression = expression.replace(operator, f'{symbol}')
        self.totalLabels.config(text = expression)

    def updateLabel(self):
        self.Labels.config(text = self.currentExpression[:11])

    

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()

    
