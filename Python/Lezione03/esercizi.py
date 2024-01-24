def extract_number(message: str) -> str:
    num = str()
    val = ''
    mp =  {'zero': '0', 'uno': '1', 'due': '2', 'tre': '3', 'quattro' : '4', 'cinque' : '5', 'sei': '6', 'sette' : '7', 'otto': '8', 'nove': '9'}
    for c in mp:
        idx = message.find(c)
        if idx > 0:
            for l in range(idx, len(message)):    
                if message[l] is not  " ":
                    num += message[l]
                else: 
                    val += mp[num]
                    num = ''
                    break
    return val


def extract_number_01(message: str) -> str:

    if message is  None:
        return None
    
    mp =  {'zero': '0', 'uno': '1', 'due': '2', 'tre': '3', 'quattro' : '4', 'cinque' : '5', 'sei': '6', 'sette' : '7', 'otto': '8', 'nove': '9'}

    words = message.lower().split()
    number = ' '

    # for word in words:
    #     if word in mp:
    #         number += mp.get(word,'')
    
    lst = [mp.get(word,'') for word in words if word in mp]
    return ''.join(lst) 



from itertools import repeat 

def extract_number_02(message: str) -> str:

    if message is  None:
        return None
    
    d =  {'zero': '0', 'uno': '1', 'due': '2', 'tre': '3', 'quattro' : '4', 'cinque' : '5', 'sei': '6', 'sette' : '7', 'otto': '8', 'nove': '9'}

    words = message.lower().split() #lower perchè magari alcune stringhe hanno un carattere maiuscolo ed altre minuscolo quindi le passo tutte in minuscolo
    out = map(d.get, words, repeat('')) #map mi permette di applicare la funzione (primo argomento) su tutti gli oggetti in words. La funzione get
                                        #se non trova una chiave della mappa in words ritorna None oppure il secondo parametro specificato che nel nostro caso è
                                        #uno spazio vuoto '' . Lo spazio vuoto glie lo passo con repeat al posto che passargli uno spazio vuoto per ogni words 
    out = list(out)

    return ''.join(out)

mes = 'dieci poveri negretti se ne andarono a mangiar; unO fece indigestione, Nove ne restar'

c = extract_number_02(mes)
print(c)