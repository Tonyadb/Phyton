# Esercizio 3
def potenze(base: float, maxesp: int) -> list:
    pow = []
    for i in range(1, maxesp+1):
        pow.append(base**i)
    return pow

# Soluzioni in classe
def potenze_v2(base: float, maxesp: int) -> list:
    pow = []
    for i in range(1, maxesp+1):
        pow.extend([base**i])
    return pow

def potenze_v3(base: float, maxesp: int) -> list:
    pow = []
    for i in range(1, maxesp+1):
        pow += [base**i]
    return pow

a = 2
b = 5
print(f'Le potenze con base {a} e maxesp {b} sono {potenze(a, b)}')
    