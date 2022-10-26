sp1 = [2, 3, 4, 5, 6]
sp2 = [2, 3, 5, 6]

def multiplication_in_pairs (sp):
    i = 0
    n = 0
    final_mass = []
    try:
        for int in range(1, len(sp)-1):
            if len(sp) > 1:
                n = sp[i]*sp[(len(sp) - 1)]
                final_mass.append(n)
                sp.pop(i)
                sp.pop(len(sp) - 1)
            elif len(sp) == 1:
                n = sp[i]*sp[i]
                final_mass.append(n)
        return final_mass
    except: ("Что-то пошло не так")

print(multiplication_in_pairs(sp1))
print(multiplication_in_pairs(sp2))