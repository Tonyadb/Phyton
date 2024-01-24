#gli oggetti sono elementi del linguaggio che tengono insieme i dati e le operazioni che si possono fare su quei dati.

#come si fanno classi in python? class nome_classe : e poi si inseriscono sotto indentate tutte le cose
#come si costruisce un oggetto? nome_oggetto = nome_classe()

#i metodi sono funzioni definiti all'interno della classe. Una differenza col c++ è che quando definizmo una classe non è obbligatorio definire gli attributi della classe
#ogni oggetto python è moificabile in modo dinamico; ogni oggetto python ha assoiato un dizionario di cose che appartengono a quell'oggetto. 
#un oggetto "Person" ad esempio, non è detto che abbia le stesse cose di un altro oggetto "Person". 
#Ogni oggetto ha dentro un dizionario con i suoi campi, possiamo dinamicamente mentre eseguiamo aggiungere volendo altri campi che altri oggetti della stessa classe non avevano.
#Gli attributi non vengono assegnati nella classe, il modo standard che si fa è aggungerli durante la costruzione.
#Creo l'oggetto e poi durante la costruzione aggiungo i campi (che poi non vieta di aggiungerne di altri dopo che si è finito di costruire)

#quando creiamo un oggetto viene invocato il metodo init invocando il "self" che è l'oggetto stesso; è l'analogo del "this" in c++. Qui self va semple esplicato.
# Nella  __init__ quando viene creato l'oggetto ne vengono aggiunti gli attributi. 
#Un altro metodo molto importante è il metodo __str__ che viene chiamato ogni volta che trasformiamo l'oggetto in stringa (ad esempio ogni volta
#che si chiama il print sull'oggetto)

#non esistono il pubblico o il privato. I metodi possono aggiungere altri campi, così come anche da fuori si possono aggiungere altri campi.
#Metodi speciali o dumper sono quei metodi che corrispondono agli operatori del linguaggio. Tutti gli operatori sono ridefinibili per quella classe.
#una delle caratteristiche degli oggetti python è poter creare delle collezioni di oggetti, normalmente non serve, ma nel caso si può fare e si può 
#ridefinire il metodo __len__ in questo caso, che normalmente ci a la lungehzza di una lista di elementi
#Quando usiamo le parentesi quadre viene chiamata la funzione __getitem__

from __future__ import annotations #questo mi serve per specificare con la freccetta di ce tipo è l'oggetto di ritorno della funzione __init__
                                   #posso comunque tranquillamente ometterlo

import copy

