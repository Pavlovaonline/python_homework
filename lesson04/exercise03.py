from random import randint
k = int(input("Введите степень многочлена: "))

def generate_polynom (degree):
    polynom = ""
    if k > 1:
        polynom = f"{randint(1, 100)}*x^{k}"
        for i in range(k-1, 1, -1):
            n = randint(0, 10)
            if n == 0:
                continue
            if n == 1:
                polynom += f"+x^{i}"
            else:
                polynom += f"+{n}*x^{i}"
        polynom += "+"
    if k > 0:
        b = randint(0, 100)
        if b == 1:
            polynom += f"x"
        elif b > 1:
            polynom += f"{b}*x"
        c = randint(0, 100)
        if c > 0:
            polynom += f"+{c}"
        polynom += "=0"
    return polynom

def io_polynom (polynom):
    with open("C:/GB/Python/homework/lesson04/file_exercise03.txt", "w") as fl:
        fl.write(polynom)
    with open("C:/GB/Python/homework/lesson04/file_exercise03.txt", "r") as fl:
        return fl.readline()

polynom01 = generate_polynom(k)
print(f"Сгенерированный полином:{polynom01}")
print(f"Cодержимое файла: {io_polynom(polynom01)}")

    # try:
    #     fi = open('C:/GB/Python/homework/lesson04/file_exercise03.txt', 'w')
    #     fi.write(polynom)
    #     fi = open('C:/GB/Python/homework/lesson04/file_exercise03.txt', 'r')
    #     print(f"Cодержимое файла: {fi.readline()}")
    # finally:
    #     fi.close()