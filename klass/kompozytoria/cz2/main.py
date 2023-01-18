from auito import Auto


auto = Auto("Ala")


while True:
    auto.all_information()
    print('Zmieniać?')
    print('Y - Tak')
    print('N - Nie')
    inp2 = input().lower()
    if inp2 == 'y':
        auto.zmien_informacje()
    if inp2 == 'n':
        auto.all_information()
        break
