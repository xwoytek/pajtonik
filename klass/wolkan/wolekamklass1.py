class user:
    def __init__(self,id,password,ip,pracownik_szkoly):
        self.id = id
        self.password = password
        self.ip = ip
        self.pracownik_szkoly = pracownik_szkoly
    
    def pokaid(self):
        print(self.id)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.id = int(input('jakie nowe id'))
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass
    def pokapassword(self):
        print(self.password)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.password = int(input('jakie nowe haslo'))
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass
    def pokaip(self):
        print(self.ip)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.ip = int(input('jakie nowe ip'))
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass
    def pokapracownik(self):
        print(self.pracownik_szkoly)
        inp = input('zmienic? ')
        if inp == 'Tak':
            inp2 = input('pracownik czy nie')
            if inp2 == 'tak':
                self.pracownik_szkoly = True
            if inp2 == 'nie':
                self.pracownik_szkoly = False
        if inp == 'nie':
            print('ok nic nie zmieniam')
        else:
            pass