try: 
    a = int(input("Введите число: "))
    sp = []
    f = 1
    n = 1
    for i in range (1, (a+1), 1):
        for j in range(1, (i), 1):
            i*=j
        sp.append(i)
    print(sp)
except: ("Введны неверные данные")