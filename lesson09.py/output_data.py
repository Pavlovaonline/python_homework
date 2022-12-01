import json
import bot

with open("C:/GB/Python/homework/lesson09/data_bot.json", "r", encoding="utf-8") as file:
    data = json.load(file)["report"]

def read_contact (name):
    if name in data["Name"]:
        return data.get("Number")
