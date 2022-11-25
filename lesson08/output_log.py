import json

with open("C:/GB/Python/homework/lesson08/advertising.json", "r", encoding="utf-8") as file:
    data = json.load(file)

def booked ():
    place_booked = []
    dict_booked = []
    count = 0
    for txt in data['report']:
        if txt["ads"] == "True":
            place_booked = txt['TV channel'], ':', txt["date"], ':', txt["time"], ':', txt["programme"], ':', txt['rating']
            count += 1
        dict_booked.append(place_booked)
    return count, dict_booked
    

def vacancy ():
    place_vacancy = []
    dict_vacancy = []
    count = 0
    for txt in data['report']:
        if txt["ads"] == "False":
            place_vacancy = txt['TV channel'], ':', txt["date"], ':', txt["time"], ':', txt["programme"], ':', txt['rating']
            count += 1
            dict_vacancy.append(place_vacancy)
    return count, dict_vacancy

def rating ():
    sum = 0
    for txt in data['report']:
        if txt["ads"] == "True":
            sum += float(txt['rating'])
    return sum 
