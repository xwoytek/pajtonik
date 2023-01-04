from klassfizyk import wszst
# from random import randint
# ahfioufga = wszst(randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081),randint(1,4780174081))
ahfioufga= wszst(float(input('jakie s? ')),
float(input('jakie v? ')),
float(input('jakie t? ')),
float(input('jakie v0? ')),
float(input('jakie vk? ')),
float(input('jakie s0? ')),
float(input('jakie t0? ')),
float(input('jakie sk? ')),
float(input('jakie tk? ')),
float(input('jakie a? ')),
float(input('jakie vsr? ')),
float(input('jakie x0? ')),
float(input('jakie xt? ')),
float(input('jakie asr? ')),
float(input('jakie delta v? ')),
float(input('jakie delta t? ')),
float(input('jakie a do delty? ')),
float(input('jakie b do delty? ')),
float(input('jakie c do delty? ')),
float(input('jakie fn? ')),
float(input('jaki współczynnik tarcia? ')),
float(input('jakie m t? ')),
float(input('jakie g? ')),
float(input('jaka gęstość powietrza? ')),
float(input('jaki drag coefficient? ')),
float(input('jaka powierzchnia? ')),
float(299792458**2),
float(input('jaka objętość? ')),
float(input('jaka gęstość cieczy? ')))

lista = [ahfioufga]

print('Co obliczasz \n 1 - prędkość \n 2 - drogę \n 3 - czas \n 4 - przyśpieszenie \n 5 - prędkość średnią \n 6 - wykres położenia od czasu \n 7 - przyśpieszenie średnie \n 8 - zmianę prędkości \n 9 - zmianę czasu \n 10 - deltę \n 11 - siłę tarcia \n 12 - siłę grawitacji \n 13 - opór areodynamiczny \n 14 - energię w spoczynku  \n 15 - ciśnienie \n 16 - energię kinetyczną  \n 17 - gęstość \n 18 - siła wyporu')

inp = int(input())

if inp == 1:
    for obj in lista:
        obj.kalkulujv()
if inp == 2:
    for obj in lista:
        obj.kalkulujs()
if inp == 3:
    for obj in lista:
        obj.kalkulujt()
if inp == 4:
    for obj in lista:
        obj.kalkuluja()
if inp == 5:
    for obj in lista:
        obj.kalkulujvsr()
if inp == 6:
    for obj in lista:
        obj.kalkulujxt()
if inp == 7:
    for obj in lista:
        obj.kalkulujasr()
if inp == 8:
    for obj in lista:
        obj.kalkulujdeltav()
if inp == 9:
    for obj in lista:
        obj.kalkulujdeltat()
if inp == 10:
    for obj in lista:
        obj.kalkulujdelte()
if inp == 11:
    for obj in lista:
        obj.kalkulujft()
if inp == 12:
    for obj in lista:
        obj.kalkulujfg()
if inp == 13:
    for obj in lista:
        obj.kalkulujopor()
if inp == 14:
    for obj in lista:
        obj.kalkulujajnstajn()
if inp == 15:
    for obj in lista:
        obj.kalkulujprawopascala()
if inp == 16:
    for obj in lista:
        obj.kalkulujpewpew()
if inp == 17:
    for obj in lista:
        obj.kalkulujgestosc()
if inp == 18:
    for obj in lista:
        obj.kalkulujwypornosc()