import json
import user_interface


with open("C:/GB/Python/homework/lesson08/advertising.json", "r", encoding="utf-8") as file:
    data = json.load(file)["report"]


def add_new_ads ():
    num = search.num
    for txt in data['report']:
        if txt["ID"] == num:
            if txt["ads"] == "True":
                return "Этот выход уже занят"
            if txt["ads"] == "False":
                add_data(num)

def add_data():
    spot_data = []
    dict_data = []
    num_id = str(search.num)
    for txt in data['report']:
        spot_data = txt["ID"], txt['TV channel'], txt["date"], txt["time"], txt["programme"], txt["rating"], txt['ads']
        dict_data.append(spot_data)
    for txt in data['report']:
        if txt["ID"] == num_id:
            dict_data['report']["ID":num_id]["ads"] = "True"
    return dict_data

def del_ads (num):
    num = search.num
    for txt in data['report']:
        if txt["ID"] == num:
            if txt["ads"] == "False":
                return "Выход не занят. Выберете другое место."
            if txt["ads"] == "True":
                del_data(num)

def del_data(num):
    spot_data = []
    dict_data = []
    num_id = str(search.num)
    for txt in data['report']:
        spot_data = txt["ID"], txt['TV channel'], txt["date"], txt["time"], txt["programme"], txt["rating"], txt['ads']
        dict_data.append(spot_data)
    for txt in data['report']:
        if txt["ID"] == num_id:
            dict_data['report']["ID":num_id]["ads"] = "False"
    return dict_data



with open("C:/GB/Python/homework/lesson08/advertising.json", "w", encoding="utf-8") as file:
    json.dump(add_new_ads())



