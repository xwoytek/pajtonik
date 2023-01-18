from silnik import Silnik
from akumulator import Akumulator
from sprzeglo import skrzyniabiegow
from bagaznik import bagaznik

class Auto:
    def __init__(self, wlasciciel : str) -> None:
        self.__wlascicel = wlasciciel
        self.__akumlator = Akumulator()
        self.__silnik = Silnik()
        self.__skrzyniabiegow = skrzyniabiegow()
        self.__bagaznik = bagaznik()

    def all_information(self):
        print("="*40)
        print(self.__wlascicel)
        self.__akumlator.informacje()
        self.__silnik.informacje()
        self.__skrzyniabiegow.informacje()
        self.__bagaznik.informacje()
        print("="*40)

    def zmien_informacje(self):
        while True:
            print("co chcesz zmienic")
            print("a - silnik")
            print("b - akumulator")
            print('c - skrzynia biegow')
            print('d - bagaznik')
            print('e - eggsit')
            inp = input().lower().strip()
            if inp == "a":
                self.__silnik.zmien_informacje_silnik()
            if inp == "b":
                self.__akumlator.zmien_dane_akumolatora()
            if inp == "c":
                self.__skrzyniabiegow.zmiendaneskrzynibiegow()
            if inp == "d":
                self.__bagaznik.zmiendanebagaznik()
            if inp == 'e':
                break
            

    def brrrbrrrr(self):
        self.__silnik.brrrbrrrr()
        