from random import randint
atakenemy = 0
hpenemy = 0
killcount = 0
leczmale = int(0)
leczsrednie = int(0)
leczduze = int(0)
iloscatak1 = 20 
iloscatak2 = 20 
iloscatak3 = 20 
iloscatak4 = 20 
# POKEMONY--------------------------------------------------------------------------------------------------
    # MOJE POKI
def bulbasaur():
    global name
    global hpmoje
    global atak1
    global atak2
    global atak3
    global atak4
    global mojlevel
    global grafika
    grafika = 'https://drive.google.com/file/d/1g_dYa0hyTkSdnQMMi1v4smUMHEQR3deA/view?usp=sharing'
    name = 'bulbasaur'
    hpmoje = 100
    atak1 = 20
    atak2 = 10
    atak3 = 1
    atak4 = 15
def charmander():
    global name
    global hpmoje
    global atak1
    global atak2
    global atak3
    global atak4
    global mojlevel
    global grafika
    grafika = 'https://drive.google.com/file/d/1KY8PavwSz3H03ZPZ-IalnGc1swZAVUDs/view?usp=sharing'
    name = 'charmander'
    hpmoje = 120
    atak1 = 40
    atak2 = 15
    atak3 = 20
    atak4 = 10
def squirtle():
    global name
    global hpmoje
    global atak1
    global atak2
    global atak3
    global atak4
    global mojlevel
    global grafika
    grafika = 'https://drive.google.com/file/d/1Mskq7X8OMDztd23jzGBYGznlwJ1ttLFJ/view?usp=sharing'
    name = 'squirtle'
    hpmoje = 90
    atak1 = 20
    atak2 = 5
    atak3 = 15
    atak4 = 10
def pikachu():
    global name
    global hpmoje
    global atak1
    global atak2
    global atak3
    global atak4
    global mojlevel
    global grafika
    grafika = 'https://drive.google.com/file/d/1o9wtU2VazOD0UMNGbP9cRT1iuREki5kk/view?usp=sharing'
    name = 'pikachu'
    hpmoje = 150
    atak1 = 50
    atak2 = 40
    atak3 = 30
    atak4 = 35
def ratata():
    global name
    global hpmoje
    global atak1
    global atak2
    global atak3
    global atak4
    global grafika
    grafika = 'https://drive.google.com/file/d/1aRdeFsj-6RmJsbmKNbTwyV5qmMEJ8DF1/view?usp=sharing'
    name = 'rattata'
    hpmoje = 50
    atak1 = 10
    atak2 = 15
    atak3 = 7
    atak4 = 3
def pidgey():
    global name
    global hpmoje
    global atak1
    global atak2
    global atak3
    global atak4
    global grafika
    grafika = 'https://drive.google.com/file/d/17QiSsMLLQEXjrHMxlZ2JtOrZb8mZOCPT/view?usp=sharing'
    name = 'pidgey'
    hpmoje = 65
    atak1 = 20
    atak2 = 15
    atak3 = 10
    atak4 = 8
def growlite():
    global name
    global hpmoje
    global atak1
    global atak2
    global atak3
    global atak4
    global grafika
    grafika = 'https://drive.google.com/file/d/1Pei6PiYb9wCsNBubp3rl2n1aRzCKO22L/view?usp=sharing'
    name = 'growlite'
    hpmoje = 200
    atak1 = 80
    atak2 = 60
    atak3 = 40
    atak4 = 20
    # PRZECIWNIK POKI
def bulbasaurenemy():
    global nameenemy
    global hpenemy
    global atakenemy
    nameenemy = 'bulbasaur'
    hpenemy = 100
    atakenemy = 20
def charmanderenemy():
    global nameenemy
    global hpenemy
    global atakenemy
    nameenemy = 'charmander'
    hpenemy = 120
    atakenemy = 40
def squirtleenemy():
    global nameenemy
    global hpenemy
    global atakenemy
    nameenemy = 'squirtle'
    hpenemy = 90
    atakenemy = 20
