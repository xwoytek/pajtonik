from random import randint,choice
from time import sleep
class gracz:
    def __init__(self,imie : str,hp : int,gold : int,exp : int,damage : int,maxhp : int,damagefinal : int,killcount:int) -> None:
        self.basicdata()
        self.imie = imie
        self.hp = hp
        self.maxhp = maxhp
        self.runy = runyy(0,0,0,0,0,0)
        self.gold = gold
        self.exp = exp
        self.damage = damage
        self.damagefinal = damagefinal
        self.killcount = killcount
    def hypy(self):
        self.maxhp = self.runy.runahp*10 + 100

    def basicdata(self):
        self.imie = str(input('Witaj przybyszu, jak cię zwą? '))
        self.hp = 100
        self.maxhp = 100
        self.gold = 0
        self.exp = 0
        self.damage = 10
        self.kalkulujdamage()
        self.killcount = 0
    def kalkulujdamage(self):
        self.damagefinal = abs(self.damage + randint(-10,10))

class runyy:
    def __init__(self,runaognia:int,runawody:int,runaziemi:int,runapowietrza:int,runaataku:int,runahp:int) -> None:
        self.runaognia = runaognia
        self.runawody = runawody
        self.runaziemi = runaziemi
        self.runapowietrza = runapowietrza
        self.runaataku = runaataku
        self.runahp = runahp

class przeciwnik:
    def __init__(self,hp:int,dmg:int,imieprzeciwnik:str) -> None:
        self.hp = hp
        self.dmg = dmg
        self.imieprzeciwnik = imieprzeciwnik
        self.slaboscii = slabosci(False,False,False,False)
        self.basicdata()
    def basicdata(self):
        self.hp = randint(1,100)
        self.dmg = randint(1,10)
    

class slabosci:
    def __init__(self,slaboscognia : bool,slaboscwody : bool,slaboscpowietrza : bool,slaboscziemi : bool) -> None:
        self.slaboscognia = slaboscognia
        self.slaboscwody = slaboscwody
        self.slaboscpowietrza = slaboscpowietrza
        self.slaboscziemi = slaboscziemi

class krasnal:
    def __init__(self) -> None:
        self.przeciwnik = przeciwnik(0,0,'')
        self.przeciwnik.imieprzeciwnik = 'Krasnal'
        self.przeciwnik.slaboscii.slaboscognia = True
        self.przeciwnik.slaboscii.slaboscwody = False
        self.przeciwnik.slaboscii.slaboscpowietrza = True
        self.przeciwnik.slaboscii.slaboscziemi = False        

class goblin:
    def __init__(self) -> None:
        self.przeciwnik = przeciwnik(0,0,'')
        self.przeciwnik.imieprzeciwnik = 'Goblin'
        self.przeciwnik.slaboscii.slaboscognia = True
        self.przeciwnik.slaboscii.slaboscwody = True
        self.przeciwnik.slaboscii.slaboscpowietrza = False
        self.przeciwnik.slaboscii.slaboscziemi = False

class nimfa:
    def __init__(self) -> None:
        self.przeciwnik = przeciwnik(0,0,'')
        self.przeciwnik.imieprzeciwnik = 'Nimfa'
        self.przeciwnik.slaboscii.slaboscognia = False
        self.przeciwnik.slaboscii.slaboscwody = False
        self.przeciwnik.slaboscii.slaboscpowietrza = False
        self.przeciwnik.slaboscii.slaboscziemi = True
        
class rycerz:
    def __init__(self) -> None:
        self.przeciwnik = przeciwnik(0,0,'')
        self.przeciwnik.imieprzeciwnik = 'Rycerz'
        self.przeciwnik.slaboscii.slaboscognia = True
        self.przeciwnik.slaboscii.slaboscwody = True
        self.przeciwnik.slaboscii.slaboscpowietrza = False
        self.przeciwnik.slaboscii.slaboscziemi = True

        

class olbrzym:
    def __init__(self) -> None:
        self.przeciwnik = przeciwnik(0,0,'')
        self.przeciwnik.imieprzeciwnik = 'Olbrzym'
        self.przeciwnik.slaboscii.slaboscognia = False
        self.przeciwnik.slaboscii.slaboscwody = False
        self.przeciwnik.slaboscii.slaboscpowietrza = False
        self.przeciwnik.slaboscii.slaboscziemi = False
        

