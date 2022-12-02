import json
import output_data

with open("C:/GB/Python/homework/lesson09/data_bot.json", "r", encoding="utf-8") as file:
    data = json.load(file)["report"]

def save_change(name, field, new_data):
    dict = {}
    dict_contact =  {}
    for i in range(0, len(data), 1):
        dict = data[i]
        for i in range(0, len(dict), 1):
            if name in dict.get("Name"):
                dict_contact.update(dict)
    if field == "Name":
        dict_contact["Name"] = new_data
    if field == "Number":
        dict_contact["Number"] = new_data
    if field == "Category":
        dict_contact["Category"] = new_data
    if field == "Comment":
        dict_contact["Comment"] = new_data
    number = dict_contact.get("Number")
    category = dict_contact.get("Category")
    if dict_contact.get("Comment") == "":
        comment = "отсутствует"
    else: comment = dict_contact.get("Comment")
    new_data = data.update(dict_contact)
    json.dump(new_data, file)


def del_cobtact(name):
    dict = {}
    for i in range(0, len(data), 1):
        dict = data[i]
        if name == dict.get("Name"):
            del data[i]
            break
    json.dump(data, file)


