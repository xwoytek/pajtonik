class skrzyniabiegow:
    def __init__(self) -> None:
        self.__ilebiegow = None
        self.__automat = None
        self.__zmaianamocy = None
    
    def informacje(self):
        print("Dane Skrzyni Biegów")
        print(self.__ilebiegow)
        print(self.__automat)
        print(self.__zmaianamocy)


    def zmiendaneskrzynibiegow(self):
        while True:
            print("="*40)
            print("i - ilosc biegow skrzyni")
            print("a - automat")
            print('z - zmiana mocy')
            print("e - eggsit")
            inp = input().lower().strip()
            if inp == "i":
                inp = input().lower().strip()
                self.__ilebiegow = inp
            if inp == "a":
                inp = input().lower().strip()
                self.__automat = inp
            if inp == "z":
                inp = input().lower().strip()
                self.__zmaianamocy = inp
            if inp == "e":
                break  