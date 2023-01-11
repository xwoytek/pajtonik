from wolekamklass2 import uczen

class pupilek(uczen):
    def __init__(self,ktogolubi,ilema6,ilerazyzdenerwowalklase,ilesieuczy):
        self.ktogolubi = ktogolubi
        self.ilema6 = ilema6
        self.ilerazyzdenerwowalklase = ilerazyzdenerwowalklase
        self.ilesieuczy = ilesieuczy

    def pokaktogolubi(self):
        print(self.ktogolubi)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.ktogolubi = str(input('KTO'))
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass
    def pokailema6(self):
        print(self.ilema6)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.ilema6 = int(input('ILE'))
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass
    def pokailerazyzdenerwowalklase(self):
        print(self.ilerazyzdenerwowalklase)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.ilerazyzdenerwowalklase = int(input('ILE'))
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass
    def pokailesieuczy(self):
        print(self.ilesieuczy)
        inp = input('zmienic? ')
        if inp == 'Tak':
            inp2 = input('ILE')
            if inp2 == 'tak':
                self.ilesieuczy = True
            if inp2 == 'nie':
                self.ilesieuczy = False
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass