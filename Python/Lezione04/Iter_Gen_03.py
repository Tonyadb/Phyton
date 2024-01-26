
class FibonacciGen:
    def __init__(self, stop = 10):
        self.stop = stop
        self.prev = 0
        self.curr = 1
        self.pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos < self.stop:
            self.pos += 1
            ret = self.prev
            self.curr, self.prev = self.prev + self.curr, self.curr #in questo modo riesco a generare la serie di fibonacci senza ricorrere alla ricorsione
            return ret
        else:
            raise StopIteration


for i in FibonacciGen(10):
    print(i)



#posso anche scrivere un generatore implementando una funzione
def FibonacciGenerator():
    prev = 0
    curr = 1

    while True:
        ret = prev
        curr, prev = prev + curr, curr
        # return ret #se mettessi return ogni volta avrei sempre 0 in output e quindi chiamando la funzione ricorsivamente non ho la serie di fibonacci ma sempre 0
        yield ret #questo ci permette di far si che la funzione quando viene richiamata riparte da questo punto e quindi continua a ciclare nel while!!!
                #se avessi altre righe di codice dopo yield quando rientro nella funzione riparto ed eseguirò quelle prima di ripartire con il while

    
for i in FibonacciGenerator:
    print(i)

#se scrivessi:
    # while True:
    #     print(FibonacciGenerator())
#non funzionerebbe perchè non sto chiamando l'iteratore ma semplicemente creando una nuova funzione FibonacciGenerator


#DEFINIZIONE DI UNA FUNZIONE INLINE -> con i "lambda" 

f = lambda x : x + 1
print(f(2))

items = [2,4,6,7]
sqr = list(map(lambda x: x**2, items)) #map applica la funzione lambda su tutti gli items della lista: quindi verranno iterati gli elementi e per ognuno applicata la funzioen
#possiamo considerare la map come un generatore

# filter  -> filtra gli elementi da un elenco secondo l'esito di una funzione
numb_list = [-5, 5]
min_than_zero = list(filter(lambda x : x<0, numb_list)) #se l'elemento di numb_list è minore di zero  viene aggiunto alla lista di output


from functools import reduce # permette di ridurre una sequenza secondo dei valori specificati
product = reduce((lambda x, y : x*y), [1, 2, 3, 4])


    





    
