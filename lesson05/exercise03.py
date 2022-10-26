dig_sp = "овывдл абв лваыьб абваб лывывь абва аббв"

def del_abc (st):
    sp = st.split(" ")
    i = 0
    del_abc_sp = []
    while i < len(sp):
        if "абв" not in sp[i]:
            del_abc_sp.append(sp[i])
        i += 1
    return del_abc_sp
    
print(del_abc(dig_sp))

