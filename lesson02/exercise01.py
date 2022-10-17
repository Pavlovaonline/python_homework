try:
    a = float(input("Введите число: "))
    s = str(a)
    sum = 0
    if "." in s:
        fraction = len(str(a).split(".")[1])
        convert_num = a*(10**fraction)
    else:
        convert_num = a
    while(convert_num > 0):
        dig = convert_num % 10
        sum = round(sum + dig)
        convert_num = convert_num//10
    print("Сумма цифр равна:", sum)
except: print("Введены неверные данные")