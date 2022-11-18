import re

text = str(input("Введите арифметическое выражение: "))
sp_operation = re.findall('[+,-,*,/]+', text)
sp_text = list(text.replace(" ", ""))
    
def div(sp):
    for i in range(len(sp)):
        if sp[i] == "/":
            sp[i] = "*"
            sp[i+1] = 1/float(sp[i+1])

def subtract(sp):
    for i in range(len(sp)):
        if sp[i] == "-":
            sp[i] = "+"
            sp[i+1] = -1*float(sp[i+1])

def first_operation(sp):
    for i in range(len(sp)):
        if sp[i] == "*":
            res = float(sp[i-1])*float(sp[i+1])
            sp[i-1] = res
            sp.pop(i)
            sp.append(" ")
            sp.pop(i)
            sp.append(" ")
    while sp.count(" ") > 0:
        sp.remove(" ")

def second_operation(sp):
    for i in range(len(sp)):
        if sp[i] == "+":
            res = float(sp[i-1])+float(sp[i+1])
            sp[i-1] = res
            sp.pop(i)
            sp.append(" ")
            sp.pop(i)
            sp.append(" ")
    while sp.count(" ") > 0:
        sp.remove(" ")

def last_operation(sp):
    if sp[1] == "+":
        res = float(sp[0])+float(sp[2])
    if sp[1] == "*":
        res = float(sp[0])*float(sp[2])
    print("Результат выражения: ", res)

def calc_result(sp):
    div(sp)
    first_operation(sp)
    subtract(sp)
    second_operation(sp)
    last_operation(sp)
    
calc_result(sp_text)