class Vector: 
    #creo il costruttore
    # def __init__(self, x: float, y: float) -> Vector:
    #     self.x = x
    #     self.y = y

    def __init__(self, *args) -> Vector:
        ##mia versione
        # if isinstance(args[0], Vector):
        #     self.x = args[0].x
        #     self.y = args[0].y
        # elif (isinstance(args[0], int) or isinstance(args[0], float))  and (isinstance(args[1], int) or isinstance(args[1], float)):
        #     self.x = args[0]
        #     self.y = args[1]

        ##versione prof prima di fare il metodo copy
        if len(args) == 1 and isinstance(args[0], Vector):
            self.x = args[0].x
            self.y = args[0].y
        elif len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        else:
            raise TypeError
        
    def copy(self) -> Vector:
        ret = Vector(self.x, self.y)
        return ret
    #in python non è cosi importante avere un copy constructor perchè in python il default non è copiare! La copia non c'è mai di default, deve essere sempre esplicita
    #se gli oggetti sono complessi e dentro hanno tanti parametri, questa copia diventa un pacco, diventa onerosa per un oggetto complesso.
    #In quest'ultimo caso può essere utile usare la libreria copy fatta apposta per fare le copie di oggetti



    #questo add non è commutativo però nel senso che se io faccio vec + 2 funziona ma se faccio 2 + v1 no allora per far ciò si 
    #implementa __radd__ ovvero il "self" è a destra della somma
    #quando definiamo la add viene implementato anche il += che però ha un difetto
    def __add__(self, other: Vector|int|float) -> Vector:
        # if isinstance(other,Vector):
        #una volta definita la __iadd_ per il += potrebbe essere comodo definire la add con il +=
            # x = self.x + other.x
            # y = self.y + other.y
            # return Vector(x,y)    
        # elif isinstance(other, int) or isinstance(other, float) :
            # x = self.x + other
            # y = self.y + other
            # return Vector(x,y)  
        # else: 
        #     return NotImplemented #il NotImplemented genera l'eccezione al di fuori della classe quando proviamo ad implementarla

        # ret = Vector(self.x, self.y) #riga che può essere sostituita inserendo un metodo copy
        # ret = self.copy()  #questa riga andava prima di imortare la libreria copy!!
        #uso la libreria:
        ret = copy.copy(self)
        ret += other #LA DIFFERENZIAZIONE DELL'ISTANZA DI RIFERIMENTO LA FACCIAMO NELL __iadd__ QUINDI NON SERVE PIU METTERLE QUI
        return ret
        
    
    def __radd__(self, other: int|float) -> Vector:
        if isinstance(other, int) or isinstance(other, float) :
            x = self.x + other
            y = self.y + other
            return Vector(x,y)  
        else: 
            return NotImplemented
        
    def __iadd__(self, other: Vector|int|float) -> Vector:
        if isinstance(other,Vector):
            self.x = self.x + other.x  #questo si poteva fare anche mettendo il += qui dentro
            self.y = self.y + other.y
            return self    
        elif isinstance(other, int) or isinstance(other, float) :
            self.x = self.x + other
            self.y = self.y + other
            return self 
        else: 
            return NotImplemented #il NotImplemented genera l'eccezione al di fuori della classe quando proviamo ad implementarla
    

    #definisco una visualizzazione del vettore sotto forma di stringa
    def __str__(self):
        return f'({self.x:.3f}, {self.y}), id = {id(self)}' #con i :.3f possiamo assegnare la precisione con il quale vogliamo visualizzare il parametro (così è 3 cifre dopo la virgola)

    #si usa quando vogliamo vedere la variabile nell'editor durante l'esecuzione, con una rappresentazione più chiara.
    #Se commentiamo questa funzione possiamo vedere la differenza di rappresentazione del vettore nelal finestrella laterale
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'




if __name__ == '__main__': #metto questo cosi che se voglio importare la classe vector in un altro file tutto questo dentro al main non viene considerato
    a = {'uno': [1,2,3], 'due': [6,5,4]} 
    b = a.copy() 
    #facendo la copia in questo modo creo un dizionario separato però i valori [1,2,3] e [6,5,4] sono gli stessi elementi puntati
    #quindi con append vado a modificare la lista originaria.
    b['uno'].append(8)
    print(a)
    #quindi quello che serve a noi è quest'altro metodo-> deepcopy
    c = copy.deepcopy(a)
    c['uno'].append(9) #con la deepcopy il valore 9 non viene aggiunto
    print(a)

    v1 = Vector(5.3, 6.2)
    v2 = Vector(-3.11, 4.22)
    v3 = Vector(v1)

    print(v3)
    v = v1 + v2 #definiamo la somma tra vettori altrimenti non abbiamo questo operatore
    print(v)

    v = v1 + 2
    print(v)

    v = 2 + v1
    print(v)


    v += 2         #in realtà non sono andato a riscrivere v. 
                   #Se nella stampa aggiungiamo anche l'id dell'oggetto (ovvero un identificatore univoco tra gli oggetti che esistono simultaneamente)
                   #printando anche l'id vediamo che ho creato un altro oggetto
                   #il += su un oggetto modificabile mi crea un nuovo oggetto
                   #quando ci serve il += che modifica il vettore stesso, anche solo per efficienza, l'elemento in coda possiamo aggiungerlo con __iadd__
            
    print(v)  

    v += v1
    print(v)  
 



#costruttire che accetta x, y oppure un altro vettore? modifichiamo il costruttore cosi che se gli passo un altro vettore gli faccio una copia
    #mi serve un costruttore a parametri variabili perchè deve poter prendere un vettore oppure x,y


 #OSS: nel caso si debba lavorare con i soldi o in qualsiasi contesto in cui vogliamo mantenere una rappresentazione in base 10 e non 2 si usa il dato "decimals", l'unica è che è molto più lento
    