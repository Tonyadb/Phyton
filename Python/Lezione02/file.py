#LAVORARE CON I FILE

#un file è qualunque stream di dati che riceve il programma
#tipicamente 2 tipologie di file: file di testo e file binari; entrambi sono sequenze di byte, la differenza sostanziale è che i file di testo sono sequenze di code point nel testo, 
#ogni sequenza di code point rappresente un simbolo
#si distingue tra file di testo e binari in python perchè quando apro un file specifico se voglio usarlo come sequenza di byte o sequenza di caratteri. questo è importante perche
#quando leggo da un file binario ottengo un byte mentre quando leggo dal file di testo leggo una stringa
#La funzione per aprire/creare l'oggetto file è la open che prende il nome del file e la modalità di apertura (r = lettura )

f = open('/home/ute/Scrivania/Python/Lezione02/prova.txt', 'r') #creo un oggetto f che posso usare per accedere agli elementi del file
# a = f.read(1) #la read vuole sapere la size, ovvero quanti caratteri leggere, quanti code point leggere
# b = f.read(1)
# c = f.read(1)
# d = f.read(1)
# e = f.read(1)
s = ''
while True:
    c = f.read(1)
    if c == '':
        break
    s += c
#questo è il modo di fare il ciclo ultrabase in C. Quando si lavora con il testo è molto più agevole lavorare per righe.
#Il ciclo leggi tutto si può tradurre in semplicemente s = f.read() -> in questo modo si legge tutto il file, anche gli a capo e le linee vuote


ss = ''
ss = f.read()
# f.close() #la close si usa quando abbiamo un programma che va sempre avanti e si aprono più file contemporaneamente quindi quando finiamo di usarlo lo chiudiamo
#           #se non c'è il close() il file viene chiuso quando si esce dallo scope

# #si può lavorare a linee con il file:
# sss = f.readlines() #qui sss diventa una lista, di cui ogni elemento è una linea del file, l'accapo in fondo non viene visto come una linea vuota

for line in f.readlines():
    print(line)

for line in f.readlines():
    print(line[:-1]) #il meno uno fa qualcosa sugli spazi tipo