from random import randint
from copy import deepcopy

def zadanie1():
    inp = input('rozumiesz? ').lower()
    if inp == 'tak':
        print('super')
    else:
        zadanie1()

def zadanie2():
    num = int(input('ile liczb '))

    total_sum = 0
    for n in range(num):
        numbers = float(input('dej liczbe '))
        total_sum += numbers


    def my_sum(*all_input):
        result = 0
        for i in all_input:
            result += i
        koniec = result/num
        return koniec
    print(my_sum(total_sum))

def zadanie3():
    num = int(input('ile liczb '))
    total_sum = 0
    for n in range(num):
        numbers = float(input('dej liczbe '))  
        total_sum += 1/numbers
    def my_sum(*all_input):
        result = 0
        for i in all_input:
            result += i
        koniec = num/result
        return koniec
    print(my_sum(total_sum))

def zadanie4():
    global x
    global y 
    x = input()
    y = input()
    x,y=y,x
    print(x)
    print(y)

def zadanie5():
    lista1 = [randint(1,10) for i in range(10)]
    lista2 = [randint(1,10) for i in range(10)]
    lista3 = [randint(1,10) for i in range(10)]
    print(lista1,lista2,lista3)

def zadanie6():
    lista = []
    while len(lista) != 10:
        inp = randint(1,10)
        if inp % 2 != 0 and inp % 3 != 0 and inp % 4 != 0 and inp % 5 != 0 and inp % 6 != 0 and inp % 7 != 0 and inp % 8 != 0 and inp % 9 != 0 and inp % 10  != 0 and inp % 11 != 0 and inp % 22 != 0 and inp % 33 != 0 and inp % 44 != 0 and inp % 55 != 0 and inp % 66 != 0 and inp % 77 != 0 and inp % 88 != 0:
            lista.append(inp)
    print(lista)

def zadanie7():
    lista = []
    while len(lista) != 10:
        inp = randint(1,10)
        if inp % 2 != 0 and inp % 3 != 0 and inp % 5 != 0 and inp % 7 != 0 and inp % 11 != 0 and inp % 13 != 0 and inp % 17 != 0 and inp % 19 != 0 and inp % 23  != 0 and inp % 29 != 0 and inp % 31 != 0 and inp % 37 != 0 and inp % 41 != 0:
            lista.append(inp)
    print(lista)

def zadanie8():
    a = [23,32,123,231,123,32,123]
    b = [23,231,2231,213321,2131,12]
    c = [32,123,123,23,11,113,123,11]
    najwiekszalista = []
    duzea = max(a)
    duzeb = max(b)
    duzec = max(c)
    if duzea>duzeb and duzea>duzec:
        najwiekszalista = deepcopy(a)
    elif duzeb>duzea and duzeb>duzec:
        najwiekszalista = deepcopy(b)
    else:
        najwiekszalista = deepcopy(c)
    print(najwiekszalista)    

def zadanie9():
    a = [23,32,123,231,123,32,123]
    b = [23,231,2231,213321,2131,12]
    c = [32,123,123,23,11,113,123,11]
    mmm = [a,b,c]
    mm2 = deepcopy(mmm)
    for i in range(len(a)):
        if a[i]%2 ==0 or a[i]% 3 ==0:
            a[i] = 100
    for j in range(len(b)):
        if b[j]%2 ==0 or b[j]% 3 ==0:
            b[j] = 100
    for k in range(len(c)):
        if c[k]%2 ==0 or c[k]% 3 ==0:
            c[k] = 100
    print(mm2)
    print(mmm)
