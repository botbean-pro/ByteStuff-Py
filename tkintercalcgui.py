import tkinter as tk
from tkinter import messagebox

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("500x500")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.expression = []

        def CalcTheStuff(value):
            try:
                if isinstance(value, int) or value in ["+", "-", "*", "/"]:
                    self.expression.append(value)
                    self.TextBox.config(state="normal")
                    self.TextBox.delete(0, tk.END)
                    self.TextBox.insert(0, "".join(map(str, self.expression)))
                    self.TextBox.config(state="readonly")
                elif value == "C":
                    self.expression = []
                    self.TextBox.config(state="normal")
                    self.TextBox.delete(0, tk.END)
                    self.TextBox.config(state="readonly")
                elif value == "=":
                    result = eval("".join(map(str, self.expression)))
                    self.TextBox.config(state="normal")
                    self.TextBox.delete(0, tk.END)
                    self.TextBox.insert(0, str(result))
                    self.TextBox.config(state="readonly")
                    self.expression = [result]
            except Exception:
                self.TextBox.config(state="normal")
                self.TextBox.delete(0, tk.END)
                self.TextBox.insert(0, "Error")
                self.TextBox.config(state="readonly")
                self.expression = []

        
        self.TextBox = tk.Entry(self.root, width=30, font=("Arial", 24), state='readonly')
        self.TextBox.insert(0, "Calculation here")
        self.TextBox.pack(pady=10, padx=10)

        buttonframe = tk.Frame(self.root)
        buttonframe.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.columnconfigure(2, weight=1)
        buttonframe.columnconfigure(3, weight=1)

        buttonframe.rowconfigure(0, weight=1)
        buttonframe.rowconfigure(1, weight=1)
        buttonframe.rowconfigure(2, weight=1)
        buttonframe.rowconfigure(3, weight=1)
        buttonframe.rowconfigure(4, weight=1)

        btn1 = tk.Button(buttonframe, text="1", command=lambda: CalcTheStuff(1))
        btn1.grid(row=0, column=0, sticky=tk.NSEW, padx=1, pady=1)
        btn2 = tk.Button(buttonframe, text="2", command=lambda: CalcTheStuff(2))
        btn2.grid(row=0, column=1, sticky=tk.NSEW, padx=1, pady=1)
        btn3 = tk.Button(buttonframe, text="3", command=lambda: CalcTheStuff(3))
        btn3.grid(row=0, column=2, sticky=tk.NSEW, padx=1, pady=1)
        btn4 = tk.Button(buttonframe, text="+", command=lambda: CalcTheStuff("+"))
        btn4.grid(row=0, column=3, sticky=tk.NSEW, padx=1, pady=1)

        btn5 = tk.Button(buttonframe, text="4", command=lambda: CalcTheStuff(4))
        btn5.grid(row=1, column=0, sticky=tk.NSEW, padx=1, pady=1)
        btn6 = tk.Button(buttonframe, text="5", command=lambda: CalcTheStuff(5))
        btn6.grid(row=1, column=1, sticky=tk.NSEW, padx=1, pady=1)
        btn7 = tk.Button(buttonframe, text="6", command=lambda: CalcTheStuff(6))
        btn7.grid(row=1, column=2, sticky=tk.NSEW, padx=1, pady=1)
        btn8 = tk.Button(buttonframe, text="-", command=lambda: CalcTheStuff("-"))
        btn8.grid(row=1, column=3, sticky=tk.NSEW, padx=1, pady=1)

        btn9 = tk.Button(buttonframe, text="7", command=lambda: CalcTheStuff(7))
        btn9.grid(row=2, column=0, sticky=tk.NSEW, padx=1, pady=1)
        btn10 = tk.Button(buttonframe, text="8", command=lambda: CalcTheStuff(8))
        btn10.grid(row=2, column=1, sticky=tk.NSEW, padx=1, pady=1)
        btn11 = tk.Button(buttonframe, text="9", command=lambda: CalcTheStuff(9))
        btn11.grid(row=2, column=2, sticky=tk.NSEW, padx=1, pady=1)
        btn12 = tk.Button(buttonframe, text="*", command=lambda: CalcTheStuff("*"))
        btn12.grid(row=2, column=3, sticky=tk.NSEW, padx=1, pady=1)

        btn13 = tk.Button(buttonframe, text="C", command=lambda: CalcTheStuff("C"))
        btn13.grid(row=3, column=0, sticky=tk.NSEW, padx=1, pady=1)
        btn14 = tk.Button(buttonframe, text="0", command=lambda: CalcTheStuff(0))
        btn14.grid(row=3, column=1, sticky=tk.NSEW, padx=1, pady=1)
        btn15 = tk.Button(buttonframe, text="/", command=lambda: CalcTheStuff("/"))
        btn15.grid(row=3, column=2, sticky=tk.NSEW, padx=1, pady=1)
        btn16 = tk.Button(buttonframe, text="=", command=lambda: CalcTheStuff("="))
        btn16.grid(row=3, column=3, sticky=tk.NSEW, padx=1, pady=1)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = CalculatorGUI(root)
    root.mainloop()