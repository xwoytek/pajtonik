from wolekamklass1 import user

class uczen(user):
    def __init__(self,klasa,ulubionalekcja,wzrost,nauczaniedomowe):
        self.klasa = klasa
        self.ulubionaleckja = ulubionalekcja
        self.wzrost = wzrost
        self.nauczaniedomowe = nauczaniedomowe
    


    def pokaklasa(self):
        print(self.klasa)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.klasa = str(input('jaka nowa klasa'))
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass
    def pokaulubionalekcja(self):
        print(self.ulubionaleckja)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.password = str(input('jaka ulubiona lekcja'))
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass
    def pokawzrost(self):
        print(self.wzrost)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.ip = float(input('jaki nowy wzrost'))
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass
    def pokanauczaniedomowe(self):
        print(self.nauczaniedomowe)
        inp = input('zmienic? ')
        if inp == 'Tak':
            inp2 = input('ma nauczanie domowe czy nie')
            if inp2 == 'tak':
                self.nauczaniedomowe = True
            if inp2 == 'nie':
                self.nauczaniedomowe = False
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass