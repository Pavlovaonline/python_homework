from random import randint

candies = 2021
initial_quantity = 2021
max_step = 28
print("Правила:\n\tЗа один ход вы можете взять не менее 0 и не более 28 конфет\n\tПобеждает тот, кто забирает последнюю конфету.")
new_candies = 0

def human_action (candies): 
    try:
        if candies == 1:
            print("Вы проиграли\n\nGame over!")
        else:
            step = int(input("Сколько конфет вы хотите взять? "))
            if step > candies:
                print (f"Вы можете взять не больше {candies} конфет.")
                human_action
            elif step <= candies:
                if step > max_step:
                    print ("Вы можете взять не больше 28 конфет.")
                    human_action
                elif step < 1:
                    print ("Вы можете взять меньше 1 конфеты.")
                    human_action
                else:
                    print(f"Вы взяли {step} конфет")
                    candies = candies - step
            print(f"Осталось {candies} конфет.")
            return candies
    except: print("Попробуйте ещё раз.")


def bot_action (candies):
    try:
        if candies == 1:
            print("Вы выиграли\n\nGame over!")
        else: 
            if candies == initial_quantity:
                step = candies % (max_step+1)
            elif candies > (max_step+1) and candies < initial_quantity:
                step = max_step - (candies % (max_step+1))
            elif candies <= (max_step+1):
                step = candies - 1
            print(f"Бот взял {step} конфет.")
            candies = candies - step
            print(f"Осталось {candies} конфет.")
            return candies
    except: print("Что-то не так.")

i = int(randint(1, 2)) 
if i == 2:
    print("Бот ходит первым.")
    while candies!=0:
        if candies>0:
            candies = bot_action(candies)
            candies = human_action(candies)
            
elif i == 1: 
    print("Вы ходите первым.")
    while candies!=0:  
        if candies>0:
            candies = human_action(candies)
            candies = bot_action(candies)