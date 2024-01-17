#LAVORARE CON I FILE 01
#se vogliamo distruggere il file dopo averlo usato possiamo usare il "with"

# with open('/home/ute/Scrivania/Python/Lezione02/prova.txt', 'r') as f:
#     for line in f.readlines():
#         print(line[:-1])

# with open('/home/ute/Scrivania/Python/Lezione02/input1.txt', 'r') as f:
#         print(f.read())
#qui sul primo file da errore per via della codifica del file, per via delle lettere accentate
#le stringhe del file sono sequenze di code point, sono liste di numeri interi da 0 a circa 1 milione.
#Ogni file di testo è una codifica di una sequenza di code point
#la open quando apre un file usa una determinata codifica. Python usa la codifica di default del sistema operativo che si utilizza
#Si può sapere che codifica si sta utilizzando
#si può specificare se si vuole utilizzare un'altra codifica nella sezione 'encoding': è una stringa in cui noi diciamo come è codificato il file

with open('/home/ute/Scrivania/Python/Lezione02/input1.txt', 'r', encoding='latin1') as f: #latin1: un byte per carattere
        print(f.read())

with open('/home/ute/Scrivania/Python/Lezione02/input2.txt', 'r', encoding ='utf-8') as f: #questo daro che riusciamo a vederlo anche senza specificare la codifica sarà sicuramente in utf-8
        print(f.read())

#quindi se il file non è codificato nell encoding di defautl allora va specificata qual'è! 
#La libreria chardet può permetterci di capire in che codifica è scritto un file.
#la libreria non fa altro che provare a decodificare, se c'è un errore allora prova con un'altra codifica e cosi via ma non sempre ci dà la versione corretta
#PEr vedere la codifica di default che si ha sul proprio sistema:
    # import locale
    # print(locale.getpreferredencoding)

#Quindi si può specificare un encoding oppure utilizzare quello di default. 

#In ogni caso il comportamento in caso di errore è configurabile perchè magari a volte a noi non interessa che in qualche punto il decodificatore dia errore
# In questo caso si specifica in una delle opzioni.

#si può usare 'ignore' che ovviamente produce una perdita id dati ma amen; si può anche provare a non generare l'errore ma sostituire con un carattere ecc...
with open('/home/ute/Scrivania/Python/Lezione02/input1.txt', 'r', errors = 'ignore') as f: #latin1: un byte per carattere
        print(f.read())
#Qui aver messo ignore produce l'effetto che le lettere che non si riesce a decodificare non vengono proprio stampate

#con line.strip() si possono eliminare spazi che non si ritengono significativi ad inizio e fine della linea


        
pass