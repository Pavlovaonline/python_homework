# ДЗ в процессе подготовки 

# 5911327426:AAFeYcF7b0WuuoDQhPY4Nk9_iwIoS68JVwo

import telebot
import output_data
import input_data

API_TOKEN = '5911327426:AAFeYcF7b0WuuoDQhPY4Nk9_iwIoS68JVwo'

bot = telebot.TeleBot(API_TOKEN)

global field
global name
global number
global category
global comment

@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Выберите действие: \nНайти контакт 'search'\nДобавить новый контакт 'add'")

# ПОИСК:
@bot.message_handler(commands = ['search'])
def search_message(message):
    bot.send_message(message.chat.id, "Поиск контакта")

# ИЗМЕНИТЬ:
@bot.message_handler(commands = ['change'])
def change_field(message):
    bot.send_message(message.chat.id, "Изменение контакта")


# УДАЛИТЬ:
@bot.message_handler(commands = ['delete'])
def show_delete_info(message):
    bot.send_message(message.chat.id, output_data.read_contact(name))
    # output_data.delete_contact(name)
    # input_data.del_cobtact(message)
    bot.send_message(message.chat.id, "Данные удалены")

# ДОБАВИТЬ НОВЫЙ КОНТАКТ:
@bot.message_handler(commands = ['add'])
def add_name(message):
    bot.send_message(message.chat.id, "Добавление нового контакта")



# ПОИСК: 
@bot.message_handler(content_types = 'text')
def read_name(message):
    global name
    bot.send_message(message.chat.id, "Введите Имя контакта: ")
    name = message.text
    bot.send_message(message.chat.id, output_data.read_contact(name))
    bot.send_message(message.chat.id, "Выберите действие: \nИзменить контакт 'change'\nУдалить контакт 'delete'")

# ИЗМЕНИТЬ:
@bot.message_handler(content_types = 'text')
def change_data(message):
    global field 
    bot.send_message(message.chat.id, "Укажите поле, которое выхотите изменить (Name, Number, Category, Comment)")
    field = message.text
    bot.send_message(message.chat.id, "Введите новые данные")

@bot.message_handler(content_types = 'text')   
def show_change_info(message):
    new_data = message.text
    bot.send_message(message.chat.id, output_data.change_contact(read_name(), change_data(), new_data))
    # input_data.save_change(read_name(), change_data(), new_data)
    bot.send_message(message.chat.id, "Изменения сохранены.")
    # return output_data.change_contact(read_name(message.text), change_data(message.text), new_data)


# ДОБАВИТЬ НОВЫЙ КОНТАКТ:
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


