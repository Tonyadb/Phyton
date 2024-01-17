import math

def dividi(ls: list) -> tuple[list, list]:
    ls1 = []
    ls2 = []
    for i in range(len(ls)):
        if i+1 <= math.ceil((len(ls)/2)):
            ls1.append(ls[i])
        else:
            ls2.append(ls[i])
    return ls1, ls2

# Soluzione in classe 
def dividi_class(ls: list) -> tuple[list, list]:
    first = []
    second = []
    n = len(ls)
    i = 0
    while i < n /2:
        first.append(ls[i])
        i += 1
    while i < n:
        second.append(ls[i])
        i += 1
    return first, second

a, b = dividi([1,2,3,4,5,6,7])
print(a, b) # [1,2,3,4] [5,6,7]

a, b = dividi([1,2,3,5,6,7])
print(a, b) # [1,2,3] [5,6,7]

# In python esiste anche lo slicing per le liste (es. numbers[0:3], si ottiene una lista dal primo indice incluso fino al quarto elemento escluso).
# [:] questo tipo di slicing mi permette di fare una copia di una lista senza usare il metodo copy che si ferma al primo livello di copia (es. lista di liste di liste).
# a[::-1] estrae tutti gli elementi ma con step negativo e quindi produce una lista che è il reverse di quella di partenza.
# a.extend([4, 5]) -> metodo che estende la dimensione della lista e aggiunge gli elementi dell'oggetto iterabile specificato nella chiamata a funzione.
# In alternativa si può usare l'operatore + che fa la concatenazione di liste.
# L'operatore * produrrà una lista in cui si ripetono gli elementi tanto quanto specificato dall'intero dopo l'operatore.
# Per avere una copia ricorsiva con il metodo copy() ho bisogno di usare il metodo copy.deepcopy() sulla lista da copiare.
# non_tuple = (1) -> questa non è una tupla perchè l'interprete non ha modo di differenziarla da una espressione matematica.
# tuple = (1, ) -> questo è il modo di definire una tupla con un solo elemento.
# In python è possibile assegnare un valore ad '_' e in questo modo si specifica che quel valore di ritorno non mi interessa (e non sono utilizzati dal codice).