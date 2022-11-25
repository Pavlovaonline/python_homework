import json

with open("C:/GB/Python/homework/lesson08/advertising.json", "r", encoding="utf-8") as file:
    data = json.load(file)

def booked ():
    for txt in data['report']:
        if txt["ads"] == "True":
            return txt['TV channel'], ':', txt["date"], ':', txt["programme"], ':', txt['rating']
    

def vacancy ():
    vacancy = []
    for txt in data['report']:
        if txt["ads"] == "False":
            vacancy.append(txt['TV channel'], ':', txt["date"], ':', txt["programme"], ':', txt['rating'])
    return vacancy

def rating ():
    sum = 0
    for txt in data['report']:
        if txt["ads"] == "True":
            sum += float(txt['rating'])
            return sum 
print(rating())