from tkinter import *
from tkinter import ttk
import output_log
import input_log

window_calc = Tk()
window_calc.title("METANIT.COM")
window_calc.geometry("1000x750")

def print_vacancy():
    label_math_ex = ttk.Label(text = output_log.vacancy())
    label_math_ex.grid(row=1, column=2, padx=10, pady=10)
    result = str(output_log.vacancy())
    return result

def btn_vacancy():
    btn_count = ttk.Button(text="Показать свободные места", command = output_log.vacancy())
    btn_count.grid(row=1, column=1, padx=10, pady=10)
    print_vacancy()

def print_booked():
    label_math_ex = ttk.Label(text = output_log.booked())
    label_math_ex.grid(row=2, column=2, padx=10, pady=10)
    result = str(output_log.booked())
    return result

def btn_booked():
    btn_count = ttk.Button(text="Показать занятые места", command = output_log.booked())
    btn_count.grid(row=2, column=1, padx=10, pady=10)
    print_booked()

def print_rating():
    label_math_ex = ttk.Label(text = output_log.rating())
    label_math_ex.grid(row=3, column=2, padx=10, pady=10)
    result = str(output_log.vacancy())
    return result

def btn_rating():
    btn_count = ttk.Button(text="Показать количество набранных рейтингов", command = output_log.rating())
    btn_count.grid(row=3, column=1, padx=10, pady=10)
    print_rating()


def btn_rating():
    btn_count = ttk.Button(text="Удалить занятое место", command = output_log.rating())
    btn_count.grid(row=3, column=1, padx=10, pady=10)
    print_rating()

def input_text():
    label_text = ttk.Label(text="Введите номер выхода, который хотите занять: ")
    label_text.grid(row=4, column=1, padx=10, pady=10)
    entry = ttk.Entry()
    entry.grid(row=5, column=1, padx=10, pady=10)
    text = str(entry.get())
    return text

def btn_add_spot():
    btn_count = ttk.Button(text="Занять выбранное место", command = input_log.add_new_ads())
    btn_count.grid(row=5, column=1, padx=10, pady=10)

def btn_del_spot():
    btn_count = ttk.Button(text="Удалить выбранное место", command = input_log.del_ads())
    btn_count.grid(row=7, column=1, padx=10, pady=10)

with open("C:/GB/Python/homework/lesson07/calculator/logs.txt", "a") as file:
        file.write(input_text())

btn_vacancy()
btn_booked()
btn_rating()
input_text()
btn_add_spot()
btn_del_spot()

window_calc.mainloop()




