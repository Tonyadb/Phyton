# enumerate :
#quando faccio un for faccio "for x in lista" ad esempio  posso fare for (posititon, title) in enumerate (lista)
#in questo caso enumerate ci torna due elementi: la posizione e il valore corrispondente

lst = ['a', 'x', 'ciao', 'prova']
for x in lst:
    print(x)

#enumerate ritorna delle tuple che hanno come primo elemento la posizione e come secondo il valore della lista (tuple expantion)
# for x in enumerate(lst):
    # print(x)
#se voglio inserire le due informazioni in due variabili diverse posso espandere la tupla e fare:
for i,x in enumerate(lst):
    print(f'{i}: {x}, type={type(x)}')

# enumerate può avere anche due input enumerate(lst, 3) il secondo elemento è la posizione da cui voglio partire se questa non è zero

#------------------zip --------------------- 
# zip crea un nuovo oggetto fatto dall'unione di due o più cose che si vogliono su cui poter iterare. Non contiene in realtà tutti gli elementi ma li scorre uno di seguito all'altro
# x = lista1
# y = lista2
# zipped = zip(x,y)
    
# for a,b in zip(x,y):
#     print(f'{a}, {b}')
#se i due elementi hanno dimensioni diverse e quindi uno dei due ad un certo punto da "stopIteration" si ferma; quindi itera fino alla dimensione del più corto dei due


#------------LIST COMPREHENSION----------------------------------------------------------------------
capitals = ["London", "rome", "Madrid"]
lenght = []

for c in capitals:
    lenght.append(len(c))

#un modo piu furbo di farlo è 
lenght = [len(c) for c in capitals] #-> quindi io scorro capitals e per ogni iterazione aggoiungo l'espressione che ho messo all'inizio, quindi len(C)
#ci va un'espressione di python ma non un comando ad esempio un print o un if. 

#se voglio mettere un if ad esempio fare l'append solo se len(c)<=4

lenght = [len(c) for c in capitals if len(c)<=4] #-> quindi la condizione di inserimento la mettiamo alla fine 

#---------------funzioni built in- ------------------------------
# len(), print(), isinstance() sono funzioni built in. ce ne sono anche altre elencate nelle slide: es. sum, min, max, abs, pow (sostituibile da **), round ecc...
# due funzioni che a volte possono essere utili: all() -> mi dice se di una sequenza gli elementi sono tutti veri, se anche solo 1 è falso da False
                                            #  any() -> mi dice se almeno uno degli elementi è vero da True
#sorted() -> prende in input una sequenza e restituisce una versione ordinata di quella
#con il .sort vado a modificare l'oggetto stesso (è una funzione in place)

#reversed() -> restituisce un iteratore agli elementi dell'oggetto su cui viene evocato, quindi devo per vedere il contenuto convertirlo in
#qualcosa di stampabile list(reversed_number) dove reversed_number = reversed(vall)

#---------------------- ECCEZIONI ------------------------------------------
# Per lanciare un'eccezione basta usare la parola chiave raise Exception('messaggio..') 

#è possibile usare "assert" per verificare se una certa condizione è vera. Per usarla va importata sys
#Ci permette di generare eccezioni del tipo AssertionError   quando l'assezione non è vera
#import sys
#assert ('linux' in sys.platform), "error msg"
#verifico se la stringa linux fa parte della piattaforma su cui sto eseguendo. Utile ad esempio per controllare su che piattaforma 
#sto eseguendo un codice che magari eseguo su macchine diverse

#try:
    # "iterazioni "
#except:
    # " cosa fare nel caso in cui un'eccezione venga catturata". Se si incontra un'eccezione non viene eseguita in quella casistica ma si va nell'except
    #è buona regola non gestire insieme tutte le ecccezioni ma fare qualcosa in base all'errore
    # pass

#per specificare l'eccezione:
#except AssertionError as errore:
   #....

#è anche possibile aggiungere un blocco "else:" dopo il blocco except. Qui si rientra se non si generano eccezioni e viene eseguito correttamente il try:
#un ultimo blocco che si può aggiungere è "finally:" che viene eseguito in tutti i casi sia con eccezioni che non
