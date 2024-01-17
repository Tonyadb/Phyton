#ESERCIZIO DECORATORI
#Devo definire un decoratore che va ad operare sull'operatore print ma senza modificare in maniera permanente la funzione print stessa che comunque deve 
#continuare a funzionare come prima
#Quando facciamo un decoratore? Noi abbiamo delle funzioni già fatte che usano altre funzioni e ci accorgiamo che vogliamo modificare il comportamento di 
#una funzione solo in quel caso, quindi non possiamo cambiare il comportamento generale della funzione che vogliamo cambiare dato che può essere usata anche da altre parti.
#Senza modificare la funzione per nulla possiamo con una riga di codice, chiamando il decoratore, cambiarne il funzionamento e commentando quella riga tornare a
#far funzionare tutto come prima nel caso non volessimo più il cambiamento. Questo è utile perchè non si deve ntervenire direttamente nel punto dove si vuole la modifica 
#cambiando il codice


def print_decorator(func):
    def wrapper(*args):
        global print
        #vogliamo modificare il comportamento della print quindi ci definiamo una nuova print che prima di ogni argomento 
        #da printare stampi anche un certo carattere che vogliamo
        #se non metto il global print non potrei fare la dichiarazione della funzione globale, starei semplicemente definendo una funzione locale print che però
        #non va ad influenzare la print globale
        old_print = print
        def print(*args):
            old_print("----Marchesini-----", end="")
            old_print(*args)
        
        ret = func(*args)
        #dobbiamo riportare prima di uscire la print alla versione originale cosi che ogni funzione che la chiama e non ha il descrittore riesca ad usare il comportamento originario
        print = old_print
        return ret
    return wrapper

@print_decorator
def myfunc1():
    print("my func1 a")
    print("my func1 b")


def myfunc2():
   print("my func2 a")
   print("my func2 b")  

myfunc1()
myfunc2()

# # altri esempi
# a = 12
# def myfun():
#     a = 32
#     def myfun2():
#         nonlocal a #il nome a in questo modo lo vado a cercare nell'ultimo spazio non-globale che trovo quindi lo spazio che contiene myfun2. Non lo cerco nel globale
#         a = 12

#     myfun2()
#     print(a)

# myfun()


#FIBONACCI 
# La funzione ritorna:
#0 se n=0
#1, se n=1
#F(n-1)+F(n-2) altrimenti

#decoratore per la funzione che permetta di fare la memorizzazione-> se la chiamata è stata già eseguita non devo rifare tutta la funzione ma prendo i valori già 
#calcolati in corrispondenza di questo input
#mettere un contatore globale dentro la fun fibonacci che ci dica quante volte viene chiamata la funzione-> se facciamo F(5) in questo modo viene chiamata 5 volte
cnt = 0

def fibonacci_decorator(func):
    results = [None] * 51 #non serve il global perchè vado a modificare quello a cui punta la lista che è un oggetto modificabile
    def wrapper(args):

        if results[args] is None:
            results[args] = func(args) #così ho che l'indice è il valore di chiamata della funzione fibonacci e il valore è il risultato
        
        return results[args]
    return wrapper


@fibonacci_decorator
def Fibonacci(num: int) -> int:
    global cnt
    cnt += 1
    if num <= 1:
        return num
    else:
        return Fibonacci(num-1) + Fibonacci(num-2)
    


print(Fibonacci(5))
print(cnt)







