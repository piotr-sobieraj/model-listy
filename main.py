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
    
    
    def __len__(self):
        return self.dlugosc
    
    
    def szukaj(self, pElement):
        tmp_adres = self.glowa
                
        while tmp_adres is not None:
            tmp_dane = tmp_adres.dane

            if tmp_dane == pElement:
#                 print (f'Znaleziono {pElement}!')
                return True
                
            tmp_adres = tmp_adres.nastepny
            
        if tmp_adres is None:
#             print(f'Nie znaleziono {pElement} wśród elementów podanej listy.') 
            return False 
            
    @property
    def dlugosc_iter(self):
        temp_adres = self.glowa
        licznik = 0
                
        if temp_adres is None:
            return licznik
        
        while temp_adres is not None:
            licznik += 1
            temp_adres = temp_adres.nastepny
        
        return licznik
        
        
    
    def dolacz(self, pElement):
        n_element = element(pElement)
        if self.glowa is None:
            self.glowa = n_element
            self.ogon = n_element
            n_element.nastepny = None
        else:
            self.ogon.nastepny = n_element
            self.ogon = n_element            
            
        self.dlugosc += 1
        
    
    def daj_element_o_indeksie(self, pIndex):
        licznik = 0
        
        tmp_adres = self.glowa
        
        while tmp_adres is not None:
            if licznik == pIndex:
                return tmp_adres.dane
            licznik += 1
            
            tmp_adres = tmp_adres.nastepny
        
        raise Exception(f'Indeks {pIndex} poza zakresem!')
        
        
print('Start testów...')
test_lista = lista()
assert len(test_lista) == 0

test_lista.dolacz(1)
assert len(test_lista) == 1

test_lista.dolacz(2)
assert len(test_lista) == 2

test_lista.dolacz(3)
assert len(test_lista) == 3
assert test_lista.dlugosc_iter == 3

assert test_lista.szukaj(10) == False
assert test_lista.szukaj(1) == True
assert test_lista.szukaj(2) == True
assert test_lista.szukaj(3) == True

assert test_lista.daj_element_o_indeksie(1) == 2


print('Testy zakończone pomyślnie :)')