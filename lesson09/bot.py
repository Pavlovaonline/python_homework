import re
import telebot
import random

API_TOKEN = '5911327426:AAFeYcF7b0WuuoDQhPY4Nk9_iwIoS68JVwo'

bot = telebot.TeleBot(API_TOKEN)
global x
global y

@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Начало игры")
    bot.send_message(message.chat.id, "Введите x координаты: ")

@bot.message_handler(content_types = 'text')
def read_x(message):
    global x
    x = message.text
    bot.send_message(message.chat.id, f"x={x}\nВведите y координаты: ")

@bot.message_handler(content_types = 'text')
def read_y(message):
    global y
    y = message.text
    bot.send_message(message.chat.id, f"y={y}")

@bot.message_handler(content_types = 'text')
def read_coord(message):    
    global x
    global y
    bot.send_message(message.chat.id, f"Вы ввели координаты: {x}, {y}")

@bot.message_handler(content_types = 'text')
def print_field_bot (message):
    bot.send_message(message.chat.id, print_field(field))
    bot.send_message(message.chat.id, check_game_over())
    bot.send_message(message.chat.id, "Чтобы начать снова введите /start")

# bot.polling()


field = []
def print_field (pr_field):
    for i in range(3):
        return " ".join(pr_field[i])

for i in range (3):
    filddraw = []
    for j in range(3):
        filddraw.append(".")
    field.append(filddraw)

def human_move ():
    global x
    global y
    # x_human = x
    # y_human = y
    field[x][y] = "o"
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
        game_over = True
        return "Human win"
    elif field[1][0] == "o" and field[1][1] == "o" and field[1][2] == "o": 
        game_over = True
        return "Human win"
    elif field[2][0] == "o" and field[2][1] == "o" and field[2][2] == "o": 
        game_over = True
        return "Human win"
    elif field[0][0] == "o" and field[1][0] == "o" and field[2][0] == "o": 
        game_over = True
        return "Human win"
    elif field[0][1] == "o" and field[1][1] == "o" and field[2][1] == "o": 
        game_over = True
        return "Human win"
    elif field[0][2] == "o" and field[1][2] == "o" and field[2][2] == "o": 
        game_over = True
        return "Human win"
    elif field[0][0] == "o" and field[1][1] == "o" and field[2][2] == "o": 
        game_over = True
        return "Human win"
    elif field[0][2] == "o" and field[1][1] == "o" and field[2][0] == "o": 
        game_over = True
        return "Human win"
    elif field[0][0] == "x" and field[0][1] == "x" and field[0][2] == "x": 
        game_over = True
        return "Bot win"
    elif field[1][0] == "x" and field[1][1] == "x" and field[1][2] == "x": 
        game_over = True
        return "Bot win"
    elif field[2][0] == "x" and field[2][1] == "x" and field[2][2] == "x": 
        game_over = True
        return "Bot win"
    elif field[0][0] == "x" and field[1][0] == "x" and field[2][0] == "x": 
        game_over = True
        return "Bot win"
    elif field[0][1] == "x" and field[1][1] == "x" and field[2][1] == "x": 
        return "Bot win"
    elif field[0][2] == "x" and field[1][2] == "x" and field[2][2] == "x": 
        game_over = True
        return "Bot win"
    elif field[0][0] == "x" and field[1][1] == "x" and field[2][2] == "x": 
        game_over = True
        return "Bot win"
    elif field[0][2] == "x" and field[1][1] == "x" and field[2][0] == "x": 
        game_over = True
        return "Bot win"
    else: 
        game_over = False
        return game_over

def check_game_over ():
    if ("." in filddraw) and (check_win() == False):
        while ("." in filddraw) and (check_win() == False):
            human_move()
            bot_move()
    else: 
        return("Game over!")

bot.polling()
