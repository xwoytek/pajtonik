from wolekamklass1 import user
class rodzic(user):
    def __init__(self,czyj,wktorejklasiedziecko,zawod,mapieniondze):
        self.czyj = czyj
        self.wktorejklasiedziecko = wktorejklasiedziecko
        self.zawod = zawod
        self.mapieniondze = mapieniondze
    
    def pokaczyj(self):
        print(self.czyj)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.czyj = str(input('jakie nowe dziecko'))
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass
    def pokawktorejklasiedziecko(self):
        print(self.wktorejklasiedziecko)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.wktorejklasiedziecko = str(input('w ktorej klasie jest dziecko'))
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass
    def pokazawod(self):
        print(self.zawod)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.zawod = str(input('jaki nowy zawod'))
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass
    def pokamapieniondze(self):
        print(self.mapieniondze)
        inp = input('zmienic? ')
        if inp == 'Tak':
            inp2 = input('ma pieniądze czy nie')
            if inp2 == 'tak':
                self.mapieniondze = True
            if inp2 == 'nie':
                self.mapieniondze = False
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass