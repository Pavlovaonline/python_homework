from pickle import NONE
try: 
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    operation = input("Введите операцию: ")
    if operation == "+": 
        c = a+b
    elif operation == "-": 
        c = a-b
    elif operation == "*": 
        c = a*b
    elif operation == "/":
        if b == 0: 
            print("Делить на 0 нельзя!")
        else: 
            c = a/b
    elif operation == "mod": 
        c=a%b
    elif operation == "pow": 
        c=a**b
    elif operation == "div": 
        if b == 0: 
            print("Делить на 0 нельзя!")
        else: 
            c = a//b
    print(round(c, 3))
except: print("Некорректные данные...")

