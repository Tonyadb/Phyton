import statistics

# Esercizio 1
def media(num: list) -> float:
    sum = 0
    for i in range(len(num)):
        sum += num[i]
    return sum / len(num)

# Soluzione in classe
def media_v2(a):
    return sum(a) / len(a)

def media_v3(a):
    return statistics.mean(a)

def media_v4(a : list):
    sum = 0
    for e in a:
        sum += e
    return sum/len(a)

# Soluzione personale
def varianza(num: list) -> float:
    sum = 0
    mean = media(num)
    for i in range(len(num)):
        sum += (num[i] - mean) ** 2
    return sum / len(num)

# Soluzione in classe
def varianza_v2(a : list):
    return statistics.pvariance(a)

def varianza_v3(a : list):
    sum = 0
    mean = media(a)
    for e in a:
        sum += (mean - e) ** 2
    return sum / len(a)


a = [1, 2, 3, 4, 5]

print(f'La media è {media(a)}')
print(f'La varianza è {varianza(a)}')