import tkinter as tk

from main import calculate, parse_expression, round_multiply_divide_result


def run():
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("450x450")

    tk.Label(root, text="Result", font=("Arial", 10)).grid(row=0, column=0, columnspan=2)
    tk.Label(root, text="Rounded", font=("Arial", 10)).grid(row=0, column=2, columnspan=2)

    entry = tk.Entry(root, font=("Times New Roman", 18), justify="right")
    entry.grid(row=1, column=0, columnspan=2, padx=6, pady=6, sticky="ew")

    rounded_entry = tk.Entry(root, font=("Times New Roman", 18), justify="right")
    rounded_entry.grid(row=1, column=2, columnspan=2, padx=6, pady=6, sticky="ew")

    def add_number(value):
        rounded_entry.delete(0, tk.END)
        entry.insert(tk.END, value)

    def clear():
        entry.delete(0, tk.END)
        rounded_entry.delete(0, tk.END)

    def add_parentheses():
        text = entry.get()
        if text.count("(") > text.count(")"):
            entry.insert(tk.END, ")")
        else:
            entry.insert(tk.END, "(")

    def format_result(result):
        if isinstance(result, float) and result.is_integer():
            return str(int(result))
        return str(result)

    def calculate_result():
        expression = entry.get()
        try:
            first_num, operation, second_num = parse_expression(expression)
            result = calculate(first_num, operation, second_num)
            entry.delete(0, tk.END)
            rounded_entry.delete(0, tk.END)
            entry.insert(0, format_result(result))
            if operation in ("*", "/"):
                rounded_result = round_multiply_divide_result(result)
                rounded_entry.insert(0, format_result(rounded_result))
        except ZeroDivisionError:
            entry.delete(0, tk.END)
            rounded_entry.delete(0, tk.END)
            entry.insert(0, "Error: division by zero")
        except ValueError:
            entry.delete(0, tk.END)
            rounded_entry.delete(0, tk.END)
            entry.insert(0, "Error")

    buttons = [
        ["C", "**", "//", "%"],
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["()", "0", ".", "="],
    ]

    for row_index, row in enumerate(buttons, start=2):
        for col_index, value in enumerate(row):
            if value == "C":
                command = clear
            elif value == "=":
                command = calculate_result
            elif value == "()":
                command = add_parentheses
            else:
                command = lambda v=value: add_number(v)

            button = tk.Button(
                root,
                text=value,
                font=("Arial", 14),
                width=6,
                height=2,
                command=command,
            )
            button.grid(row=row_index, column=col_index, padx=3, pady=3)

    root.bind("<Return>", lambda event: calculate_result())
    root.mainloop()


if __name__ == "__main__":
    run()
