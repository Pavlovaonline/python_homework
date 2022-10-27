# dig_sp = "овывдл абв лваыьб абваб лывывь абва аббв"

# def del_abc (st):
#     sp = st.split(" ")
#     i = 0
#     del_abc_sp = []
#     while i < len(sp):
#         if "абв" not in sp[i]:
#             del_abc_sp.append(sp[i])
#         i += 1
#     return del_abc_sp
    
# print(del_abc(dig_sp))

from random import randint


candies = 2021
max_step = 28
print("Правила:\n\tЗа один ход вы можете взять не менее 0 и не более 28 конфет\n\tПобеждает тот, кто забирает последнюю конфету.")
i = int(randint(1, 2))

# def human_action (step): 
#     try:
#         # step = randint(1, 28)
#         print(f"Вы взяли {step} конфет")
#         if step <= 0 or step > max_step:
#             print ("Вы можете взять не больше 28 конфет.")
#             human_action
#         if step > max_step:
#             print ("Вы можете взять меньше 1 конфеты.")
#             human_action
#         else:
#             candies -= step
#         print(f"Осталось {candies} конфет.")
#         return candies
#     except: print("Что-то не так.")
# human_action(step)

def human_action (candies): 
    try:
        step = int(input("Сколько конфет вы хотите взять? "))
        print(f"Вы взяли {step} конфет")
        if step > candies:
            print (f"Вы можете взять не больше {candies} конфет.")
            human_action
        elif step <= candies:
            if step <= 0 or step > max_step:
                print ("Вы можете взять не больше 28 конфет.")
                human_action
            elif step > max_step:
                print ("Вы можете взять меньше 1 конфеты.")
                human_action
            else:
                candies -= step
        print(f"Осталось {candies} конфет.")
        return candies
    except: print("Что-то не так.")


def bot_action (candies):
    try:
        if candies == 2021:
            step = candies % (max_step+1)
            # print(f"Бот взял {step} конфет")
        elif candies > (max_step+1) and candies < 2021:
            step = max_step - (candies % (max_step+1))
            # print(f"Бот взял {step} конфет")
        elif candies <= (max_step+1):
            step = candies - 1
        print(f"Бот взял {step} конфет")
        candies -= step
        return candies
    except: print("Что-то не так.")



if i == 1:
    print("Первым ходит робот")
    while candies!=0:
        if candies>0:
            bot_action(candies)
            human_action(candies)
        else:
            print("Game over")   
elif i == 2: 
    print("Первым ходит человек")
    while candies!=0:  
        if candies>0:
            human_action(candies)
            bot_action(candies)
        else:
            print("Game over")  