def pikachuenemy():
    global nameenemy
    global hpenemy
    global atakenemy
    nameenemy = 'pikachu'
    hpenemy = 150
    atakenemy = 50
def ratataenemy():
    global nameenemy
    global hpenemy
    global atakenemy
    nameenemy = 'rattata'
    hpenemy = 50
    atakenemy = 10
def pidgeyenemy():
    global nameenemy
    global hpenemy
    global atakenemy
    nameenemy = 'pidgey'
    hpenemy = 65
    atakenemy = 20
def growliteenemy():
    global nameenemy
    global hpenemy
    global atakenemy
    nameenemy = 'growlite'
    hpenemy = 200
    atakenemy = 5
# WYBOR POKEMONA--------------------------------------------------------------------------------------------
def wybor():
    global mojlevel
    global money
    money = 0
    argbh = input('Witaj miszczu pokemon,')
    argbh = input('To ja Profesor D??B')
    argbh = input('https://drive.google.com/file/d/18NwjNCAX5mECUw0Y39BNveptOefhASFH/view?usp=sharing')
    argbh = input('Wybierz pokemona startowego')
    argbh = input('Masz do wyboru:')
    argbh = input('Bulbasaur: https://drive.google.com/file/d/1g_dYa0hyTkSdnQMMi1v4smUMHEQR3deA/view?usp=sharing')
    argbh = input('Charmander: https://drive.google.com/file/d/1KY8PavwSz3H03ZPZ-IalnGc1swZAVUDs/view?usp=sharing')
    argbh = input('Squirtle: https://drive.google.com/file/d/1Mskq7X8OMDztd23jzGBYGznlwJ1ttLFJ/view?usp=sharing')
    inp = input('Co wybierasz? ').lower()
    if inp == 'bulbasaur':
        bulbasaur()
    elif inp == 'charmander':
        charmander()
    elif inp == 'squirtle':
        squirtle()
    else:
        argbh = input('eee')
        argbh = input('nie chcesz ??adnych z tych?')
        argbh = input('czekaj mam pomys??')
        argbh = input('nie wiedzia??em, ??e jeste?? analfabet??')
        argbh = input('nie wa??ne jak nie chcesz ??adnych z tamtych to dostaniesz:')
        argbh = input('pr??downice z amazona za 15 cent??w')
        pikachu()
    mojlevel = 1
    print('\n')
# DOPASOWANIE Z LEVELEM-------------------------------------------------------------------------------------
def losowanko():
    global pok
    pok = randint(1,7)
    if pok == 1: bulbasaurenemy()
    if pok == 2: charmanderenemy()
    if pok == 3: squirtleenemy()
    if pok == 4: pikachuenemy()
    if pok == 5: ratataenemy()
    if pok == 6: pidgeyenemy()
    if pok == 7: growliteenemy()
def przeciwnik():
    global levelenemy
    global atakenemy
    global levelenemy
    global atakenemyend
    global hpenemyend
    global hpenemy

    levelenemy = int(mojlevel + randint(-5,5))
    if levelenemy <= 0:
        levelenemy = 1
    
    atakenemyend = int(atakenemy + (randint(-5,5)* levelenemy))
    if atakenemyend <= 0:
        atakenemyend = 1

    hpenemyend = hpenemy + 10 + levelenemy/2
    if killcount >= 1:
        hpenemyend /= 3
def mojpokemon():
    global hpmojeend
    global atak1end
    global atak2end
    global atak3end
    global atak4end
    hpmojeend = hpmoje + mojlevel/2
    atak1end = atak1 + mojlevel/2
    atak2end = atak2 + mojlevel/2
    atak3end = atak3 + mojlevel/2
    atak4end = atak4 + mojlevel/2
