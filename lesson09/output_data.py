import json

with open("C:/GB/Python/homework/lesson09/data_bot.json", "r", encoding="utf-8") as file:
    data = json.load(file)["report"]

def read_contact(name):
    dict = {}
    dict_contact =  {}
    for i in range(0, len(data), 1):
        dict = data[i]
        for i in range(0, len(dict), 1):
            if name in dict.get("Name"):
                dict_contact.update(dict)
    number = dict_contact.get("Number")
    category = dict_contact.get("Category")
    if dict_contact.get("Comment") == "":
        comment = "отсутствует"
    else: comment = dict_contact.get("Comment")
    return (f"Имя: {name} \nНомер: {number} \nКатегория: {category} \nКомментарий: {comment}")

def change_contact (name, field, new_data):
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
    return (f"Новые данные контакта:\nИмя: {name} \nНомер: {number} \nКатегория: {category} \nКомментарий: {comment}")

def delete_contact(name):
    dict = {}
    for i in range(0, len(data), 1):
        dict = data[i]
        if name == dict.get("Name"):
            del data[i]
            break
    return data

def add_contact (name, number, category, comment):
    dict_contact =  {}
    for i in range(0, len(data), 1):
        dict = data[i]
        if name in dict.get("Name"):
            return "Имя должно быть уникальным"
            continue
        elif number in dict.get("Number"):
            return "Номер должен быть уникальным"
            continue
        else:
            dict_contact =  {"Name": name, "Number": number, "Category": category, "Comment": comment}
            data.append(dict_contact)
            break
    return data


# print(read_contact("Кольцов Александр"))
# print()
# print(change_contact ("Кольцов Александр", "Number", "8900111550177"))
# print()
# print(delete_contact("Кольцов Александр"))
# print()
# print(data)
# print()
# print()
# print(add_contact ("name1", "number1", "category1", "comment1"))
