#ESERCIZIO 1
def doppio(val):
    return val*2

num_in = float(input("Dammi un numero: "))
print(f"Il doppio di {num_in} è {doppio(num_in)}") 


#ESERCIZIO 2
def somma(val: int) -> int:
    i = 0
    somma = 0
    while i<=(val):
        somma += i
        i += 1
    return somma

num_in = int(input("Dammi un numero intero: "))
print("La somma dei valori da 1 a %d è %d" % (num_in, somma(num_in)))


#ESERCIZIO 4
def is_prime(val: int) ->bool:
    k = 2
    primo = True
    for k in range(2,val):
        if val%k == 0:
            primo = False
            break
        k +=1
    return primo


num = int(input("Dammi un numero intero:"))
if is_prime(num):
    print(f"Il numero {num} è primo")
else:
    print(f"Il numero {num} non è primo")