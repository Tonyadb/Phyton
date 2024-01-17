#ESERCIZIO 1 - OKK FUNZIA A MENO DEI CASI IN CUI HO LA SOMMA DI UN GRUPPO DI ZERI!!
def read_gruppi(filename: str) -> list[int]:
    f = open(filename, 'r') 
    l = []
    somma = 0
    ingroup = False
    for line in f:
        if line is not '\n':
            val = int(line)
            somma += val
        else:
            if somma is not 0:
                l.append(somma)
            somma = 0
    else:
        if somma is not 0:
            l.append(somma)
        
    return l

filename = '/home/ute/Scrivania/Python/Lezione02/file1.txt'
lst = read_gruppi(filename)
# print(lst)


#ESERCIZIO 2
# def read_cities(filename: str) -> list[tuple[str, int]]:
#     f = open(filename, 'rb')
#     a = f.read(4)
#     n = int.from_bytes(b'a', 'little')
#     for

    
#     pass


def read_cities(filename: str) -> list[tuple[str, int]]:
    try:
        with open(filename, 'rb') as f:
            cities = []
            a = f.read(4)
            n_cities = int.from_bytes(a, 'little')
            for i in range(n_cities):
                bcity = bytes()
                while True:
                    c = f.read(1)
                    if c == b'\0' or c == b'': #oppure if len(c)<1 or c == b'0'
                        break
                    bcity += c
                city = bcity.decode()
                bpop = f.read(4)
                if len(bpop) < 4: #check error
                    break
                population = int.from_bytes(bpop, 'little')
                cities.append((city, population)) #doppia parentesi per poter fare append di una tupla
            return cities
                
    except FileNotFoundError:
        return

    




filename = '/home/ute/Scrivania/Python/Lezione02/cities01.bin'
lst = read_cities(filename)