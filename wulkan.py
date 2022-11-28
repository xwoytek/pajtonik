from random import randint
ludzie = [
    {
        "imie":"Kemal",
        "nazwisko":"Schultz",
        "praca":"komornik sądowy",
        "edukacja" : "najniższa",
        "data urodzin" : randint(1,2023),
        "hobby": ['podbijanie ludów germańskich','wytwarzanie broni','inwestowanie'],
    },
    {
        "imie":"Remigiusz",
        "nazwisko":"Sokołowski",
        "praca":"Wojownik",
        "edukacja" : "podstawowa",
        "data urodzin" : randint(1,2023),
        "hobby": ['rozbijanie samolotów','animowanie','rzutki']
    },
    {
        "imie":"Eustachy",
        "nazwisko":"Mazur",
        "praca":"pilot marynarki wojennej Stanów Zjednoczonych",
        "edukacja" : "średnia",
        "data urodzin" : randint(1,2023),
        "hobby": ['topienie czołgów','hazard','djembe']
    },
    {
        "imie":"Aneta",
        "nazwisko":"Mróz",
        "praca":"malarka",
        "edukacja" : "brak",
        "data urodzin" : randint(1,2023),
        "hobby": ['robienie mydła','Obróbka drewna','robienie drinków'],
    },
    {
        "imie":"Arkadiusz ",
        "nazwisko":"Szymczak",
        "praca":"hydraulik",
        "edukacja" : "podstawowa",
        "data urodzin" : randint(1,2023),
        "hobby": ['robienie noży','warcaby','botania']
    },
    {
        "imie":"Florentyna",
        "nazwisko":"Czarnecka",
        "praca":"wizażystka zwłok",
        "edukacja" : "Wyższe",
        "data urodzin" : randint(1,2023),
        "hobby": ['Robienie sera','zbieranie kamieni','futbol australijski']
    }]

print(ludzie)
def usuwacz():
    inp = input('kogo usuwać???????????????????????????????????????????????????????????????????????????????????????')
    i = 0
    for slownik in ludzie:
        if slownik["imie"] == inp:  
            t = 'Przed użyciem zapoznaj się z treścią ulotki dołączonej do opakowania bądź skonsultuj się z lekarzem lub farmaceutą, gdyż każdy lek niewłaściwie stosowany zagraża Twojemu życiu lub zdrowiu'
            print(f"Wpisz {t} aby potwierdzić")
            t_imp = input()
            if t_imp == t:
                print(f"Gratuluje usunałes uzytkownika {inp} teraz pamietaj, że ta czynnosc była nieodrwacalnia i nie da sie tego naprawic")
                ludzie.pop(i)
            else:
                print("a sory to nie usuwam")
        else:
            print("Error 404 Not Found")
        i += 1



def dodejhobbi ():
    hobby_lista = []
    while True:
        print("stop - napisz kiedy kończtsz")
        inp = input("").lower()
        if inp == "stop":
            break
        else:
            hobby_lista.append(inp)  
    return hobby_lista
def zmienpracownikow():
    for slownik in ludzie:
        inp = input("Podaj osobe ")
        print("e - wyjdz")
        if slownik.get("imie") == inp:  
            while True:
                print("""
                Co chcesz zmienic
                1 - imie, 2 - nazwisko
                3 - praca , 4 - edukacja
                5 - data urodzin, 6 - hobby, 7 - KONIEC
                """)
                inp_num= int(input("Podaj liczbe "))
                if inp_num == 1:
                    inp = input("IMIE ? ")
                    slownik["imie"] = inp
                elif inp_num == 2:
                    inp = input("NAZWISKO ? ")
                    slownik["nazwisko"] = inp
                elif inp_num == 3:
                    inp = input("PRACA ? ")
                    slownik["praca"] = inp  
                elif inp_num == 4:
                    inp = input("edukacja ? ")
                    slownik["edukacja"] = inp  
                elif inp_num == 5:
                    inp = input("data urodzin ? ")
                    slownik["data urodzin"] = int(inp)  
                elif inp_num == 6:
                    inp = input("hobby ? ")
                    slownik["hobby"] = dodejhobbi()
                elif inp_num == 7:
                    break
                else:
                    print("Co ty próbujesz?")
                    continue
        elif inp == "e":
            break
        else:
            print("Error 404 Not Found")


inp = input('USUWASZ CZY EDYTUJESZ??????????????????????????????    ')
if inp == 'USUWAM':
    usuwacz()
if inp == 'EDYTUJE':
    zmienpracownikow()