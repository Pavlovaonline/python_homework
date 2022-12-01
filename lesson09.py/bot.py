# ДЗ в процессе подготовки 

# 5911327426:AAFeYcF7b0WuuoDQhPY4Nk9_iwIoS68JVwo

import telebot

API_TOKEN = '5911327426:AAFeYcF7b0WuuoDQhPY4Nk9_iwIoS68JVwo'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Выберите действие: \nНайти контакт 'search'\nДобавить новый контакт 'add'")

# ПОИСК:
@bot.message_handler(commands = ['search'])
def search_message(message):
    bot.send_message(message.chat.id, "Введите Имя контакта: ")

# def search_contact(name):
#     # поиск в json имени, возврат всех данных
#     return name

@bot.message_handler(content_types = 'text')
def read_name(message):
#    search_contact(message.text)
   bot.send_message(message.chat.id, "Выберите действие: \nИзменить контакт 'change'\nУдалить контакт 'delete'")
# ПОИСК


# ИЗМЕНИТЬ:
@bot.message_handler(commands = ['change'])
def change_field(message):
    bot.send_message(message.chat.id, "Укажите поле, которое выхотите изменить (Name, Number, Category, Comment)")

# def change_contact(field, new_data):
#     # поиск в json имени, изменение данных в field на new_data, возврат всех данных.
#     return field, new_data

@bot.message_handler(content_types = 'text')
def change_data(message):
    field = message.text
    bot.send_message(message.chat.id, "Введите новые данные")

@bot.message_handler(content_types = 'text')
def show_change_info(message):
    # change_contact(read_field(message).field, message.text)
    bot.send_message(message.chat.id, "Изменения сохранены.")
# ИЗМЕНИТЬ

# УДАЛИТЬ:
@bot.message_handler(commands = ['delete'])
def delete_name(message):
    # search_contact(read_name(message))
    bot.send_message(message.chat.id, "Введите Имя контакта")

@bot.message_handler(commands = ['delete'])
def show_delete_info(message):
    bot.send_message(message.chat.id, "Данные удалены")
# УДАЛИТЬ



# ДОБАВИТЬ НОВЫЙ КОНТАКТ:
@bot.message_handler(commands = ['add'])
def add_name(message):
    bot.send_message(message.chat.id, "Введите имя контакта")

@bot.message_handler(content_types = 'text')
def add_number(message):
   bot.send_message(message.chat.id, "Введите номер контакта")

@bot.message_handler(content_types = 'text')
def add_category(message):
   bot.send_message(message.chat.id, "Введите категорию контакта")

@bot.message_handler(content_types = 'text')
def add_comment(message):
   bot.send_message(message.chat.id, "Введите комментарий к контакту")

@bot.message_handler(content_types = 'text')
def show_add_info(message):
   bot.send_message(message.chat.id, "Контакт добавлен.")
# ДОБАВИТЬ НОВЫЙ КОНТАКТ

bot.polling()


