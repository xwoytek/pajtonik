from random import randint
class Uczen():
    def __init__(self, imie, nazwisko, wiek, oceny):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.oceny = oceny

    def ocny(self):
        self.oceny = []
        self.oceny.append(randint(1,6))
        print(self.oceny)

    def przedstawsie(self):
        print(f'jestem {self.imie} {self.nazwisko}')
    
    def sredniaocen(self):
        print(sum(self.oceny)/len(self.oceny))

u1 = Uczen
u2 = Uczen
u3 = Uczen

lista = [u1,u2,u3]