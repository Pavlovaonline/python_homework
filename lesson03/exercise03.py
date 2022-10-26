import math
from fractions import Fraction
from decimal import Decimal

sp = [1.1, 1.2, 3.1, 5, 10.01]
def dif_frac (sp):
    i = 0
    n = 0
    h = ""
    mass = []
    try:
        for i in range(0, len(sp)-1):
            n = (sp[i]) - math.trunc(sp[i])
            mass.append(n)
        n = (max(mass)) - (min(mass))
        print(mass)
        return n
    except:("Что-то пошло не так")

print(dif_frac(sp))
