import unittest
import teoria_sui_test

class TestSomma(unittest.TestCase):
    def test_interi(self):
        self.assertEqual(teoria_sui_test.somma(3,5),8)
    
    def test_none(self):
        self.assertEqual(teoria_sui_test.somma(3,None))


if __name__ == '__main__':
    unittest.main() #questo si occupa di eseguire i test



#test fixtures sono la parte che serve per preparare l'esecuzione dei test. Quando ci sono operazioni complesse da fare ogni volta, non c'è bisogna di farli per ogni test
#la parte comune di preparazione si può mettere a parte:

# class Test(unittest.TestCase):
#     @classmethod ##definisce che quello è un metodo di classe -> in C++ si chiamano "static"
#     def setUpClass(cls) -> None:    #questo metodo viene chiamato prima di di tutti i test da eseguire e qui dentro ci vanno contenute le operazioni da ripetere per tutte
#         return super().setUpClass()
    
#     @classmethod
#     def tearDownClass(cls) -> None:      #alla fine dell'esecuzione di tutti i metodi si chiama quest'altro metodo alla fine di tutto
#         return super().tearDownClass()