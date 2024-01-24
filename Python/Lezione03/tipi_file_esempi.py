
#csv.reader è un oggetto che fa il parsing automatico dei file csv; con questo usando next(csv_reader) ci da l'elemento successivo del file. il file csv_reader viene letto a righe
#se ci fosse l'accapo dentro la riga lui farebbe il parsing di testo per dirci che li c'è anche un accapo.
#se mettiamo in un for -> printf(f"Columns name are { ', ' .join(column_data)}") La virgola tra le virgolette è il simbolo utilizzato per separare i cambi printati

#Se volessi leggere gli elementi del file come dizionario, al posto che usare l'oggetto .reader, uso l'oggetto csv.DictReader. Questo prende il file, assume che come prima
#riga ci siano i nomi dei campi. 
#Ogni riga è un dizionario che ha come chiavi i nomi della prima riga letta e possiamo utilizzare i "nomi" delle colonne per accedere all'elemento corrispondente
# Se i nomi gli e li vogliamo dare noi esternamente si può fare con : csv.DictReader(csv_file, fieldnames = listra con stringhe di nomi) -> vedi slide

#csv..DictWriter per scrivere su un file csv a partire da un dizionario; con il metodo .writerow scrivo una riga alla volta nel mio file, con .writerows invece scrivo tutto
#il dizionario in una volta

#posso scrivere anche dei file in versione json -> va importata la libreria json, si apre il dile con open() e poi basta fare il metodo .dump sul file
#Con .dumps si ottiene una stringa da poter manipolare.

import json

data = {
    "corso" : "Python III edizione",
    "docenti": [
        {
            "nome" : "Costantino" , #i docenti sono una lista di dizionari che contengono nome e cognome
            "cognome" : "Grana",
        },
        {
            "nome" : "Federico" ,
            "cognome" : "Bolelli",
        },
    ],
    "numero partecipanti": 9,
    "costo" : None,
    "laboratorio" : True,
}

#Vogliamo scrivere questa struttura su stringa in formato json
s = json.dumps(data)
print(s)

#Scrivere un file json è facile, potevamo farlo anche a mano. Per leggere apro il file in lettura e con .load prendo tutti i dati
# data = json.load(open("data.json", "r"))
#Se le informazioni arrivano sottoforma di stringa si fa "json.loads"

#-------------Pickle
# Non sempre vogliamo leggere da file json. 
# A volte abbiamo degli oggetti complessi: matrici, vettori, tensori ottenuti da librerie. Voglio salvare quegli oggetti li cosi come sono senza aver bisogno di trasformarli.
#In C era una cosa molto complessa da fare.
# python ha la caratteristica di avere la reflection -> gli oggetti possono interrogarsi su come sono fatti, di che tipo è quello che hanno dentro, quali sono i suoi campi e cosi via.
#C'è un modulo apposta per serializzare in formato binario i dati. Il modulo pickle è un formato binario in grado di serializzare qualsiasi oggetto python.
#La cosa può diventare complicata con alcuni oggetti. 
#Ci consente di salvare su disco i dati binari contenuti nell'oggetto e ricaricarli, indipendentemente dall'architettura. Lo scopo di pickle è salvare dati da python a python;
#non è salvare dati che siano poi distribuibili al di fuori di python.
#un difetto di python è che nn è totalmente stabile; in base alla versione che si usa di python qualcosa potrebbe cambiare, anche se negli ultimi anni non l'hanno più
#cambiato.
#pickle funziona uguale al modulo json. Si può fare il .dump dell'oggetto e con la .load ci troviamo gli oggetti ricaricati.
# La differenza è che pickle essendo binario, se abbiamo dei dati numerici di grandi dimensioni non ci occuperà lo stesso spazio che ci occupa il json. Il json non ha il 
# concetto di matrici, dovevamo essere noi a scriverlo con le giuste parentesi, con pickle posso prendere direttamente una matrice e ritorna un oggetto di tipo matrix.
