from klassbryl import wszst


print('Co obliczasz \n 1 - objętość sześcianu \n 2 - objętość prostopadłościanu \n 3 - objętość graniastosłupa \n 4 - objętość ostrosłupa \n 5 - objętość walca \n 6 - objętość KULI \n 7 - pole sześcianu \n 8 - pole prostopadłościanu \n 9 - pole graniastosłupa \n 10 - pole ostrosłupa \n 11 - pole walca \n 12 - pole KULI')

inp = int(input())

if inp == 1:
    Ouagadougou = wszst(float(input('dej a ')),0,0,0,0,0,0)
    lista = [Ouagadougou]
    for obj in lista:
        obj.objszescian()
if inp == 2:
    Ouagadougou = wszst(float(input('dej a ')),float(input('dej b ')),float(input('dej c ')),0,0,0,0)
    lista = [Ouagadougou]
    for obj in lista:
        obj.objprostopadloscian()
if inp == 3:
    Ouagadougou = wszst(0,0,0,0,float(input('dej wysokosc ')),float(input('dej pole podstawy ')),0)
    lista = [Ouagadougou]
    for obj in lista:
        obj.objgraniastoslup()
if inp == 4:
    Ouagadougou = wszst(0,0,0,0,float(input('dej wysokosc ')),float(input('dej pole podstawy ')),0)
    lista = [Ouagadougou]
    for obj in lista:
        obj.objostroslup()
if inp == 5:
    Ouagadougou = wszst(0,0,0,float(input('dej promien ')),float(input('dej wysokosc ')),0,0)
    lista = [Ouagadougou]
    for obj in lista:
        obj.objwalec()
if inp == 6:
    Ouagadougou = wszst(0,0,0,float(input('dej promien ')),0,0,0)
    lista = [Ouagadougou]
    for obj in lista:
        obj.objkula()


if inp == 7:
    Ouagadougou = wszst(float(input('dej a ')),0,0,0,0,0,0)
    lista = [Ouagadougou]
    for obj in lista:
        obj.poleszescian()

if inp == 8:
    Ouagadougou = wszst(float(input('dej a ')),float(input('dej b ')),float(input('dej c ')),0,0,0,0)
    lista = [Ouagadougou]
    for obj in lista:
        obj.poleprostopadloscian()

if inp == 9:
    Ouagadougou = wszst(0,0,0,0,0,float(input('dej pole podstawy ')),float(input('dej pole boków ')))
    lista = [Ouagadougou]
    for obj in lista:
        obj.polegraniastoslup()

if inp == 10:
    Ouagadougou = wszst(0,0,0,0,0,float(input('dej pole podstawy ')),float(input('dej pole boków ')))
    lista = [Ouagadougou]
    for obj in lista:
        obj.poleostroslup()

if inp == 11:
    Ouagadougou = wszst(0,0,0,float(input('dej promien ')),float(input('dej wysokosc ')),0,0)
    lista = [Ouagadougou]
    for obj in lista:
        obj.polewalec()

if inp == 12:
    Ouagadougou = wszst(0,0,0,float(input('dej promien ')),0,0,0)
    lista = [Ouagadougou]
    for obj in lista:
        obj.polekula()