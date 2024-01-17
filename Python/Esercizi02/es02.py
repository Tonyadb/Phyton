# Esercizio 2
def ribalta(num: list) -> list:
    return num[::-1]

# Soluzioni in classe
def ribalta_v2(a : list) -> list:
    res = []
    for e in a:
        res = [e] + res
    return res

def ribalta_v3(a : list) -> list:
    b = a[:]     # b = a.copy()
    b.reverse()
    return b

a = [1,2,3,4,5]
print(f'La lista ribalta di {a} è {ribalta(a)}')
print(f'La lista ribalta di {a} è {ribalta_v2(a)}')
print(f'La lista ribalta di {a} è {ribalta_v3(a)}')