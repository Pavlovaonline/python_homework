n = int(input("Введите число: "))

def dig_in_bin (x):
    s = ""
    try: 
        while x != 0:
            s += str(x % 2)
            x = x // 2
        return s[::-1]
    except: print("Что-то пошло не так")

print(dig_in_bin(n))