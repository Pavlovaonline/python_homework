try:
    x = int(input("Введите номер дня недели (1 - понедельник, 7 - воскресенье): "))
    if x > 0 and x < 6: print("будний день")
    elif x > 5 and x < 8: print("выходной день")
    else: print ("некорректный номер дня недели")
except: print("Некорректные данные...")
