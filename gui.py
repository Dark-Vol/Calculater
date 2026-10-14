
import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("450x450")

# Display
entry = tk.Entry(root, font=("Times New Romen", 20), justify="right")
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Add a digit or decimal point
def add_number(value):
    entry.insert(tk.END, value)

# Clear the input field
def clear():
    entry.delete(0, tk.END)

# Button layout
buttons = [
    ["C", "**", "//", "%"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["()", "0", ".", "="]
]

# Create buttons
for row_index, row in enumerate(buttons, start=1):
    for col_index, value in enumerate(row):
        if value == "C":
            command = clear
        else:
            command = lambda v=value: add_number(v)

        button = tk.Button(
            root,
            text=value,
            font=("Arial", 14),
            width=6,
            height=2,
            command=command
        )
        button.grid(
            row=row_index,
            column=col_index,
            padx=3,
            pady=3
        )

root.mainloop()
