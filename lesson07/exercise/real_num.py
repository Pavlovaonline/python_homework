import re



def read_expression ():
    with open("C:/GB/Python/homework/lesson07/exercise/logs.txt", "r") as file:
        text = file.readline()
        sp_operation = re.findall('[+,-,*,/]+', text[3])
        sp_text = list(text.replace(" ", ""))
        return sp_text
        
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
    elif sp[1] == "*":
        res = float(sp[0])*float(sp[2])
    else: res = "I don't know"
    return "Результат выражения: ", res

def get_result():
    div(read_expression())
    first_operation(read_expression())
    subtract(read_expression())
    second_operation(read_expression())
    last_operation(read_expression())
    
