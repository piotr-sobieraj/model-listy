class element:
    def __init__(self, pDane, pNastepny=None):
        self.dane = pDane
        self.nastepny = pNastepny
        
    def __repr__(self):
        return f'{self.__dict__}'

    
class lista:
    def __init__(self):
        self.glowa = None
        self.ogon = None
        self.dlugosc = 0
        
    def __repr__(self):
        return f'{self.__dict__}'
    
    def szukaj(self, pElement):
        tmp_nastepny = self.glowa
        tmp_dane = tmp_nastepny.dane
                
        while tmp_nastepny is not None:
            tmp_dane = tmp_nastepny.dane

            if tmp_dane == pElement:
                print(f'Znaleziono {pElement}!')
                return
                
            tmp_nastepny = tmp_nastepny.nastepny
            
        print(f'Nie znaleziono {pElement} wśród elementów podanej listy.')


# Wstawienie i testy
lst = lista()
q = element(3)
lst.glowa = q
lst.ogon = q

r = element(5)
q.nastepny = r
lst.ogon = r


s = element(7)
r.nastepny = s
lst.ogon = s

print(lst)
lst.szukaj(10)
lst.szukaj(3)