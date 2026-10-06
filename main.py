import tkinter as tk
from tkinter import messagebox


# Завдання 1
def task1():
    window = tk.Toplevel()
    window.title("Завдання 1")
    window.geometry("300x150")

    label = tk.Label(window, text="Натисніть кнопку для виходу")
    label.pack(pady=20)

    exit_button = tk.Button(
        window,
        text="Вихід",
        command=window.destroy
    )
    exit_button.pack()


# Завдання 2
def task2():
    window = tk.Toplevel()
    window.title("Завдання 2")
    window.geometry("400x200")

    entry = tk.Entry(window, width=30)
    entry.pack(pady=20)

    label = tk.Label(window, text="Тут з'явиться введений текст")
    label.pack(pady=10)

    def confirm():
        label.config(text=entry.get())

    button = tk.Button(
        window,
        text="Підтвердити",
        command=confirm
    )
    button.pack()


# Завдання 3
def task3():
    window = tk.Toplevel()
    window.title("Завдання 3")
    window.geometry("400x250")

    language = tk.StringVar(value="Python")

    tk.Label(
        window,
        text="Оберіть мову програми:"
    ).pack(pady=10)

    languages = ["Python", "Java", "C++"]

    for lang in languages:
        tk.Radiobutton(
            window,
            text=lang,
            variable=language,
            value=lang,
            command=lambda: messagebox.showinfo(
                "Вибір мови",
                "Ви обрали: " + language.get()
            )
        ).pack()


# Завдання 4
def task4():
    window = tk.Toplevel()
    window.title("Завдання 4")
    window.geometry("400x250")

    days = [
        "Понеділок",
        "Вівторок",
        "Середа",
        "Четвер",
        "П'ятниця",
        "Субота",
        "Неділя"
    ]

    months = [
        "Січень",
        "Лютий",
        "Березень",
        "Квітень",
        "Травень",
        "Червень",
        "Липень",
        "Серпень",
        "Вересень",
        "Жовтень",
        "Листопад",
        "Грудень"
    ]

    day = tk.StringVar(value=days[0])
    month = tk.StringVar(value=months[0])

    tk.Label(window, text="Оберіть день:").pack(pady=5)

    day_menu = tk.OptionMenu(
        window,
        day,
        *days
    )
    day_menu.pack()

    tk.Label(window, text="Оберіть місяць:").pack(pady=5)

    month_menu = tk.OptionMenu(
        window,
        month,
        *months
    )
    month_menu.pack()

    def show_date():
        messagebox.showinfo(
            "Обрана дата",
            "Ви обрали: " + day.get() + ", " + month.get()
        )

    button = tk.Button(
        window,
        text="Показати дату",
        command=show_date
    )
    button.pack(pady=15)


# Завдання 5
def task5():
    window = tk.Toplevel()
    window.title("Завдання 5")
    window.geometry("300x400")

    expression = tk.StringVar()

    display = tk.Entry(
        window,
        textvariable=expression,
        font=("Arial", 18),
        justify="right"
    )
    display.pack(
        padx=10,
        pady=10,
        fill="x"
    )

    def add_symbol(symbol):
        expression.set(expression.get() + symbol)

    def calculate():
        try:
            result = eval(expression.get())
            expression.set(str(result))
        except:
            expression.set("Помилка")

    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", "+", "(", ")"]
    ]

    for row in buttons:
        frame = tk.Frame(window)
        frame.pack()

        for button_text in row:
            button = tk.Button(
                frame,
                text=button_text,
                width=5,
                height=2,
                command=lambda x=button_text: add_symbol(x)
            )
            button.pack(
                side="left",
                padx=2,
                pady=2
            )

    result_button = tk.Button(
        window,
        text="Результат",
        width=22,
        height=2,
        command=calculate
    )
    result_button.pack(pady=10)


# Головне вікно
root = tk.Tk()
root.title("Практична робота")
root.geometry("400x400")

title = tk.Label(
    root,
    text="Оберіть завдання",
    font=("Arial", 16)
)
title.pack(pady=20)


button1 = tk.Button(
    root,
    text="Завдання 1 — Вихід",
    width=30,
    command=task1
)
button1.pack(pady=5)

button2 = tk.Button(
    root,
    text="Завдання 2 — Введення тексту",
    width=30,
    command=task2
)
button2.pack(pady=5)

button3 = tk.Button(
    root,
    text="Завдання 3 — Вибір мови",
    width=30,
    command=task3
)
button3.pack(pady=5)

button4 = tk.Button(
    root,
    text="Завдання 4 — День і місяць",
    width=30,
    command=task4
)
button4.pack(pady=5)

button5 = tk.Button(
    root,
    text="Завдання 5 — Калькулятор",
    width=30,
    command=task5
)
button5.pack(pady=5)


root.mainloop()