# EWOLUCJE--------------------------------------------------------------------------------------------------
def evolucja():
    if name == 'bulbasaur' and mojlevel == 16:
        print(f'Gratulacje!!! Tw??j pokemon ewoluowa?? z {name}')
        name = 'ivysaur'
        print(f'do {name}')
    if name == 'ivysaur' and mojlevel == 32:
        print(f'Gratulacje!!! Tw??j pokemon ewoluowa?? z {name}')
        name = 'venusaur'
        print(f'do {name}')
    if name == 'charmander' and mojlevel == 16:
        print(f'Gratulacje!!! Tw??j pokemon ewoluowa?? z {name}')
        name = 'charmeleon'
        print(f'do {name}')
    if name == 'charmeleon' and mojlevel == 32:
        print(f'Gratulacje!!! Tw??j pokemon ewoluowa??  {name}')
        name = 'charizard'
        print(f'do {name}')
    if name == 'squirtle' and mojlevel == 16:
        print(f'Gratulacje!!! Tw??j pokemon ewoluowa?? z {name}')
        name = 'wartortle'
        print(f'do {name}')
    if name == 'watrortle' and mojlevel == 32:
        print(f'Gratulacje!!! Tw??j pokemon ewoluowa?? z {name}')
        name = 'blastoise'
        print(f'do {name}')
    if name == 'pidey' and mojlevel == 18:
        print(f'Gratulacje!!! Tw??j pokemon ewoluowa?? z {name}')
        name = 'pidgeotto'
        print(f'do {name}')
    if name == 'pidgeotto' and mojlevel == 36:
        print(f'Gratulacje!!! Tw??j pokemon ewoluowa?? z {name}')
        name = 'pidgeot'
        print(f'do {name}')
    if name == 'rattata' and mojlevel == 20:
        print(f'Gratulacje!!! Tw??j pokemon ewoluowa?? z {name}')
        name = 'raticate'
        print(f'do {name}')
    if name == 'growlite' and mojlevel == 32:
        print(f'Gratulacje!!! Tw??j pokemon ewoluowa?? z {name}')
        name = 'arcanine'
        print(f'do {name}')
# POKEBALLE-------------------------------------------------------------------------------------------------
def pokeball():
    global pokebal
    global greatbal
    global ultrabal
    global masterbal
    pokebal = 100
    greatbal = 50
    ultrabal = 30
    masterbal = 1
def lapanie():
    global pokebal
    global greatbal
    global ultrabal
    global masterbal
    print(f'Masz do wyboru: pokekule ({pokebal}), ??wietn??kule ({greatbal}), ultrakul?? ({ultrabal}), mistzrowsk??kul?? ({masterbal})')
    inp2 = input('Kt??ry ball? ').lower()
    if inp2 == 'pokekula':
        pokebal -= 1
        losuj = randint(1,1000000)
        if losuj == 2456:
            print(f'Gratulacje!!! Z??apa??e?? {nameenemy}')
            z??apany = True
    elif inp2 == '??wietnakula':
        greatbal -= 1
        losuj = randint(1,10000)
        if losuj == 1356:
            print(f'Gratulacje!!! Z??apa??e?? {nameenemy}')
            z??apany = True
    elif inp2 == 'ultrakula':
        ultrabal -= 1
        losuj = randint(1,100)
        if losuj == 58:
            print(f'Gratulacje!!! Z??apa??e?? {nameenemy}')
            z??apany = True
    elif inp2 == 'mistrzowskakula':
        masterbal -= 1
        print(f'Gratulacje!!! Z??apa??e?? {nameenemy}')
        z??apany = True
    else: 
        z??apany = False
        argbh = input('pokemon uciek?? z pokeballa')
    if z??apany == True:
        if nameenemy == 'bulbasaur':
            bulbasaur()
        elif nameenemy == 'charmander':
            charmander()
        elif nameenemy == 'squirtle':
            squirtle()
        elif nameenemy == 'rattata':
            ratata()
        elif nameenemy == 'pidgey':
            pidgey()
        elif nameenemy == 'growlite':
            growlite()
