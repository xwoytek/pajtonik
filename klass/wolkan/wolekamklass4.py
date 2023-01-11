from wolekamklass1 import user
class nauczyciel(user):
    def __init__(self,admin,kwalifikacje,czegouczy,wychowawca):
        self.admin = admin
        self.kwalifikacje = kwalifikacje
        self.czegouczy = czegouczy
        self.wychowawca = wychowawca
    
    def pokaadmin(self):
        print(self.admin)
        inp = input('zmienic? ')
        if inp == 'Tak':
            inp2 = input('admin czy nie')
            if inp2 == 'tak':
                self.admin = True
            if inp2 == 'nie':
                self.admin = False
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass
    def pokakwalifikacje(self):
        print(self.kwalifikacje)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.kwalifikacje = str(input('jakie kwalifikacje'))
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass
    def pokaczegouczy(self):
        print(self.czegouczy)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.czegouczy = str(input('Czego uczy'))
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass
    def pokawychowawca(self):
        print(self.wychowawca)
        inp = input('zmienic? ')
        if inp == 'Tak':
            inp2 = input('wychowawca czy nie')
            if inp2 == 'tak':
                self.wychowawca = True
            if inp2 == 'nie':
                self.wychowawca = False
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass