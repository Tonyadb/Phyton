#I set vanno sppecificati utilizzando le parentesi graffe. Sono collezioni di oggetti non ripetuti
#non sono collezioni di oggetti ordinati quindi non si può accedere all'elemento utilizzando la graffa x[0]. Se proprio ho bisogno dell'indexing posso convertire 
#il set in una lista ma ovviamente non c'è poi garanzia sull'ordine
# Aggiungere elemento al set -> set.add()
#Eliminare un elemento dal set -> set.discard() -> la discard non dice nulla, non lancia nessuna eccezione nel caso in cui il valore da eliminare non ci sia dentro al set
#set.remove() da invece un'eccezione se il valore da eliminare non è contenuto nel set

#DIZIONARI
#Sono coppie chiave-valore
#Li definisco con le parentesi graffe {"chiave": "valore", "chiave": "valore"...}. Non posso avere due chiavi uguali nello stesso dizionario, due valori invece si
#dict.get("chiave", "valore opzionale") -> cerco la chiave nel dizionario, se c'è ti restituisco il suo valore altrimenti ritorna il valore opzionale che di default è None
#dict.keys() -> posso estrarre la sequenza di chiavi dal dizionario. dict.keys è un oggetto iterabile che appunto mi permette di iterare sulle chiavi (for k in dict.keys)
#posso anche costruire una copia in una lista delle chiavi l = list(dict.keys()). Se non mi serve avere la lista itero direttamente come scritto prima cosi risparmio memoria
# d.values() stessa cosa del precedente ma con i valori. Contiene tutti i valori ed è iterabile
#d.items() contiene invece la coppia chiave-valore. quindi ottengo una lista di tuole chiave-valore. Posso iterare srotolando la tupla direttamente nel for
# e fare quindi (for k, v in d.items()) così riesco ad avere i due valori slegati

# Non c'è garanzia sull'ordinamento delle cose contenute in un dizionario. Se ci serve qualcosa che di agaranzia di ordinamento c'è la possibilità di utilizzare le collections (ordered dict)
#dict.setdefault("chiave", valore opzionale) -> la setdefault fa la get sul dizionario e se l'elemento non c'è aggiunge dentro al dizionario il valore opzionale voluto
#volendo si può vedere come la versione più compatta di d["ee"] = d.get("ee", "opt") che è più dispendioso perchè si fa l'accesso al dizionario due volte

def dict_invert(d: dict) ->dict:
    d_bis = {}
    for k, v in d.items():
        d_bis[v] = k
    return d_bis


d = {"Theodore": 10, "Mathew" : 11, "Roxanne": 9}
d_res = dict_invert(d)
print(d_res.items())


# from es01 import dict_invert    -> #questo se la funzione fosse stata definita in un altro file es01.py e la volessi importare
                                     #se avessi fatto direttamente import es01 avrei importato e quindi compilato ed eseguito tutto il file 
                                     #invece in questo modo prendo solo la funzione di interesse
                                     #posso rinominare il namespace importato aggiuggendo : import es01 as e
                                     #in questo caso la funzione la posso chiamare come e.dict_invert
                                     #scrivendo invece come fatto a sinistra: from es01 import dict_invert non c'è bisogno di specificare il namespace davanti alla funzione
                                     #si può importare tutte le funzioni contenute ma è pericoloso from es01 import *

def dict_invert_inplace(d:dict) ->dict:
    d_bis = dict_invert(d) #se fosse stato in e01.py avrei dovuto fare d_bis = e01.dict_invert(d)
    
    d.clear()
    d.update(d_bis)  

    return d

print(dict_invert_inplace(d).items())


#questa dicitura mi permette di eseguire parte di un codice di un file solo se quel file viene eseguito come main 
#se il file è importato allora name assume un altro valore e la parte nell'if non viene eseguita

int __name__ == "__main__":
    def dict_invert(d: dict) ->dict:
        d_bis = {}
        for k, v in d.items():
            d_bis[v] = k
        return d_bis


    d = {"Theodore": 10, "Mathew" : 11, "Roxanne": 9}
    d_res = dict_invert(d)
    print(d_res.items())