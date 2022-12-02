# ДЗ в процессе подготовки 

# 5911327426:AAFeYcF7b0WuuoDQhPY4Nk9_iwIoS68JVwo

import telebot
import output_data
import input_data

API_TOKEN = '5911327426:AAFeYcF7b0WuuoDQhPY4Nk9_iwIoS68JVwo'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Выберите действие: \nНайти контакт 'search'\nДобавить новый контакт 'add'")

# ПОИСК:
@bot.message_handler(commands = ['search'])
def search_message(message):
    bot.send_message(message.chat.id, "Введите Имя контакта: ")

@bot.message_handler(content_types = 'text')
def read_name(message):
    name = message.text
    bot.send_message(message.chat.id, output_data.read_contact(name))
    bot.send_message(message.chat.id, "Выберите действие: \nИзменить контакт 'change'\nУдалить контакт 'delete'")
    return name
# ПОИСК


# ИЗМЕНИТЬ:
@bot.message_handler(commands = ['change'])
def change_field(message):
    bot.send_message(message.chat.id, "Укажите поле, которое выхотите изменить (Name, Number, Category, Comment)")

@bot.message_handler(content_types = 'text')
def change_data(message):
    field = message.text
    bot.send_message(message.chat.id, "Введите новые данные")
    return field

@bot.message_handler(content_types = 'text')   
def show_change_info(message):
    new_data = message.text
    bot.send_message(message.chat.id, output_data.change_contact(read_name(), change_data(), new_data))
    # input_data.save_change(read_name(), change_data(), new_data)
    bot.send_message(message.chat.id, "Изменения сохранены.")
    # return output_data.change_contact(read_name(message.text), change_data(message.text), new_data)
# ИЗМЕНИТЬ

# УДАЛИТЬ:
@bot.message_handler(commands = ['delete'])
def delete_name(message):
    bot.send_message(message.chat.id, "Введите Имя контакта")

@bot.message_handler(commands = ['delete'])
def show_delete_info(message):
    bot.send_message(message.chat.id, output_data.search_contact(read_name(message)))
    output_data.delete_contact(read_name(message))
    # input_data.del_cobtact(message)
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


