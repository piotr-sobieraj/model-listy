del element, lista


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
    
    
    def __str__(self):
        lista_wyj = "["
        tmp_adres = self.glowa
        
        while tmp_adres is not None:
            lista_wyj += str(tmp_adres.dane)            

            tmp_adres = tmp_adres.nastepny
            if tmp_adres is not None: #dodanie przecinka i spacji, ale nie dla osatniego elementu
                lista_wyj += ", "
                      
        lista_wyj += "]"
        return lista_wyj    
    
    
    def szukaj(self, pElement):
        tmp_nastepny = self.glowa
                
        while tmp_nastepny is not None:
            tmp_dane = tmp_nastepny.dane

            if tmp_dane == pElement:
                print (f'Znaleziono {pElement}!')
                return True
                
            tmp_nastepny = tmp_nastepny.nastepny
            
        if tmp_nastepny is None:
            print(f'Nie znaleziono {pElement} wśród elementów podanej listy.') 
            return False 
            
    
    def dolacz(self, pNowyElement):
        nowy_element = element(pNowyElement)
        
        if self.glowa is None: #pusta lista
            self.glowa = nowy_element
            self.ogon = nowy_element
        else:
            self.ogon.nastepny = nowy_element
            self.ogon = nowy_element
            
        self.dlugosc += 1