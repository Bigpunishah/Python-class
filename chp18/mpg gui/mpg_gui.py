# Vikel Cunningham

import tkinter as tk
from tkinter import ttk


class MyFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack()

        # Define string variables for text entry fields
        miles_driven = tk.StringVar()
        gallons_used = tk.StringVar()
        miles_per_gallon = tk.StringVar()

        def click():
            print(miles_driven.get())
            print(gallons_used.get())
            md = float(miles_driven.get())
            gu = float(gallons_used.get())
            total = calculate_mpg(md, gu)
            miles_per_gallon.set(total)

        def calculate_mpg(milesDriven, gallonsUsed):
            MPG = round((milesDriven/gallonsUsed), 2)
            return MPG

        # Display the grid of components
        ttk.Label(self, text="Miles Driven:").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=miles_driven).grid(
            column=1, row=0)

        ttk.Label(self, text="Gallons of Gas Used:").grid(
            column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=gallons_used).grid(
            column=1, row=1)

        ttk.Label(self, text="Miles Per Gallon:").grid(
            column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=miles_per_gallon, state="readonly").grid(
            column=1, row=2)

        calcButton = ttk.Button(
            self, width=15, text="Calculate", command=click)
        calcButton.grid(column=1, row=3, sticky=tk.E)

        # Add padding to all components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Miles Per Gallon Calculator")
    MyFrame(root)
    root.mainloop()
