class Vector:
    #definiamo i Dunder methods per la classe -> si possono cercare online cosi da trovarli tutti quelli esistenti
    def __init__(self, *args):
        #dentro al vettore ci sarà una lista quindi possiamo costruire con una sequenza di parametri che saranno dentro al vettore.
        #Possiamo anche verificare che questi parametri siano float
        self.__data = list(args) #se non mettessi list() ma solo args avrei una tupla
        for x in self.__data:
            if not isinstance(x, float):
                raise TypeError
            
#self.__data è un attributo privato quindi andiamo a definirne le properties
    def __len__(self):
        return len(self.__data)

    def __str__(self):
        return str(self.__data)

    def __repr__(self): #rappresentazione per uso interno. Ad esempio quello che vedo durante l'esecuzione nella finestra di visualizzazione variabili
        return f'Vector({self.__data})'.replace('[', '').replace(']', '') #tiro via le parentesi quadre dalla rappresentazione della lista
    


    def __getitem__(self, key): #getitem viene chiamata quando uso l'operatore parentesi per accedere all'elemento di un vettore, key è l'indice dell'elemento 
                                  #a cui si vuole accedere
                                  #noi qui passiamo un intero ma inrealtà a getitem la chiave che si passa può essere qualsiasi cosa, ad esempio anche una stringa se ad esempio al posto che la 
                                  #classe vettore stessimo definendo un dizionario
        #print(type(key))
        if isinstance(key, int):
            return self.__data[key]
        elif isinstance(key, slice):
            return Vector(*self.__data[key]) #questo per avere dalla get ancora un vettore degli elementi selezionati e non una lista.
                                            #in questo caso se passassi a Vector "self.__data[key]" avrei che questa è una lista che sto passando a vector. Vector nella sua __init__ però vuole dei parametri singoli e non
                                            #una lista di parametri quindi metto l'asterisco: *self.__data[key]
        #Cos'è l'asterisco? Non è il puntatore del C!!!!! Finora l'abbiamo usato per passare più parametri ad una funzione. Quindi *args diventa una lista con tutti i parametri
        #che noi passiamo alla funzione. In questo caso con la __getitem__ vogliamo fare il contrario ovvero prendere una lista di parametri e spacchettarli. Si fa esattamente
        #utilizzando lo stesso asterisco davanti alla lista di cose. Quindi tutte le volte che si ha una lista di parametri, sia per riceverla che per scompattarla usiamo l'asterisco
        # OSS: Avevamo visto anche l' "**" usato con i dizionari, può prendere il dizionario e lo trasforma in una lista di chiave-valore o viceversa.


    
    def __setitem__(self, key, val): #questo metodo implementabile per assegnare qualcosa
        self.__data[key] = val #key diventa una slice ovvero una terna di parametri; che cosa significa dipende dalla classe che si sta usando

class Example: 
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __getitem__(self, key):
        #per come facicio la get faccio funzionare la classe Error come un dizionario
        if key == 'first':
            return self.first
        elif key == 'second':
            return self.second
        else:
            raise TypeError
    
if __name__ == '__main__':
    v = Vector(3.0,6.0,9.0)
    print(v)
    print(len(v))
    v = Vector(3.0, 6.0, 9.0, -1.2, 3.115)
    print(v)
    print(len(v))
    print(v[2])
    print(v[2:4])  #2:4 fa si che la key diventi una slice: una terna di parametri 
    #quando accedo ad un elemento di un vector mi deve ritornare il contenuto (float in questo caso); quando chiedo di avere gli elementi [2:3] mi aspetto 
    #che ritorni un sottovettore. In questo caso se guardiamo il type(v[2:3]) torna una lista. Ma io voglio un vettore. Allora quando facciamo lo slicing in questo caso io vorrei
    #una copia del vettore selezionato, non una lista. Allora in getitem vado a guardare se ho una slice come key di ingresso o solo un parametro

    for i in range(len(v)):
        print(v[i])

    #in python però non si usa molto il for con gli indici ma con gli elementi!!!!
    for x in v: #se noi abbiamo la __getitem__ e la __len__ automaticamente vengono utilizzati quando chiediamo di accedere agli elementi. Se non avessimo avuto la getitem vediamo cosa succede
                     #facendo un'altra classe di esempio  -> class Example
        print(x)

    e = Example("ciao", 32)
    for x in e: #se non gli costruiamo dei metodi ci dice se proviamo ad eseguire cosi che l'oggetto non è iterabile (is not iterable) 
                #iter e next sono i due dunder metod che bisogna realizzare!!!
        print(x)
    
    #faccio ora la __getitem__ anche per la classe di esempio; anche in questo caso non ci fa iterare su l'oggetto example. Non riesce a scorrere oggetti che abbiano nella
    #__getitem__ qualcosa di diverso da valori nu,erici. Per questo per la classe Vector siamo riusciti ad iterare anche senza aver implementato i metodi iter e next

#--------------------ITERATORI-------------------
    #Gli iteratori consentono di attraversare un contenitore che a questo punto viene chiamato Iterable, un oggetto iterabile. L'iteratore consente di scorrere il contenitore
    #separando la posizione corrente dal contenitore. 
    #Gli iteratori:
    #restituiscono un dato alla volta del contenitore
    #tengono traccia dell'indice del dato dato

    # __iter__ è usato per creare l'oggetto iteratore; la __next__ è fatta per iterare e quindi chiamare elementi successivi. L'oggetto iteratore di solito 
    #restituisce se stesso, self; il metodo next invece deve gestire l'iterazione in base al tipo di contenitore (se è una lista, un dizionario ecc). Quando l'iterazione
    #si deve fermare __next__ deve sollevare l'eccezione StopIteration per interrompere l'iterazione

    #L'iteratore può restituire i dati cosi come sono oppure possono fare delle operazioni per ritornare gli elementi trasformati, l'ultimo tipo di iteratore invece è
    #definito Generatore.

#Proviamo a fare un iteratore per il nostro oggetto!! -> Nuovo file python
         