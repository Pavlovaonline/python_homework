from tkinter import *
from tkinter import ttk
# import log
import real_num

window_calc = Tk()
window_calc.title("METANIT.COM")
window_calc.geometry("500x500")


def read_logs ():
    with open("C:/GB/Python/homework/lesson07/exercise/logs.txt", "r") as file:
        return file.readlines()

def input_text():
    label_text = ttk.Label(text="Enter math expression:")
    label_text.grid(row=1, column=1, padx=10, pady=10)
    entry = ttk.Entry()
    entry.grid(row=1, column=2, padx=10, pady=10)

def btn_count_res():
    btn_count = ttk.Button(text="Count", command = lambda:[real_num.get_result()])
    btn_count.grid(row=2, column=1, padx=10, pady=10)

def print_result():
    label_math_ex = ttk.Label(text = real_num.get_result())
    label_math_ex.grid(row=3, column=1, padx=10, pady=10)
    result = str(real_num.get_result())
    return result

def btn_read_log ():
    btn_log = ttk.Button(text="Get log", command = read_logs ())
    btn_log.grid(row=2, column=2, padx=10, pady=10)

def print_log():
    label_log = ttk.Label(text = str(read_logs ()))
    label_log.grid(row=3, column=2, padx=10, pady=10)

input_text()
btn_count_res()
btn_read_log ()
print_result()
print_log()

window_calc.mainloop()




