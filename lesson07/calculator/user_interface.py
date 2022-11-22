from tkinter import *
from tkinter import ttk

import output_log
import count_res

window_calc = Tk()
window_calc.title("METANIT.COM")
window_calc.geometry("500x500")

def input_text():
    label_text = ttk.Label(text="Введите математическое выражение: ")
    label_text.grid(row=1, column=1, padx=10, pady=10)
    entry = ttk.Entry()
    entry.grid(row=1, column=2, padx=10, pady=10)

def print_result(res):
    label_math_ex = ttk.Label(text = res)
    label_math_ex.grid(row=3, column=1, padx=10, pady=10)
    result = str(count_res.get_result())
    return result

def btn_count_res():
    btn_count = ttk.Button(text="Посчитать", command = lambda:[count_res.get_result()])
    btn_count.grid(row=2, column=1, padx=10, pady=10)
    print_result(count_res.get_result())


def print_log(log):
    label_log = ttk.Label(text = log)
    label_log.grid(row=3, column=2, padx=10, pady=10)

def btn_read_log ():
    btn_log = ttk.Button(text="Показать логи", command = print_log(output_log.read_log()))
    btn_log.grid(row=2, column=2, padx=10, pady=10)
    # print_log(str(output_log.read_log()))


input_text()
btn_count_res()
btn_read_log ()

window_calc.mainloop()