# SKLEP-----------------------------------------------------------------------------------------------------
def sklep():
    global pokebal
    global greatbal
    global ultrabal
    global masterbal
    global leczmale
    global leczsrednie
    global leczduze
    global iloscatak1
    global iloscatak2
    global iloscatak3
    global iloscatak4
    global money
    wyjdz = False
    aopauhwdpa = input('Witaj!')
    aopauhwdpa = input('Jeste?? w sklepie')
    aopauhwdpa = input('Chcesz zobaczy?? moje towary? ')
    aopauhwdpa = input('eh, i tak nie obchodzi mnie twoje zdanie')
    aopauhwdpa = input('Mo??esz kupi??: KULE, Leczenia dla pokemona, Odnowienie atak??w')
    inp = input('Co bierzesz? ').lower()
    if inp == 'kule':
        print(f'Masz {money} Boliwar??w Wenezuelskich')
        inp2 = input('jakie kule? Masz do wyboru: POKEKULA za 1000 boliwar??w, SWIETNAKULA za 2000 boliwar??w, ULTRAKULA za 5000 boliwar??w i MISTRZOWSKAKULA za 100000 ').lower()
    elif inp == 'leczenie':
        print(f'Masz {money} Boliwar??w Wenezuelskich')
        inp2 = input('jakie leczenie? Masz do wyboru: MALE za 1000 boliwar??w, SREDNIE za 3000 boliwar??w i DUZE za 5000 ').lower()
    elif inp == 'odnowienia':
        print(f'Masz {money} Boliwar??w Wenezuelskich')
        inp2 = input('Na kt??ry atak? Masz do wyboru: ATAK 1 ,  ATAK 2 , ATAK 3 i ATAK 4 ka??dy za 3000 boliwar??w ').lower()            
    else:
        uohdawd = input('NIE mam ci?? dosy?? wywalaj ze sklepu ')
        wyjdz = True
    if wyjdz == False:
        
        ilosc = int(input('ile chcesz? '))

        if inp2 == 'pokekula' and money*ilosc > 1000:
            pokebal += ilosc
            money -= 1000*ilosc
        elif inp2 == 'swietnakula' and money*ilosc > 2000:
            greatbal += ilosc
            money -= 2000*ilosc
        elif inp2 == 'ultrakula' and money*ilosc > 5000:
            ultrabal += ilosc
            money -= 5000*ilosc
        elif inp2 == 'mistrzowskakula' and money*ilosc > 100000:
            masterbal += ilosc
            money -= 100000*ilosc
        elif inp2 == 'male' and money*ilosc > 1000:
            leczmale += ilosc
            money -= 1000*ilosc
        elif inp2 == 'srednie' and money*ilosc > 3000:
            leczsrednie += ilosc
            money -= 3000*ilosc
        elif inp2 == 'duze' and money*ilosc > 5000:
            leczduze += ilosc
            money -= 5000*ilosc
        elif inp2 == 'atak 1' and money*ilosc > 3000:
            iloscatak1 += ilosc
            money -= 3000*ilosc
        elif inp2 == 'atak 2' and money*ilosc > 3000:
            iloscatak2 += ilosc
            money -= 3000*ilosc
        elif inp2 == 'atak 3' and money*ilosc > 3000:
            iloscatak3 += ilosc
            money -= 3000*ilosc
        elif inp2 == 'atak 4' and money*ilosc > 3000:
            iloscatak4 += ilosc
            money -= 3000*ilosc
        aopauhwdpa = input('Id?? i nigdy wi??cej nie wracaj!')
    if money < 0:
        print('https://drive.google.com/file/d/1oGzoZKCFQO-00JSjNQu2uYWuzzVuBcvn/view?usp=sharing')
        exit()
# LECZENIE--------------------------------------------------------------------------------------------------
def leczenie():
    global hpenemyend
    global leczmale
    global leczsrednie
    global leczduze
    print(f'masz {leczmale} ma??ych fiolek')
    print(f'masz {leczsrednie} ??rednich fiolek')
    print(f'masz {leczduze} du??ych fiolek')
    inp = input('Kt??re fiolki?').lower()
    if inp == 'male' and leczmale > 0:
        hpmojeend += leczmale
        leczmale -= 1
    if inp == 'srednie' and leczsrednie > 0:
        hpmojeend += leczsrednie*5
        leczmale -= 1
    if inp == 'duze' and leczduze > 0:
        hpmojeend += leczduze*10
        leczmale -= 1
    else:
        print('sory nic nie uleczono')