class sklep:
    def __init__(self) -> None:
        self.gracz = gracz('',100,0,0,10,100,0,0)
    def rundawsklepie(self):
        self.gracz.gold += randint(1,100)
        cenarunyognia = 10
        cenarunywody = 10
        cenarunypowietrza = 10
        cenarunyziemi = 10
        cenarunyataku = 20
        cenarunyzdrowia = 15
        czynnosc = ''
        while czynnosc != 'e':
            print('Witaj w sklepie podróżniku co chcesz zrobić?')
            print('r - przeglądaj runy, e - wyjdz')
            czynnosc = input('')
            if czynnosc == 'r':
                print(f'co chcesz kupić podróżniku? masz {self.gracz.gold} złota')
                print('1 - runa ognia 2 - runa wody 3 - runa powietrza 4 - runa ziemi 5 - runa ataku 6 - runa zdrowia')
                runydozobaczenia = int(input(''))
                if runydozobaczenia == 1:
                    print(f'Jedna runa kosztuje {cenarunyognia} monet')
                    ilosc = int(input("Ile chcesz towaru? "))
                    if self.gracz.gold >= ilosc*cenarunyognia:
                        self.gracz.gold -= ilosc*cenarunyognia
                        self.gracz.runy.runaognia += ilosc
                        print('Miło się z tobą robi interesy podróżniku \n')
                    else:
                        print('https://drive.google.com/file/d/1oGzoZKCFQO-00JSjNQu2uYWuzzVuBcvn/view?usp=sharing'*29)
                        exit()
                if runydozobaczenia == 2:
                    print(f'Jedna runa kosztuje {cenarunywody} monet')
                    ilosc = int(input("Ile chcesz towaru? "))
                    if self.gracz.gold >= ilosc*cenarunywody:
                        self.gracz.gold -= ilosc*cenarunywody
                        self.gracz.runy.runawody += ilosc
                        print('Miło się z tobą robi interesy podróżniku \n')
                    else:
                        print('https://drive.google.com/file/d/1oGzoZKCFQO-00JSjNQu2uYWuzzVuBcvn/view?usp=sharing'*29)
                        exit()
                if runydozobaczenia == 3:
                    print(f'Jedna runa kosztuje {cenarunypowietrza} monet')
                    ilosc = int(input("Ile chcesz towaru? "))
                    if self.gracz.gold >= ilosc*cenarunypowietrza:
                        self.gracz.gold -= ilosc*cenarunypowietrza
                        self.gracz.runy.runapowietrza += ilosc
                        print('Miło się z tobą robi interesy podróżniku \n')
                    else:
                        print('https://drive.google.com/file/d/1oGzoZKCFQO-00JSjNQu2uYWuzzVuBcvn/view?usp=sharing'*29)
                        exit()
                if runydozobaczenia == 4:
                    print(f'Jedna runa kosztuje {cenarunyziemi} monet')
                    ilosc = int(input("Ile chcesz towaru? "))
                    if self.gracz.gold >= ilosc*cenarunyziemi:
                        self.gracz.gold -= ilosc*cenarunyziemi
                        self.gracz.runy.runaziemi += ilosc
                        print('Miło się z tobą robi interesy podróżniku \n')
                    else:
                        print('https://drive.google.com/file/d/1oGzoZKCFQO-00JSjNQu2uYWuzzVuBcvn/view?usp=sharing'*29)
                        exit()
                if runydozobaczenia == 5:
                    print(f'Jedna runa kosztuje {cenarunyataku} monet')
                    ilosc = int(input("Ile chcesz towaru? "))
                    if self.gracz.gold >= ilosc*cenarunyataku:
                        self.gracz.gold -= ilosc*cenarunyataku
                        self.gracz.runy.runaataku += ilosc
                        print('Miło się z tobą robi interesy podróżniku \n')
                    else:
                        print('https://drive.google.com/file/d/1oGzoZKCFQO-00JSjNQu2uYWuzzVuBcvn/view?usp=sharing'*29)
                        exit()
                if runydozobaczenia == 6:
                    print(f'Jedna runa kosztuje {cenarunyzdrowia} monet')
                    ilosc = int(input("Ile chcesz towaru? "))
                    if self.gracz.gold >= ilosc*cenarunyzdrowia:
                        self.gracz.gold -= ilosc*cenarunyzdrowia
                        self.gracz.runy.runahp += ilosc
                        print('Miło się z tobą robi interesy podróżniku \n')
                    else:
                        print('https://drive.google.com/file/d/1oGzoZKCFQO-00JSjNQu2uYWuzzVuBcvn/view?usp=sharing'*29)
                        exit()
                else:
                    print('Jesteś głupi czy głupi \n')
            if czynnosc == 'e':
                break
            else:
                print('eeeee co? \n')

