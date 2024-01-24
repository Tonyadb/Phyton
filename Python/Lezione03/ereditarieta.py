# una classe può ereditare le funzionalità da un'altra classe. 
#Quando chiamo la init della mia classe all'interno devo chiamare a sua volta la init della classe da cui sto prendendo le proprietà

#In python abbiamo l'ereditarietà multipla ovvero costruire una classe che acquisisce le proprietà di più classi contemporaneamente
#Quando si usa l'ereditarietà multima abbiamo delle classi che aggiungono delle proprietà, vengono chiamate anche interfacce, forniscono diversi modi per utilizzare quella classe

#Non esiste l'overloading degli operatori, non possiamo fare due versioni della stessa funzione ma comportamenti diversi; bisgona comunque fare una sola funzione.
#Se sto prendendo gli attributi da più classi ed una funzione è definita in piu di una di queste, quando chiamo quel metodo farò riferimento alla funzione definita nella
#classe che viene prima in ordine, l'ordine che definisco quando definisco la mia classe come ereditabile di altre

#Qui ha senso introdurre il concetto di attributi privati. Per leggerli o settarli uso get o set.
#Gli attributi nn pubblici sono quelli che non devono essere usati dagli altri, è il funzionamento interno della classe. 
#Per definire un attributo come non pubblico bisogna mettere il doppio underscore davanti. Esempio: self.__age = age dentr la funzione di __init
#con gli attributi non pubblici faccio due metodi, uno per impostare, l'altro per leggere gli attributi. Non è possibile andare a richiamare 
# classe.__age ad esempio in un print -> non possiamo fare print(classe.__age)





#con una @property possiamo cambiare uno specifico attributo sostituendolo con una sua stessa versione resa anche privata.
#se vogliamo che un attributo venga modificato solo da chi eredita ci mettiamo un underscore solo davanti. Quindi quando vediamo un parametro definito in questo modo
#non va usato al di fuori nel programma ma non ci sono modi per obbligarlo a non usarlo.