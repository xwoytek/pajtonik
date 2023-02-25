from random import randint
#----------------------------------------Stats
Imie = input("podaj imię swojego bohatera - ")
life = 100
weapon = "drewniany_miecz"
bow = "stary_łuk"
gold = 0
Hp = 0
Dmg = 0
EXP = 0
#-----------------------------------atack
def atack(weapon,bow):
    print("1=normalny atak")
    print("2=strzał z łuku")
    atak = float(input())
    if atak == 1:
        if weapon == "drewniany_miecz":
            return randint(5,10)
        if weapon == "kamienny_miecz":
            return randint(10,15)
        if weapon == "żelazny_miecz":
            return randint(15,20)
        if weapon == "diamentowy_miecz":
            return randint(20,25)
        if weapon == "boski_miecz":
            return randint(35,50)
    if atak == 2:
        if bow == "stary_łuk":
            return randint(0,20)
        if bow == "nowy_łuk":
            return randint(15.50)  
    else:
        print("nie wybrano akcji")
        atack(weapon,bow)
#---------------------------------Sklep
def sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg):
    while EXP >= 100:
        print("zdobyłeś poziom")
        print("na co chcesz przeznaczyć punkt doświadczenia(dana statystyka zwiększy się o 1):1-obrażenia, 2-zdrowie")
        poziom = float(input())
        if poziom == 1:
            Dmg = Dmg+1
        elif poziom == 2:
            Hp = Hp+1
        else:
            print("źle podana liczba")
            sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
        EXP = EXP-100
    print("gdzie chcesz iść:1-sklep z bronią, 2-sklep z zbroją, 3-arena")
    print("masz",gold,"golda ")
    czynnosc = float(input())
    if czynnosc == 1:
        print("co chcesz kupić: 1-miecz, 2-łuk")
        bron = float(input())
        if bron == 1:
            print("1-kamienny miecz(10-15)-40G,2-żelazny miecz(15-20)-100G,3-diamentowy miecz(20-25)-175G,4-boski miecz(35-50)-250G,5-powrót")
            wybor = float(input())
            if wybor == 1:
                if gold >= 40:
                    gold = gold - 40
                    weapon = "kamienny_miecz"
                    print("kupiłeś miecz")
                    sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
                else:
                    print("nie stać cię")
                    sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
            if wybor == 2:
                if gold >= 100:
                    gold = gold - 100
                    weapon = "żelazny_miecz"
                    print("kupiłeś miecz")
                    sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
                else:
                    print("nie stać cię")
                    sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
            if wybor == 3:
                if gold >= 175:
                    gold = gold - 175
                    weapon = "diamentowy_miecz"
                    print("kupiłeś miecz")
                    sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
                else:
                    print("nie stać cię")
                    sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
            if wybor == 4:
                if gold >= 250:
                    gold = gold-250
                    weapon = "boski_miecz"
                    print("kupiłeś miecz")
                    sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
                else:
                    sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
            if wybor == 5:
                sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
            else:
                sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
        if bron == 2:
            print("1-nowy łuk(15-50)-100G,2-powrót")
            wybor1 = float(input())
            if wybor1 == 1:
                if gold >= 100:
                    gold = gold - 100
                    bow == "nowy_łuk"
                    print("kupiłeś łuk")
                    sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
                else:
                    print("nie stać cię")
                    sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
            if wybor == 2:
                sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
            else:
                sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
    if czynnosc == 2:
        print("Zbroje są jednorazowe 1-skórzana zbroja(125HP)-25G,2-żelazna zbroja(150HP)-50G,3-diamentowa zbroja(200HP)-100G,4-powrót")
        wybor2 = float(input())
        if wybor2 == 1:
                if gold >= 25:
                    gold = gold - 25
                    life = 125
                    print("kupiłeś zbroję")
                    sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
                else:
                    print("nie stać cię")
                    sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
        if wybor2 == 2:
                if gold >= 50:
                    gold = gold - 50
                    life = 150
                    print("kupiłeś zbroję")
                    sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
                else:
                    print("nie stać cię")
                    sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
        if wybor2 == 3:
                if gold >= 100:
                    gold = gold - 100
                    life = 200
                    print("kupiłeś zbroję")
                    sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
                else:
                    print("nie stać cię")
                    sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
        if wybor2 == 4:
            sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
        else:
            sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
#-----------------------------------arena
# 0-nazwa, 1-życie, 2-obrażenia, 3-gold, 4-EXP
    if czynnosc == 3:
        liczba_pokonanych_przeciwnikow = 0
        a = 30
        b = 40
        c = 55
        d = 65
        e = 80
        f = 150
        dwarf = ["Krasnalem",a,6,10,15]
        goblin = ["Małym Goblinem",b,8,20,25]
        nymph = ["Nimfą Wodną",c,10,25,35]
        knight = ["Rycerzem",d,12,30,45]
        giant = ["Olbrzymem",e,14,40,50]
        final_boss = ["finałowym bosem",f,18,50,75]
        list_Opponents = [dwarf,goblin,nymph,knight,giant,final_boss]
        x = 0
        life = life+Hp
        while life >= 1:
            Opponent = list_Opponents[x]
            print("-"*40)
            while Opponent[1] > 0:
                print(f"{Imie} walczy teraz z {Opponent[0]}")
                print(f"Przeciwnik ma {Opponent[1]} Hp i zadaje ci {Opponent[2]} obrażeń")
                life = life - Opponent[2]
                if life <= 0:
                    break
                print(f"Zostało ci {life} Hp")
                atak = atack(weapon,bow)+Dmg
                Opponent[1] = Opponent[1] - atak
                print(f"Zadałeś {atak} obrażeń")
                if Opponent[1] <= 0:
                    print("-"*40)
                    print('Zabiłeś przeciwnika')
                    gold = gold+Opponent[3]
                    liczba_pokonanych_przeciwnikow = liczba_pokonanych_przeciwnikow+1
                    x = x+1
                    EXP = EXP+Opponent[4]
            if x > 5:
                print("wygrałeś")
                life = 100
                sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
        print("zginąłeś")
        print("pokonałeś",liczba_pokonanych_przeciwnikow,"przeciwników")
        life = 100
        x = 0
        liczba_pokonanych_przeciwnikow = 0
        sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)
sklep_i_arena(gold,weapon,bow,life,Imie,EXP,Hp,Dmg)