class currentenemy:
    def __init__(self) -> None:
        self.przeciwnicy = [krasnal(),goblin(),nimfa(),rycerz(),olbrzym()]
        self.przeciwniktera = (choice(self.przeciwnicy))
        self.przeciwnikstaty = przeciwnik(0,0,'')
    def losojprzeciwnik(self):
        self.przeciwniktera = choice(self.przeciwnicy)
        self.przeciwnikstaty.basicdata()
    def koniec(self):
        if 'krasnal' in str(self.przeciwniktera):
            return 10+len('krasnal')
        if 'goblin' in str(self.przeciwniktera):
            return 10+len('goblin')
        if 'nimfa' in str(self.przeciwniktera):
            return 10+len('nimfa')
        if 'rycerz' in str(self.przeciwniktera):
            return 10+len('rycerz')
        if 'olbrzym' in str(self.przeciwniktera):
            return 10+len('olbrzym')
    def jakipokemon(self):
        if 'krasnal' in str(self.przeciwniktera):
            self.przeciwnikstaty.imieprzeciwnik = 'Krasnal'
            self.przeciwnikstaty.slaboscii.slaboscognia = True
            self.przeciwnikstaty.slaboscii.slaboscwody = False
            self.przeciwnikstaty.slaboscii.slaboscpowietrza = False
            self.przeciwnikstaty.slaboscii.slaboscziemi = False
        if 'goblin' in str(self.przeciwniktera):
            self.przeciwnikstaty.imieprzeciwnik = 'Goblin'
            self.przeciwnikstaty.slaboscii.slaboscognia = True
            self.przeciwnikstaty.slaboscii.slaboscwody = True
            self.przeciwnikstaty.slaboscii.slaboscpowietrza = False
            self.przeciwnikstaty.slaboscii.slaboscziemi = False
        if 'nimfa' in str(self.przeciwniktera):
            self.przeciwnikstaty.imieprzeciwnik = 'Nimfa'
            self.przeciwnikstaty.slaboscii.slaboscognia = False
            self.przeciwnikstaty.slaboscii.slaboscwody = False
            self.przeciwnikstaty.slaboscii.slaboscpowietrza = False
            self.przeciwnikstaty.slaboscii.slaboscziemi = True
        if 'rycerz' in str(self.przeciwniktera):
            self.przeciwnikstaty.imieprzeciwnik = 'Rycerz'
            self.przeciwnikstaty.slaboscii.slaboscognia = True
            self.przeciwnikstaty.slaboscii.slaboscwody = True
            self.przeciwnikstaty.slaboscii.slaboscpowietrza = False
            self.przeciwnikstaty.slaboscii.slaboscziemi = True
        if 'olbrzym' in str(self.przeciwniktera):
            self.przeciwnikstaty.imieprzeciwnik = 'Olbrzym'
            self.przeciwnikstaty.slaboscii.slaboscognia = False
            self.przeciwnikstaty.slaboscii.slaboscwody = False
            self.przeciwnikstaty.slaboscii.slaboscpowietrza = False
            self.przeciwnikstaty.slaboscii.slaboscziemi = False

