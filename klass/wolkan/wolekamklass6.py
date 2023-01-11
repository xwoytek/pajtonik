from wolekamklass4 import nauczyciel

class dyrektor(nauczyciel):
    def __init__(self,iledobrychzmian,ilelatpracuje,opinianauczycieli,czyuczy):
        self.iledobrychzmian = iledobrychzmian
        self.ilelatpracuje = ilelatpracuje
        self.opinianauczycieli = opinianauczycieli
        self.czyuczy = czyuczy

    def pokailedobrychzmian(self):
        print(self.iledobrychzmian)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.iledobrychzmian = int(input('ile'))
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass
    def pokailelatpracuje(self):
        print(self.ilelatpracuje)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.ilelatpracuje = int(input('ile'))
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass
    def pokaopinianauczycieli(self):
        print(self.opinianauczycieli)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.opinianauczycieli = str(input('Jaka jest nowa opinia'))
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass
    def pokaczyuczy(self):
        print(self.czyuczy)
        inp = input('zmienic? ')
        if inp == 'Tak':
            inp2 = input('uczy czy nie')
            if inp2 == 'tak':
                self.czyuczy = True
            if inp2 == 'nie':
                self.czyuczy = False
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass