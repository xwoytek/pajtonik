from klassfizyk import wszst

Ouagadougou = wszst

print('Co obliczasz \n 1 - prędkość \n 2 - drogę \n 3 - czas \n 4 - przyśpieszenie \n 5 - prędkość średnią \n 6 - wykres położenia od czasu \n 7 - przyśpieszenie średnie \n 8 - zmianę prędkości \n 9 - zmianę czasu \n 10 - deltę \n 11 - siłę tarcia \n 12 - siłę grawitacji \n 13 - opór areodynamiczny \n 14 - energię w spoczynku  \n 15 - ciśnienie \n 16 - energię kinetyczną  \n 17 - gęstość \n 18 - siła wyporu')

inp = int(input())

if inp == 1:
    Ouagadougou.s = float(input('Dej s '))
    Ouagadougou.t = float(input('Dej t '))
    print(Ouagadougou.s/Ouagadougou.t)
if inp == 2:
    Ouagadougou.t = float(input('Dej t '))
    Ouagadougou.v = float(input('Dej v '))
    print(Ouagadougou.t*Ouagadougou.v)
if inp == 3:
    Ouagadougou.s = float(input('Dej s '))
    Ouagadougou.v = float(input('Dej v '))
if inp == 4:
    Ouagadougou.v0 = float(input('Dej v0 '))
    Ouagadougou.vk = float(input('Dej vk '))
    Ouagadougou.t = float(input('Dej t '))
    print(abs(Ouagadougou.v0 - Ouagadougou.vk)/Ouagadougou.t)
if inp == 5:
    Ouagadougou.v0 = float(input('Dej v0 '))
    Ouagadougou.vk = float(input('Dej vk '))
    Ouagadougou.t0 = float(input('Dej t0 '))
    Ouagadougou.tk = float(input('Dej tk '))
    print((Ouagadougou.v0 + Ouagadougou.vk)/(Ouagadougou.t0 - Ouagadougou.tk))
if inp == 6:
    Ouagadougou.x0 = float(input('Dej x0 '))
    Ouagadougou.v = float(input('Dej v '))
    Ouagadougou.t = float(input('Dej t '))
    print(Ouagadougou.x0 + Ouagadougou.v * Ouagadougou.t)
if inp == 7:
    Ouagadougou.v0 = float(input('Dej v0 '))
    Ouagadougou.vk = float(input('Dej vk '))
    Ouagadougou.t0 = float(input('Dej t0 '))
    Ouagadougou.tk = float(input('Dej tk '))
    print((Ouagadougou.v0 + Ouagadougou.vk)/(Ouagadougou.t0 - Ouagadougou.tk))
if inp == 8:
    Ouagadougou.v0 = float(input('Dej v0 '))
    Ouagadougou.vk = float(input('Dej vk '))
    print(abs(Ouagadougou.v0-Ouagadougou.vk))
if inp == 9:
    Ouagadougou.t0 = float(input('Dej t0 '))
    Ouagadougou.tk = float(input('Dej tk '))
    print(abs(Ouagadougou.t0 - Ouagadougou.tk))
if inp == 10:
    Ouagadougou.adodelty = float(input('Dej a '))
    Ouagadougou.bdodelty = float(input('Dej b '))
    Ouagadougou.cdodelty = float(input('Dej c '))
    print(Ouagadougou.bdodelty-4*Ouagadougou.adodelty*Ouagadougou.cdodelty)
if inp == 11:
    Ouagadougou.fn = float(input('Dej fn '))
    Ouagadougou.fs = float(input('Dej fs '))
    print(Ouagadougou.fn*Ouagadougou.fs)
if inp == 12:
    Ouagadougou.m = float(input('Dej m '))
    Ouagadougou.g = float(input('Dej g '))
    print(Ouagadougou.m*Ouagadougou.g)
if inp == 13:
    Ouagadougou.p = float(input('Dej gęstość powietrza '))
    Ouagadougou.v = float(input('Dej v '))
    Ouagadougou.cd = float(input('Dej cd '))
    Ouagadougou.area = float(input('Dej powierzchnię '))
    print(Ouagadougou.p/2 * Ouagadougou.v**2 * Ouagadougou.cd * Ouagadougou.area)
if inp == 14:
    Ouagadougou.m = float(input('Dej m '))
    print(Ouagadougou.m*Ouagadougou.c**2)
if inp == 15:
    Ouagadougou.fn = float(input('Dej fn '))
    Ouagadougou.area = float(input('Dej powierzchnię '))
    print(Ouagadougou.fn/Ouagadougou.area)
if inp == 16:
    Ouagadougou.m = float(input('Dej m '))
    Ouagadougou.v = float(input('Dej v '))
    print(Ouagadougou.m/2*Ouagadougou.v**2)
if inp == 17:
    Ouagadougou.m = float(input('Dej m '))
    Ouagadougou.objetosc = float(input('Dej objętość '))
    print(Ouagadougou.m/Ouagadougou.objetosc)
if inp == 18:
    Ouagadougou.dc = float(input('Dej gęstość cieczy'))
    Ouagadougou.objetosc = float(input('Dej objętość '))
    Ouagadougou.g = float(input('Dej g '))
    print(Ouagadougou.dc*Ouagadougou.objetosc*Ouagadougou.g)