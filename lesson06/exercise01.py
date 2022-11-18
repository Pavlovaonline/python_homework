import random

field = []
def print_field (pr_field):
    for i in range(3):
        print(" ".join(pr_field[i]))
    print("\n")

for i in range (3):
    filddraw = []
    for j in range(3):
        filddraw.append(".")
    field.append(filddraw)

def human_move ():
    x_human = int(input("Введите x координаты: "))
    y_human = int(input("Введите y координаты: "))
    field[x_human][y_human] = "o"
    print_field(field)

def bot_move ():
    x_bot = random.randint(0,2)
    y_bot = random.randint(0,2)
    if field[x_bot][y_bot]!=".":
        while field[x_bot][y_bot]!=".":
            x_bot = random.randint(0,2)
            y_bot = random.randint(0,2)
        field[x_bot][y_bot] = "x"
        print_field(field)
    else: 
        field[x_bot][y_bot] = "x"
        print_field(field)

def check_win ():
    if field[0][0] == "o" and field[0][1] == "o" and field[0][2] == "o": 
        print("Human win")
        return True
    elif field[1][0] == "o" and field[1][1] == "o" and field[1][2] == "o": 
        print("Human win")
        return True
    elif field[2][0] == "o" and field[2][1] == "o" and field[2][2] == "o": 
        print("Human win")
        return True
    elif field[0][0] == "o" and field[1][0] == "o" and field[2][0] == "o": 
        print("Human win")
        return True
    elif field[0][1] == "o" and field[1][1] == "o" and field[2][1] == "o": 
        print("Human win")
        return True
    elif field[0][2] == "o" and field[1][2] == "o" and field[2][2] == "o": 
        print("Human win")
        return True
    elif field[0][0] == "o" and field[1][1] == "o" and field[2][2] == "o": 
        print("Human win")
        return True
    elif field[0][2] == "o" and field[1][1] == "o" and field[2][0] == "o": 
        print("Human win")
        return True
    elif field[0][0] == "x" and field[0][1] == "x" and field[0][2] == "x": 
        print("Bot win")
        return True
    elif field[1][0] == "x" and field[1][1] == "x" and field[1][2] == "x": 
        print("Bot win")
        return True
    elif field[2][0] == "x" and field[2][1] == "x" and field[2][2] == "x": 
        print("Bot win")
        return True
    elif field[0][0] == "x" and field[1][0] == "x" and field[2][0] == "x": 
        print("Bot win")
        return True
    elif field[0][1] == "x" and field[1][1] == "x" and field[2][1] == "x": 
        print("Bot win")
        return True
    elif field[0][2] == "x" and field[1][2] == "x" and field[2][2] == "x": 
        print("Bot win")
        return True
    elif field[0][0] == "x" and field[1][1] == "x" and field[2][2] == "x": 
        print("Bot win")
        return True
    elif field[0][2] == "x" and field[1][1] == "x" and field[2][0] == "x": 
        print("Bot win")
        return True
    else: return False

def check_game_over ():
    if ("." in filddraw) and (check_win() == False):
        while ("." in filddraw) and (check_win() == False):
            human_move()
            bot_move()
    else: 
        print("Game over!")

print_field(field)
check_game_over()

# def check_win ():
#     for i in range (3):
#         for j in range (3):
#             if field[i][j] == "o":
#                 if field[i-1][j] == "o" and field[i-2][j] == "o":
#                     print("Human win")
#                     return True
#                 elif field[i-1][j] == "o" and field[i+1][j] == "o":
#                     print("Human win")
#                     return True
#                 elif field[i+1][j] == "o" and field[i+2][j] == "o":
#                     print("Human win")
#                     return True
#                 elif field[i][j-1] == "o" and field[i][j-2] == "o":
#                     print("Human win")
#                     return True
#                 elif field[i][j-1] == "o" and field[i][j+1] == "o":
#                     print("Human win")
#                     return True
#                 elif field[i][j+1] == "o" and field[i][j+2] == "o":
#                     print("Human win")
#                     return True
#                 elif field[i+1][j-1] == "o" and field[i-1][j+1] == "o":
#                     print("Human win")
#                     return True
#                 elif field[i+1][j-1] == "o" and field[i+2][j-2] == "o":
#                     print("Human win")
#                     return True
#                 elif field[i-1][j+1] == "o" and field[i-2][j+2] == "o":
#                     print("Human win")
#                     return True
#                 elif field[i-1][j+1] == "o" and field[i+1][j-1] == "o":
#                     print("Human win")
#                     return True
#                 elif field[i-1][j+1] == "o" and field[i-2][j+2] == "o":
#                     print("Human win")
#                     return True
#                 elif field[i+1][j-1] == "o" and field[i+2][j-2] == "o":
#                     print("Human win")
#                     return True