import time
import random
import functools

# Esercizio 4

def nodup(a : list) -> list:
    ls = []
    for i in range(len(a)):
        if (a[i] not in ls):
            ls.append(a[i])
    return ls

# Soluzioni in classe
def calctime(fun):
    @functools.wraps(fun)
    def wrapper(*args):
        start = time.time()
        ret = fun(*args)                    # L'asterisco sta per fare l'unpacking della tupla di args
        stop = time.time()
        print(f'La funzione {fun.__name__} ha impiegato {stop-start} s')
        return ret
    return wrapper

@calctime                     # Utilizzo del decoratore per chiamare la funzione wrapper definita in calctime. Il decoratore invoca la funzione calctime passandogli la funzione nodup_ord_v1
def nodup_ord_v1(a : list):   # La complessità di questa funzione è N^2
    ret = []
    for e in a:
        if e not in ret:
            ret.append(e)
    return ret

@calctime
def nodup_v1(a : list):   # La complessità di questa funzione è N + N*log(N)
    a = a[:]
    a.sort()                # La funzione è inplace e quindi non ha valore di ritorno
    ret = a[:1]             # Questo non funziona se la lista è vuota quindi devo mettere uno slicing
    for i in range(1, len(a)):
        if a[i] != ret[-1]:
            ret.append(a[i])
    return ret

@functools.cache            # Decoratore per salvare in cache l'esecuzione della funzione (questo è utile per funzioni ricorsive e fare backtracking)-
def nodup_v2(a : list) -> list:
    return list(set(a))                 # I set sono insiemi matematici implementati tramite hashtable. Questo li rende molto più efficienti perchè la complessità
                                        # della funzione è N + il costo per costruire un set.

@calctime
def donothing():
    for i in range(1, 10000):
        pass

a = [4,1,1,4,7,9,7]

#a = []
#for i in range(1, 10000):
#    a.append(random.randint(1, 1000))

#a = range(1, 10000)
#a = list(a)

#start = time.clock_gettime_ns(time.CLOCK_PROCESS_CPUTIME_ID)
#start = time.time()
#print(f'La lista senza ripetizioni e non ordinata di {a} è {nodup_ord_v1(a)}')
#nodup_ord_v1(a)
#stop = time.time()
#stop = time.clock_gettime_ns(time.CLOCK_PROCESS_CPUTIME_ID)
#print(f'La funzione nodup_ord_v1() ha impiegato {stop-start} ns per eseguirsi')

#print(calctime(nodup_ord_v1, a))

#nodup_ord_v1 = calctime(nodup_ord_v1)
nodup_ord_v1(a)

help(nodup_v2)
help(nodup_v1)

#start = time.clock_gettime_ns(time.CLOCK_PROCESS_CPUTIME_ID)
#start = time.time()
#print(f'La lista senza ripetizioni e non ordinata di {a} è {nodup_v1(a)}')
#nodup_v1(a)
#stop = time.time()
#stop = time.clock_gettime_ns(time.CLOCK_PROCESS_CPUTIME_ID)
#print(f'La funzione nodup_v1() ha impiegato {stop-start} ns per eseguirsi')

#print(calctime(nodup_v1, a))

#nodup_v1 = calctime(nodup_v1)
nodup_v1(a)

#start = time.clock_gettime_ns(time.CLOCK_PROCESS_CPUTIME_ID)
#start = time.time()
#print(f'La lista senza ripetizioni e non ordinata di {a} è {nodup_v2(a)}')
#nodup_v2(a)
#stop = time.time()
#stop = time.clock_gettime_ns(time.CLOCK_PROCESS_CPUTIME_ID)
#print(f'La funzione nodup_v2() ha impiegato {stop-start} ns per eseguirsi')

#print(calctime(nodup_v2, a))

#nodup_v2 = calctime(nodup_v2)
nodup_v2(a)


#calctime(donothing)
donothing()