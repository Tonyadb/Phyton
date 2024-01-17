# #ESERCIZIO 1
# def doppio(val):
#     return val*2

# num_in = float(input("Dammi un numero: "))
# print(f"Il doppio di {num_in} è {doppio(num_in)}") 


# #ESERCIZIO 2
# def somma(val: int) -> int:
#     i = 0
#     somma = 0
#     while i<=(val):
#         somma += i
#         i += 1
#     return somma

# num_in = int(input("Dammi un numero intero: "))
# print("La somma dei valori da 1 a %d è %d" % (num_in, somma(num_in)))


# #ESERCIZIO 4
# def is_prime(val: int) ->bool:
#     k = 2
#     primo = True
#     for k in range(2,val):
#         if val%k == 0:
#             primo = False
#             break
#         k +=1
#     return primo


# num = int(input("Dammi un numero intero:"))
# if is_prime(num):
#     print(f"Il numero {num} è primo")
# else:
#     print(f"Il numero {num} non è primo")


#ESERCIZIO 5 - no giusto rifare
# #Funzione che data una lista in ingresso la divide in due
# def dividi(vec: list) -> tuple[list, list]:
#     l1 = list()
#     l2 = list()
    
#     if len(vec)%2 == 0:
#         n = len(vec)/2
#     else:
#         n = int(len(vec)/2) + 1
    
#     i=0
#     for i in range(n): #farlo con whilw i < n/2 
#         l1.append(vec[i])
#         l2.append(vec[n+i])

#     return l1,l2



a,b = dividi([1,2,3,4,5,6,7])
print(a,b)