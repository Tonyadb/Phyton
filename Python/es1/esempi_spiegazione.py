def saluta(nome: str):
    print("ciao", nome.title()) #se non suggerisco il tipo nell'input, quando metto il punto dopo "nome" nel print non mi escono i suggerimenti dell'editor sulle funzioni che 
                              #è possibile richiamare, perchè non sa che cos'è. Se invece suggerisco il tipo allora l'editor me lo riconosce come stringa
saluta("giovanni")




def foo(*args):
    for arg in args: #il for ci permette di scorrere degli elenchi e quindi anche le tuple
        print(type(args))
    for arg in args:
        print((args))
    pass

foo('a', 5, True, None) 
        #Quando facciamo *args viene creata una tupla di oggetti
        #qui se andiamo col debug ci dice che questo è una class tuple -> quindi un elenco di oggetti non modificabili
        #siccome è una lista di oggetti non è necessario che siano dello stesso tipo



        

