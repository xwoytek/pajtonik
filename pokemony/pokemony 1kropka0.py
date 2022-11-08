from random import randint
import math
atakenemy = 0
hpenemy = 0
killcount = 0
# POKEMONY-------------------------------------------------------------------------------------------------
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
    print('Witaj miszczu pokemon, wybierz pokemona startowego:')
    print('Bulbasaur: https://drive.google.com/file/d/1g_dYa0hyTkSdnQMMi1v4smUMHEQR3deA/view?usp=sharing')
    print('Charmander: https://drive.google.com/file/d/1KY8PavwSz3H03ZPZ-IalnGc1swZAVUDs/view?usp=sharing')
    print('Squirtle: https://drive.google.com/file/d/1Mskq7X8OMDztd23jzGBYGznlwJ1ttLFJ/view?usp=sharing')
    inp = input('Co wybierasz? ').lower()
    if inp == 'bulbasaur':
        bulbasaur()
    elif inp == 'charmander':
        charmander()
    elif inp == 'squirtle':
        squirtle()
    else:
        print('gratuluje analfabetyzmu, coś źle napisałeś więc masz lepszego pokemona')
        pikachu()
    mojlevel = 1
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
        print('Gratulacje!!! Twój pokemon ewoluował z',name)
        name = 'ivysaur'
        print('do',name)
    if name == 'ivysaur' and mojlevel == 32:
        print('Gratulacje!!! Twój pokemon ewoluował z',name)
        name = 'venusaur'
        print('do',name)
    if name == 'charmander' and mojlevel == 16:
        print('Gratulacje!!! Twój pokemon ewoluował z',name)
        name = 'charmeleon'
        print('do',name)
    if name == 'charmeleon' and mojlevel == 32:
        print('Gratulacje!!! Twój pokemon ewoluował z',name)
        name = 'charizard'
        print('do',name)
    if name == 'squirtle' and mojlevel == 16:
        print('Gratulacje!!! Twój pokemon ewoluował z',name)
        name = 'wartortle'
        print('do',name)
    if name == 'watrortle' and mojlevel == 32:
        print('Gratulacje!!! Twój pokemon ewoluował z',name)
        name = 'blastoise'
        print('do',name)
    if name == 'pidey' and mojlevel == 18:
        print('Gratulacje!!! Twój pokemon ewoluował z',name)
        name = 'pidgeotto'
        print('do',name)
    if name == 'pidgeotto' and mojlevel == 36:
        print('Gratulacje!!! Twój pokemon ewoluował z',name)
        name = 'pidgeot'
        print('do',name)
    if name == 'rattata' and mojlevel == 20:
        print('Gratulacje!!! Twój pokemon ewoluował z',name)
        name = 'raticate'
        print('do',name)
    if name == 'growlite' and mojlevel == 32:
        print('Gratulacje!!! Twój pokemon ewoluował z',name)
        name = 'arcanine'
        print('do',name)
# POKEBALLE-------------------------------------------------------------------------------------------------
def pokeball():
    global pokebal
    global greatbal
    global ultrabal
    global masterbal
    pokebal = 10
    greatbal = 5
    ultrabal = 3
    masterbal = 1
def lapanie():
    global pokebal
    global greatbal
    global ultrabal
    global masterbal
    print('pokeball, greatball, ultraball, masterball')
    inp2 = input('Który ball? ').lower()
    if inp2 == 'pokeball':
        pokebal -= 1
        losuj = randint(1,1000000)
        if losuj == 2456:
            print('Gratulacje!!! Złapałeś ',nameenemy)
            złapany = True
    elif inp2 == 'greatball':
        greatbal -= 1
        losuj = randint(1,10000)
        if losuj == 1356:
            print('Gratulacje!!! Złapałeś ',nameenemy)
            złapany = True
    elif inp2 == 'ultraball':
        ultrabal -= 1
        losuj = randint(1,100)
        if losuj == 58:
            print('Gratulacje!!! Złapałeś ',nameenemy)
            złapany = True
    elif inp2 == 'masterball':
        masterbal -= 1
        print('Gratulacje!!! Złapałeś ',nameenemy)
        złapany = True
    else: 
        złapany = False
        print('pokemon uciekł z pokeballa')
    if złapany == True:
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

# EXP-------------------------------------------------------------------------------------------------------
def exp():
    global xp
    global mojlevel
    xp = 0
    xp += levelenemy/10
    if xp == mojlevel:
        print('KOLEJNY LEVEL !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        mojlevel += 1
# KOLEJNOŚĆ RZECZY------------------------------------------------------------------------------------------
wybor()
pokeball()
przeciwnik()
mojpokemon()

def runda():
    global hpenemyend
    global hpmojeend
    global killcount
    slic = slice(0,3)
    losowanko()
    while True:
        print('Twój przeciwnik to:',nameenemy)
        print('HP przeciwnika to: ',round(hpenemyend,2))
        print('LVL przeciwnika to: ',levelenemy)
        print('\n')
        print('Twoj pokemon to: ',name)
        print(grafika)
        print('Jego level to: ',mojlevel)
        print('Jego HP wynosi: ',int(hpmojeend))
        print('1 atak zadaje:',int(atak1end))
        print('2 atak zadaje:',int(atak2end))
        print('3 atak zadaje:',int(atak3end))
        print('4 atak zadaje:',int(atak4end))
        inp = input('Który atak wybierasz, czy może łapiesz go? (pisz np. atak 1 lub napisz pokeball) ').lower()
        if inp == 'atak 1':
            hpenemyend = int(hpenemyend - atak1end)
            print('twoj pokemon użył: atak 1 i zadał ',atak1end)
        elif inp == 'atak 2':
            hpenemyend = hpenemyend - atak2end
            print('twoj pokemon użył: atak 2 i zadał ',atak2end)
        elif inp == 'atak 3':
            hpenemyend = hpenemyend - atak3end
            print('twoj pokemon użył: atak 3 i zadał ',atak3end)
        elif inp == 'atak 4':
            hpenemyend = hpenemyend - atak4end
            print('twoj pokemon użył: atak 4 i zadał ',atak4end)
        elif inp == 'pokeball':
            lapanie()        
        else:
            print('Twoj pokemon nie zrozumiał co gadałeś')
        if hpenemyend <= 0:
            print('GRATULACJE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Zabiłeś przeciwnika! Teraz nadchodzi kolejny!')
            killcount += 1
            print(killcount)
            exp()
            przeciwnik()
            runda()
        else:
            print('Przeciwnik atakuje i zadaje: ',atakenemyend)
            hpmojeend = hpmojeend - atakenemyend
        if hpmojeend <= 0: 
            print('https://drive.google.com/file/d/10VleoghoIasBFFJCI836n7PloeMiWynK/view?usp=sharing')
            break

runda()
