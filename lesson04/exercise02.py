dig_sp = [18, 434, 2, 17, 434, 5, 16, 55, 55, 16]

def not_rep (sp):
    not_rep_sp = []
    i = 0
    while i < len(sp):
        if sp[i] not in not_rep_sp:
            not_rep_sp.append(sp[i])
        i += 1
    return not_rep_sp
    
print(not_rep(dig_sp))