class bitka:
    def __init__(self) -> None:
        self.gracz = gracz('',100,0,0,10,100,0,0)
        self.enemy = currentenemy()
        self.shop = sklep()
        
    def ruda(self):
        self.gracz.hypy()
        sleep(3)
        print(f'Walczyz z {str(self.enemy.przeciwniktera)[10:self.enemy.koniec()]}')
        sleep(3)
        print(f'On ma {self.enemy.przeciwnikstaty.hp} hp i zadaje {self.enemy.przeciwnikstaty.dmg} punktów zdrowia')
        sleep(3)
        print(f'Ty masz {self.gracz.hp}/{self.gracz.maxhp} hp i zadajesz {self.gracz.damage} hp')
        sleep(3)
        print('CO ROBISZ????!???!??!!?!?!?!?!?!?!?!?!?!?!?!?!?')
        sleep(3)
        print('a - atak, l - leczymy się, w - uciekamy, e - stoimy nic nie robimy i czekamy na śmierć')
        inp = input()
        sleep(3)
        if inp == 'a':
            self.gracz.kalkulujdamage()
            print(f'atakujesz {str(self.enemy.przeciwniktera)[10:self.enemy.koniec()]} za {self.gracz.damagefinal} hp')
            sleep(2)
            if self.gracz.runy.runaognia < 0 and self.enemy.przeciwnikstaty.slaboscii.slaboscognia == True:
                self.enemy.przeciwnikstaty.hp -= self.gracz.damagefinal + self.gracz.runy.runaognia*10 + self.gracz.runy.runaataku*2
                print(f'Atak SUPEREFEKTYWNY finalny damage to {abs(self.gracz.damagefinal + self.gracz.runy.runaognia*10 + self.gracz.runy.runaataku*2)} hp')
                sleep(2)
            if self.gracz.runy.runawody < 0 and self.enemy.przeciwnikstaty.slaboscii.slaboscwody == True:
                self.enemy.przeciwnikstaty.hp -= self.gracz.damagefinal + self.gracz.runy.runawody*10 + self.gracz.runy.runaataku*2
                print(f'Atak SUPEREFEKTYWNY finalny damage to {abs(self.gracz.damagefinal + self.gracz.runy.runawody*10 + self.gracz.runy.runaataku*2)} hp')
                sleep(2)
            if self.gracz.runy.runapowietrza < 0 and self.enemy.przeciwnikstaty.slaboscii.slaboscpowietrza == True:
                self.enemy.przeciwnikstaty.hp -= self.gracz.damagefinal + self.gracz.runy.runapowietrza*10 + self.gracz.runy.runaataku*2
                print(f'Atak SUPEREFEKTYWNY finalny damage to {abs(self.gracz.damagefinal + self.gracz.runy.runapowietrza*10 + self.gracz.runy.runaataku*2)} hp')
                sleep(2)
            if self.gracz.runy.runaziemi < 0 and self.enemy.przeciwnikstaty.slaboscii.slaboscziemi == True:
                self.enemy.przeciwnikstaty.hp -= self.gracz.damagefinal + self.gracz.runy.runaziemi*10 + self.gracz.runy.runaataku*2
                print(f'Atak SUPEREFEKTYWNY finalny damage to {abs(self.gracz.damagefinal + self.gracz.runy.runaziemi*10 + self.gracz.runy.runaataku*2)} hp')
                sleep(2)
            else:
                self.enemy.przeciwnikstaty.hp -= self.gracz.damagefinal + self.gracz.runy.runaataku*2
                print(f'Atak NIEEFEKTYWNY finalny damage to {abs(self.gracz.damagefinal + self.gracz.runy.runaataku*2)} hp')
                sleep(2)
            if self.enemy.przeciwnikstaty.hp <= 0:
                los = randint(1,1)
                if los == 1:
                    print(f'\nGRATULACJE ZABIŁEŚ {str(self.enemy.przeciwniktera)[10:self.enemy.koniec()]} teraz nadciąga kolejny przeciwnik uważaj na siebie')
                    self.gracz.killcount += 1
                    self.shop.rundawsklepie()
                    self.enemy.losojprzeciwnik()
                    self.ruda()
                else:
                    print(f'\nGRATULACJE ZABIŁEŚ {str(self.enemy.przeciwniktera)[10:self.enemy.koniec()]} teraz nadciąga kolejny przeciwnik uważaj na siebie')
                    self.gracz.killcount += 1
                    self.enemy.losojprzeciwnik()
                    self.ruda()
            else:
                sleep(1)
                demedz = 0
                demedz = abs(self.enemy.przeciwnikstaty.dmg + randint(-10,10))
                self.gracz.hp -= demedz
                print(f'O NIE przeciwnik teraz ciebie atakuje przeciwnik i zadaje {demedz}')
                if self.gracz.hp < 0:
                    print('https://drive.google.com/file/d/10VleoghoIasBFFJCI836n7PloeMiWynK/view?usp=sharing'*21)
                else:
                    self.ruda()
        if inp == "l":
            losowanko  = randint(1,2)
            if losowanko == 2:
                self.gracz.hp += randint(1,50)
                print('Uleczono')
                if self.gracz.hp > self.gracz.maxhp:
                    self.gracz.hp = self.gracz.maxhp + 1 - 1
                self.ruda()
            else:
                print('nie udało się uleczyć')
                self.ruda()
        if inp == 'w':
            losoj = randint(1,10**100)
            if losoj == 55757:
                print('wow uciekłeś \n')
                self.enemy.losojprzeciwnik()
                self.ruda()
            else:
                print('https://drive.google.com/file/d/10VleoghoIasBFFJCI836n7PloeMiWynK/view?usp=sharing'*21)
        if inp == 'e':
            print('https://drive.google.com/file/d/10VleoghoIasBFFJCI836n7PloeMiWynK/view?usp=sharing'*21)
abhfughf = bitka().ruda()
abhfughf