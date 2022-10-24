a = int(input())
b = int(input())
if a<b:
    min_dig = a
    max_dig = b
elif a>b:
    min_dig = b
    max_dig = a
elif a==b:
    min_dig = a
    max_dig = b
for i in range(2, min_dig):
    if max_dig%i==0:
        print("делим на ", i)
        break