# EXP-------------------------------------------------------------------------------------------------------
def exp():
    global xp
    global mojlevel
    xp = 0
    xp += levelenemy/2
    if xp > mojlevel or xp == mojlevel:
        afgiayfgaifawikbgiakfbaifugbaifaogbaof = input('KOLEJNY LEVEL !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        mojlevel += 1
        xp = 0
# KOLEJNO???? RZECZY------------------------------------------------------------------------------------------
wybor()
pokeball()
przeciwnik()
mojpokemon()
def runda():
    global hpenemyend
    global hpmojeend
    global killcount
    global iloscatak1
    global iloscatak2
    global iloscatak3
    global iloscatak4
    global money
    losowanko()
    while True:
        print('Tw??j przeciwnik to:',nameenemy)
        print('HP przeciwnika to: ',round(hpenemyend,2))
        print('LVL przeciwnika to: ',levelenemy)
        print('\n')
        print('Twoj pokemon to: ',name)
        print(grafika)
        print('Jego level to: ',mojlevel)
        print('Jego HP wynosi: ',int(hpmojeend))
        print('1 atak zadaje:',int(atak1end))
        print(f'masz {iloscatak1} atak??w 1')
        print('2 atak zadaje:',int(atak2end))
        print(f'masz {iloscatak2} atak??w 2')
        print('3 atak zadaje:',int(atak3end))
        print(f'masz {iloscatak3} atak??w 3')
        print('4 atak zadaje:',int(atak4end))
        print(f'masz {iloscatak4} atak??w 4')
        print('\n')
        inp = input('Kt??ry atak wybierasz, czy mo??e ??apiesz go? (pisz np. atak 1 lub napisz lapie) ').lower()
        if inp == 'atak 1' and iloscatak1 > 0:
            hpenemyend = int(hpenemyend - atak1end)
            iloscatak1 -= 1
            print(f'twoj pokemon u??y??: atak 1 i zada?? {atak1end} damage a')
        elif inp == 'atak 2' and iloscatak2 > 0:
            hpenemyend = hpenemyend - atak2end
            iloscatak2 -= 1
            print(f'twoj pokemon u??y??: atak 2 i zada?? {atak2end} damage a')
        elif inp == 'atak 3' and iloscatak3 > 0:
            hpenemyend = hpenemyend - atak3end
            iloscatak3 -= 1
            print(f'twoj pokemon u??y??: atak 3 i zada?? {atak3end} damage a')
        elif inp == 'atak 4' and iloscatak4 > 0:
            hpenemyend = hpenemyend - atak4end
            iloscatak4 -= 1
            print(f'twoj pokemon u??y??: atak 4 i zada?? {atak4end} damage a')
        elif inp == 'lapie':
            lapanie()        
        else:
            aosfgbhuhofasbinfhoasihfaos=input('Twoj pokemon nie zrozumia?? co gada??e??')
        if hpenemyend <= 0:
            afglbhuogaghuoavgbyifgbi = input('GRATULACJE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Zabi??e?? przeciwnika! Teraz nadchodzi kolejny!')
            print(f'Dosta??e?? {levelenemy/2} expa')
            money += levelenemy*5
            killcount += 1
            inp3 = input('chcesz leczy???').lower()
            if inp3 == 'tak':
                leczenie()
            los = randint(1,8)
            if los == 1:
                sklep()
            exp()
            przeciwnik()
            runda()
        else:
            print('Przeciwnik atakuje i zadaje: ',atakenemyend)
            hpmojeend = hpmojeend - atakenemyend
        print('\n'*3)
        if hpmojeend <= 0: 
            print('https://drive.google.com/file/d/10VleoghoIasBFFJCI836n7PloeMiWynK/view?usp=sharing '*20)
            print('\n killcount to: ',killcount)
            break
runda()
