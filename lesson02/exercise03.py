first = str(input("Введите текст: "))
second = str(input("Введите слово, которое требуется найти: "))

f = []
s = []
for x in first:
    f.extend(x)
for y in second:
    s.extend(y)
i = 0
word_check = []
num_of_repet = 0
p = 0
while i < len(first):
    if f[i] == s[0]:
        word_check += f[i:i+(len(s)):]
        if word_check == s:
            p+=1
    word_check.clear()
        #num_of_repet = round(len(word_check)//len(s))
    i+=1
print(f"Слово \"{second}\" встречается в тексте {p} раз")