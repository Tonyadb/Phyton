#inpython c'è una libreria per fare i test. La più famosa è "unittest"
#alcune regole: i test devono essere metodi di una classe; abbiamo alcuni metodi standard predefiniti che fanno asserzioni-> delle assert 
#questi metodi sono definiti nella classe TestCase. per utilizzarli bisogna creare una classe di test che eredita da TestCase
def somma(a, b):
    if b is None:
        return None
    return a+b

if __name__ == '__main__':
    print(somma(3,5))

#ci vuole una regola per far capire al framework quali sono i test
#la regola è creare un file chiamandolo test_nomefunzione