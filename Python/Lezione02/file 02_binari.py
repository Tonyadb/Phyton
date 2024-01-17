#FILE BINARI
#per aprire il file binario bisogna mettere come metodo di apertura "rb"
f = open('/home/ute/Scrivania/Python/Lezione02/prova.txt', 'rb') 
a = f.read()
print(a) #si vedrà davanti alla stampa del contenuto una "b" che ci fa capire che quella che vediamo non è una stringa ma una sequenza di caratteri
#  se facessimo type(a) avremmo " class 'bytes" e a[0] = 99 che corrisponde alla c e NON È UNA STRINGA! Non si possono concatenare stringhe a byte
# quindi non si può fare a += 'x'
#Come facciamo a rappresentare una stringa in byte? 'x'.encode() . Se non si specifica nulla codifica la x in utf-8 altrimenti si può secificare tra le parentesi un'altra codifica

#Sia per le stringhe che per i byte non esiste il metodo .append perchè sono IMMUTABILI. Per le stringhe possiamo fare il +=

#Possiamo prendere una sequenza di byte e decodificarla in una stringa:
b = b'\xc3\xa8'
# b.decode() per decodificare in stringa!!!
print(b.decode())

#per gli interi invece si può avere:
c = int.from_bytes(b'\x05\x01\x00\x00', 'little') #'little' è l'ordine con cui vanno decodificati questi binari!
print(c)

