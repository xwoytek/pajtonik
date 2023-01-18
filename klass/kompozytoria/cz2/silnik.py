class Silnik:
    def __init__(self) -> None:
        self.__rok_produkcji = None
        self.__liczba_koni = None
    
    # naj pros wersja
    def brrrbrrrr(): 
        print("brrrrrrrrr!!!!!!!!!!!111")

    def informacje(self):
        print("Dane silnika")
        print(self.__rok_produkcji)
        print(self.__liczba_koni)

    def zmien_informacje_silnik(self):
        while True:
            print("="*40)
            print("a - rok produkcji s - liczba koni e - eggsit")
            inp = input().strip().lower()
            if inp == "a":
                inp = int(input())
                self.__rok_produkcji = inp 
            elif inp == "s":
                inp = int(input())
                self.__liczba_koni = inp 
            elif inp == "e":
                break  

