# num_of_gueses = 1
# secret = "1234"

# #Read in user's guess
# user_guess = input("Please enter password: ")

# while user_guess != secret and num_of_gueses < 5:
#     print("Incorrect. ")
#     user_guess = input("Please enter password: ")
#     num_of_gueses +=1

# if user_guess == secret:
#     print("Correct")
# else:
#     print("Incorrect. Game over.")

# ESERCIZIO 1
num_in = input("Dammi un numero: ")
# print("Il doppio di", float(num_in), "è", float(num_in)*2 )
doppio = float(num_in)*2
# print("Il doppio di %f è %f" % (float(num_in), doppio))
print("Il doppio di {0} è {1}".format(float(num_in), doppio)) #questo è il modo più efficace nel caso si debba tradurre lo script in un altro linguaggio
# print(f"Il doppio di {float(num_in)} è {doppio}") //questa modalità è comoda quando si scrive ma è rischioso se lo script deve essere dato in pasto a dei traduttori


#ESERCIZIO 2
num_in = int(input("Dammi un numero intero: "))
i = 0
somma = 0
while i<=(num_in):
    somma += i
    i += 1
print("La somma dei valori da 1 a %d è %d" % (num_in, somma))

#ESERCIZIO 3
import math
print("Dammi due numeri interi m e n")
m = int(input("m:"))
n = int(input("n:"))
MCD = math.gcd(m,n)
print(f"Il massimo comune divisore è {MCD}")

#ESERCIZIO 4
num = int(input("Dammi un numero intero:"))
k = 2
primo = 1

for k in range(2,num):
    if num%k == 0:
        primo = False
        break
    k +=1

if primo:
    print(f"Il numero {num} è primo")
else:
    print(f"Il numero {num} non è primo")









