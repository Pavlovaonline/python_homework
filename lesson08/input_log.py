# import json
# import user_interface

# with open("C:/GB/Python/homework/lesson08/advertising.json", "r", encoding="utf-8") as file:
#     data = json.load(file)

# def add_new_ads (num):
#     num = user_interface.input_text()
#     for txt in data['report']:
#         if txt["ID"] == num:
#             if txt["ads"] == "True":
#                 return "Этот выход уже занят"
#             if txt["ads"] == "False":
#                 change_data(num)

# new_data = {}
# a = "0002"
# def change_data(num):
#     place_data = []
#     dict_data = []
#     for txt in data['report']:
#         place_data = txt["ID"], txt['TV channel'], txt["date"], txt["time"], txt["programme"], txt["rating"], txt['ads']
#         dict_data.append(place_data)
#     for txt in data['report']:
#         if txt["ID"] == num:
#             dict_data["ads"] = "True"
#     return dict_data


# with open("C:/GB/Python/homework/lesson08/advertising.json", "w", encoding="utf-8") as file:
#     json.dump(change_data())



