class Example: 
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def begin(self):
        return ExampleIterator(self)
    
    def __iter__(self):
        return ExampleIterator(self)
        

    def __getitem__(self, key):
        #per come facicio la get faccio funzionare la classe Error come un dizionario
        if key == 'first':
            return self.first
        elif key == 'second':
            return self.second
        else:
            raise TypeError

class ExampleIterator:
    def __init__(self, example):
        self.__example = example
        self.__pos = 0

    def __iter__(self):
        return self
    
    def __next__(self): #mi deve dare l'elemento del nostro dizionario Example in base a cosa gli passiamo
        self.__pos += 1
        if self.__pos == 0:
            return self.__example.first
        elif self.__pos == 1:
            return self.__example.second
        else:
            raise StopIteration
        

if __name__ == '__main__':

    e = Example("ciao", 32)
#fatto l'iteratore il fatto che si chiami ExampleIterator non lo lega in nessun modo alla classe Example. Quindi questo non basta!!!
    #per usare l'Example iterator dobbiamo usarlo proprio praticamente nel for
    # ei = ExampleIterator(e)
    ei = iter(e)
    for x in e:           
        print(x)
    #la prima cosa che il for chiama su un oggetto è __iter__ che ritorna l'iteratore stesso, seconda cosa chiama la next che ritorna quindi il primo elemento; successivamente chiama di nuovo la next che restituisce il 
    #secondo elemento poi siamo arrivati quindi si ha StopIteration
        
    #C'è un modo per collegare insieme example ed ExampleIterator? Potrei mettere alla C++ un metodo begin che restituisce l'iteratore:
    # ei2 = e.begin()
    #Ma in python c'è una funzione apposta per chiamare la funzione iteratore della mia classe, non serve il begin!! -> iter()
    #ei = iter(e)
    #se chiamo la iter su un ogetto che non ha la __iter__ implementata, python ritorna l'iterator obgject standard che ha la next ch eritorna il prossimo elemento 
    #ottenuto con le parentesi quadre che comunque sulla nostra classe non funzionerebbe
    #dobbiamo quindi definire la funzione __iter__ nella clasee Example se vogliamo scorrerla! In questo caso non serve quindi più definire ei = iter(e) ma il for
    #come prima cosa chiamerà __iter__ su quell'oggetto ovvero su Example. é utile però mantenere il metodo __iter__ anche nell'iteratore stesso
    # oltre che averlo inserito nella classe Exampli. Cosi se non voglio scorrere la classe tutta in una volta (per il quale posso usare: for x in e) ma voglio
    # scorrere il contenitore  fino ad un certo punto poi fermarmi fare delle operazioni e poi ripartire mi serve utilizzare "for x in ei"
    #in un for successivo, ei ripartirà dall'iterazione a cui si era fermato        
    
    # Esempio: lo facciamo con una lista che forse è più chiaro
    lst = [3,5,-1,7,8,9]
    #voglio scorrere tutti gli elementi della lista fino al primo negativo e stampalo poi stampa tutti i successivi cambiati di segno 
    neg = 0
    for x in lst:
        if neg == 1:
            print(-x)
        if x < 0 and neg == 0:
            print(x) 
            neg = 1
    
    xi = iter(lst)
    for x in xi:
        if x < 0:
            print(x)   
            break
    for x in xi:
        print(-x)  
    
    #L'iteratore quindi tiene in memoria l'elemento a cui si era arrivato. L'iteratore è lo stato corrente dell'iterazione, quindi mi interessa tirere fuori l'iteratore
    #quando mi serve tenere in memoria il punto di arrivo dell'iterazione. Questo quindi spiega perchè anche l'iteratore stesso deve mantenere il metodo __iter__ al suo interno
        
    #Con gli iteratori se voglio scorrere una lista e tirarne fuori il quadrato dei valori posso fare il quadratom quindi la trasformazione, sul momento stesso. Non 
    #mi serve crearmi prima una lista copia con i quadrati per poi scorrere questa; posso farmi restituire direttamente i quadrati mentre scorro!!!!!
    #Il vantaggio è che così non dobbiamo memorizzare in memoria tutti i dati modificati prima dell'iterazione.
    
    #Un altro modo per usare un iteratore è generare dei dati; ad esempio range è un iteratore che genera dei dati senza memorizzarli in memoria.
    #In questo caso non ci sarà una __getitem__ perchè non accedo agli elementi in sequenza ma ci sarà solo un __item__ o un __next__    
