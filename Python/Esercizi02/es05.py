# Esercizio 5
import time

def nodup_ord(a : list) -> list:
    return list(set(a))                 # I set sono insiemi matematici implementati tramite hashtable. Questo li rende molto più efficienti perchè la complessità
                                        # della funzione è N + il costo per costruire un set.

a = [4,1,1,4,7,9,7]

#start = time.clock_gettime_ns(time.CLOCK_PROCESS_CPUTIME_ID)
start = time.time()
print(f'La lista senza ripetizioni e ordinata di {a} è {nodup_ord(a)}')
stop = time.time()
#stop = time.clock_gettime_ns(time.CLOCK_PROCESS_CPUTIME_ID)

print(f'La funzione nodup() ha impiegato {stop-start} ns per eseguirsi')

# indexing e slicing funzionano anche sulle stringhe. Si possono ricercare elementi o sottostringhe in una stringa.
# s = """ciao mamma 
#        come stai? io sto bene"""
# s.split() -> ritorna una lista di stringhe divise dai whitespace
# s.split("i") -> in questo caso divido la stringa in lista di sottostringhe divise dal carattere "i"
# .join() -> posso inserire in una posizione della stringa un certo valore
# .strip() -> elimina gli spazi iniziali e finali