import telebot
import random
from telebot import types

API_TOKEN = '5911327426:AAFeYcF7b0WuuoDQhPY4Nk9_iwIoS68JVwo'
bot = telebot.TeleBot(API_TOKEN)
item = {}
gameIsStart = False
game_field = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " ", ]
CrossesOrToe = ["0", "X"]
playerSymbol = CrossesOrToe[random.randint(0, 1)]
botSymbol = ""
if (playerSymbol == "0"):
    botSymbol = "X"
else:
    botSymbol = "0"
print("Bot is start")
winbool = False
losebool = False

def clear():
    global game_field
    game_field = [" ", " ", " ",
                  " ", " ", " ",
                  " ", " ", " ", ]

def human_win(cell_1, cell_2, cell_3):
    if cell_1 == playerSymbol and cell_2 == playerSymbol and cell_3 == playerSymbol:
        global winbool
        winbool = True

def bot_win(cell_1, cell_2, cell_3):
    if cell_1 == botSymbol and cell_2 == botSymbol and cell_3 == botSymbol:
        global losebool
        losebool = True

def defend(cell_1, cell_2, posDef):
    if cell_1 == playerSymbol and cell_2 == playerSymbol:
        posDef = botSymbol

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item[0] = types.KeyboardButton("Крестики нолики")
    markup.add(item[0])
    if message.text == "/start":
        bot.send_message(message.chat.id,
                         "Привет,{0.first_name}!".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    if message.chat.type == 'private':
        if message.text == "Крестики нолики":
            global gameIsStart
            gameIsStart = True
        else: 
            bot.send_message(message.chat.id, "Я умею только играть в крестики")
    if gameIsStart == True:
        item = {}
        bot.send_message(message.chat.id, "Игра началась")
        global markup
        markup = types.InlineKeyboardMarkup(row_width=3)
        i = 0
        for i in range(9):
            item[i] = types.InlineKeyboardButton(game_field[i], callback_data=str(i))
        markup.row(item[0], item[1], item[2])
        markup.row(item[3], item[4], item[5])
        markup.row(item[6], item[7], item[8])
        bot.send_message(message.chat.id, "Ваш ход", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callbackInline(call):
    if (call.message):
        randomCell = random.randint(0, 8)
        if game_field[randomCell] == playerSymbol:
            randomCell = random.randint(0, 8)
        if game_field[randomCell] == botSymbol:
            randomCell = random.randint(0, 8)
        if game_field[randomCell] == " ":
            game_field[randomCell] = botSymbol
        for i in range(9):
            if call.data == str(i):
                if (game_field[i] == " "):
                    game_field[i] = playerSymbol
            if human_win(game_field[0], game_field[1], game_field[2]): break
            if human_win(game_field[0], game_field[4], game_field[8]): break
            if human_win(game_field[6], game_field[4], game_field[2]): break
            if human_win(game_field[6], game_field[7], game_field[8]): break
            if human_win(game_field[0], game_field[3], game_field[6]): break
            if bot_win(game_field[0], game_field[1], game_field[2]): break
            if bot_win(game_field[0], game_field[4], game_field[8]): break
            if bot_win(game_field[6], game_field[4], game_field[2]): break
            if bot_win(game_field[6], game_field[7], game_field[8]): break
            if bot_win(game_field[0], game_field[3], game_field[6]): break
            item[i] = types.InlineKeyboardButton(game_field[i], callback_data=str(i))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Крестики нолики", reply_markup=None)
        global  markup
        markup.row(item[0], item[1], item[2])
        markup.row(item[3], item[4], item[5])
        markup.row(item[6], item[7], item[8])
        bot.send_message(call.message.chat.id, "Выберите клетку", reply_markup=markup)
        global winbool
        if winbool:
            clear()
            bot.send_message(call.message.chat.id, "Вы победили!")
            winbool = False
            gameIsStart = False
        global losebool
        if losebool:
            clear()
            bot.send_message(call.message.chat.id, "Бот победил!")
            losebool = False
            gameIsStart = False

bot.polling(none_stop=True)