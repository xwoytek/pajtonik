class bagaznik:
    def __init__(self) -> None:
        self.__automatycznosc = None
        self.__cialo = None
        self.__gasnica = None
    
    def informacje(self):
        print("Dane Bagaznika")
        print(self.__automatycznosc)
        print(self.__cialo)
        print(self.__gasnica)


    def zmiendanebagaznik(self):
        while True:
            print("="*40)
            print("a - automatycznosc")
            print("c - cialo w bagazniku")
            print('g - gasnica')
            print("e - eggsit")
            inp = input().lower().strip()
            if inp == "i":
                inp = input().lower().strip()
                self.__automatycznosc = inp
            if inp == "a":
                inp = input().lower().strip()
                self.__cialo = inp
            if inp == "z":
                inp = input().lower().strip()
                self.__gasnica = inp
            if inp == "e":
                break  