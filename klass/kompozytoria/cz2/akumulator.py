class Akumulator:
    def __init__(self) -> None:
        self.__rok_produkcji = None
        self.__firma = None
        self.__moc = None

    def informacje(self):
        print("Dane akumulatora")
        print(self.__rok_produkcji)
        print(self.__firma)
        print(self.__moc)    


    def zmien_dane_akumolatora(self):
        while True:
            print("="*40)
            print("a - rok produkcji")
            print("s - firma")
            print('m - moc')
            print("e - eggsit")
            inp = input().lower().strip()
            if inp == "a":
                inp = input().lower().strip()
                self.__rok_produkcji = inp
            if inp == "s":
                inp = input().lower().strip()
                self.__firma = inp
            if inp == "m":
                inp = input().lower().strip()
                self.__moc = inp
            if inp == "e":
                break