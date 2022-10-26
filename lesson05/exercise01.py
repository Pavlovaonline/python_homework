# from curses.ascii import isdigit
from random import randint
from turtle import st

candies = 2021
max_step = 28
print("Правила:\n\tЗа один ход вы можете взять не менее 0 и не более 28 конфет\n\tПобеждает тот, кто забирает последнюю конфету.")

i = randint(1, 2)

def human_action (): 
    try:
        # step = int(input("Сколько конфет вы хотите взять? "))
        step = randint(0, 28)
        print(f"Вы взяли {step} конфет")
        # if not isdigit(step):
        #     print("Введите целое число.")
        #     human_action
        if step < 0 or step > max_step:
            print ("Вы можете взять не больше 28 конфет.")
            human_action
        if step <= 0 or step >= max_step:
            candies -= step
        print(f"Осталось {candies} конфет.")
    except: print("Что-то не так.")

def bot_action ():
    try:
        if i == 2:
            candies -= 0
        elif i == 1:
            if candies == 2021:
                step = candies - (candies % (max_step+1))
                print(f"Бот взял {step} конфет")
            elif candies >= (max_step+1):
                step = max_step - (candies % (max_step+1))
                print(f"Бот взял {step} конфет")
            elif candies <= (max_step+1):
                step = candies - 1
                print(f"Бот взял {step} конфет")
            candies -= step
    except: print("Что-то не так.")

while candies < 0:
    print(bot_action())
    print(human_action())
    print("Game over")
