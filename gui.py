import tkinter as tk
from tkinter import ttk

from main import (
    calculate_expression,
    format_result,
    round_multiply_divide_result,
)


FONT = ("Times New Roman", 14)
DISPLAY_FONT = ("Times New Roman", 14)


def run():
    root = tk.Tk()
    root.title("Scientific Calculator")
    root.geometry("850x750")
    root.minsize(650, 600)
    root.configure(padx=10, pady=10)

    # ---------- Поля ввода и результата ----------

    tk.Label(root, text="Expression", font=FONT).pack(anchor="w")

    expression_entry = tk.Entry(
        root,
        font=DISPLAY_FONT,
        justify="right",
    )
    expression_entry.pack(fill="x", pady=(3, 8), ipady=6)

    result_frame = tk.Frame(root)
    result_frame.pack(fill="x", pady=(0, 8))
    result_frame.grid_columnconfigure(0, weight=1)
    result_frame.grid_columnconfigure(1, weight=1)

    tk.Label(result_frame, text="Result", font=FONT).grid(
        row=0, column=0, sticky="w"
    )
    tk.Label(result_frame, text="Rounded", font=FONT).grid(
        row=0, column=1, sticky="w"
    )

    result_entry = tk.Entry(
        result_frame,
        font=DISPLAY_FONT,
        justify="right",
        state="readonly",
    )
    result_entry.grid(row=1, column=0, sticky="ew", padx=(0, 5), ipady=4)

    rounded_entry = tk.Entry(
        result_frame,
        font=DISPLAY_FONT,
        justify="right",
        state="readonly",
    )
    rounded_entry.grid(row=1, column=1, sticky="ew", padx=(5, 0), ipady=4)

    # ---------- Работа с полями ----------

    def set_entry(entry, value):
        entry.configure(state="normal")
        entry.delete(0, tk.END)
        entry.insert(0, value)
        entry.configure(state="readonly")

    def clear():
        expression_entry.delete(0, tk.END)
        set_entry(result_entry, "")
        set_entry(rounded_entry, "")
        expression_entry.focus_set()

    def backspace():
        position = expression_entry.index(tk.INSERT)

        if position > 0:
            expression_entry.delete(position - 1, position)

        expression_entry.focus_set()

    def insert_value(value):
        if value == "clear":
            clear()
            return

        if value == "backspace":
            backspace()
            return

        if value == "equals":
            calculate_result()
            return

        expression_entry.insert(tk.INSERT, value)
        expression_entry.focus_set()

    # ---------- Вычисления ----------

    def calculate_result():
        expression = expression_entry.get().strip()

        if not expression:
            return

        try:
            result = calculate_expression(expression)
            set_entry(result_entry, format_result(result))

            if isinstance(result, (int, float)) and not isinstance(result, bool):
                rounded = round_multiply_divide_result(result)
                set_entry(rounded_entry, str(rounded))
            else:
                set_entry(rounded_entry, "—")

        except ZeroDivisionError:
            set_entry(result_entry, "Ошибка: деление на ноль")
            set_entry(rounded_entry, "")

        except (ValueError, TypeError, SyntaxError, OverflowError) as error:
            set_entry(result_entry, f"Ошибка: {error}")
            set_entry(rounded_entry, "")

    # ---------- Создание кнопок ----------

    def add_button(parent, label, value, row, column, colspan=1):
        button = tk.Button(
            parent,
            text=label,
            font=FONT,
            command=lambda v=value: insert_value(v),
            height=1,
            padx=3,
            pady=5,
        )
        button.grid(
            row=row,
            column=column,
            columnspan=colspan,
            sticky="nsew",
            padx=3,
            pady=3,
        )
        return button

    def create_button_grid(parent, buttons, columns=4):
        for column in range(columns):
            parent.grid_columnconfigure(column, weight=1)

        for index, (label, value) in enumerate(buttons):
            row = index // columns
            column = index % columns
            add_button(parent, label, value, row, column)

        for row in range((len(buttons) + columns - 1) // columns):
            parent.grid_rowconfigure(row, weight=1)

    # ---------- Вкладки ----------

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    basic_tab = tk.Frame(notebook, padx=5, pady=5)
    scientific_tab = tk.Frame(notebook, padx=5, pady=5)
    geometry_tab = tk.Frame(notebook, padx=5, pady=5)
    progression_tab = tk.Frame(notebook, padx=5, pady=5)

    notebook.add(basic_tab, text="Основная")
    notebook.add(scientific_tab, text="Научная")
    notebook.add(geometry_tab, text="Геометрия")
    notebook.add(progression_tab, text="Прогрессии")

    # ---------- Основная клавиатура ----------

    basic_buttons = [
        ("C", "clear"),
        ("⌫", "backspace"),
        ("(", "("),
        (")", ")"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("÷", "/"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("×", "*"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("−", "-"),
        ("0", "0"),
        (".", "."),
        ("xʸ", "**"),
        ("+", "+"),
        ("%", "%"),
        ("//", "//"),
        ("π", "pi"),
        ("e", "e"),
        ("x²", "**2"),
        ("√", "sqrt("),
        ("∛", "cbrt("),
        ("=", "equals"),
    ]

    create_button_grid(basic_tab, basic_buttons, columns=4)

    # ---------- Научные функции ----------

    scientific_buttons = [
        ("ln", "ln("),
        ("log₁₀", "log10("),
        ("log₂", "log2("),
        ("log(x, base)", "log("),
        ("sin°", "sind("),
        ("cos°", "cosd("),
        ("tan°", "tand("),
        ("sin rad", "sin("),
        ("cos rad", "cos("),
        ("tan rad", "tan("),
        ("asin", "asin("),
        ("acos", "acos("),
        ("atan", "atan("),
        ("root(x,n)", "root("),
        ("factorial", "factorial("),
        ("abs", "abs("),
        ("ceil", "ceil("),
        ("floor", "floor("),
        ("round", "round("),
        ("exp", "exp("),
        ("gcd", "gcd("),
        ("lcm", "lcm("),
    ]

    create_button_grid(scientific_tab, scientific_buttons, columns=4)

    # ---------- Геометрия ----------

    geometry_buttons = [
        ("Площадь круга", "circle_area("),
        ("Длина окружности", "circle_circumference("),
        ("Площадь прямоугольника", "rectangle_area("),
        ("Периметр прямоугольника", "rectangle_perimeter("),
        ("Площадь треугольника", "triangle_area("),
        ("Треугольник по 3 сторонам", "triangle_area_sides("),
        ("Площадь трапеции", "trapezoid_area("),
        ("Площадь правильного многоугольника", "polygon_area("),
        ("Объём куба", "cube_volume("),
        ("Площадь куба", "cube_area("),
        ("Объём параллелепипеда", "cuboid_volume("),
        ("Площадь параллелепипеда", "cuboid_area("),
        ("Объём шара", "sphere_volume("),
        ("Площадь шара", "sphere_area("),
        ("Объём цилиндра", "cylinder_volume("),
        ("Площадь цилиндра", "cylinder_area("),
        ("Объём конуса", "cone_volume("),
        ("Площадь конуса", "cone_area("),
        ("Объём призмы", "prism_volume("),
        ("Объём пирамиды", "pyramid_volume("),
    ]

    create_button_grid(geometry_tab, geometry_buttons, columns=2)

    # ---------- Прогрессии ----------

    progression_buttons = [
        ("n-й член АП", "ap_term("),
        ("Сумма АП", "ap_sum("),
        ("n-й член ГП", "gp_term("),
        ("Сумма ГП", "gp_sum("),
    ]

    create_button_grid(progression_tab, progression_buttons, columns=2)

    # ---------- Подсказка ----------

    help_text = (
        "Примеры: sqrt(144), log(100,10), root(27,3), "
        "triangle_area_sides(3,4,5), cube_volume(3), ap_sum(2,3,10). "
        "Нажми кнопку функции, введи аргументы и закрой скобку. "
        "Enter — вычислить, Esc — очистить."
    )

    tk.Label(
        root,
        text=help_text,
        font=FONT,
        justify="left",
        wraplength=820,
    ).pack(fill="x", pady=(8, 0))

    root.bind("<Return>", lambda event: calculate_result())
    root.bind("<KP_Enter>", lambda event: calculate_result())
    root.bind("<Escape>", lambda event: clear())

    expression_entry.focus_set()
    root.mainloop()


if __name__ == "__main__":
    run()