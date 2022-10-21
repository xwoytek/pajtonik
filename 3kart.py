from random import randint


def zadanie1():
    list1 = [1,4,5,2,6]
    def maximum(arr):
        max_ = arr[0]
        for ele in arr:
            if(ele > max_):
                max_ = ele
        return max_ 
    result = maximum(list1)
    print(result)

def zadanie2():
    lista2 = []
    lista1 = []
    a = int(input('ile elementow '))
    for i in range(a):
        losowy = randint(1,100)
        lista1.append(losowy)
        if losowy % 5 == 0:
            lista2.append(losowy)
    print('cala lista --->',lista1)
    print('podzielne przez 5 --->',lista2)

def zadanie3():
    lista3 = []
    a3 = int(input('ile elementow '))
    b3 = int(input('minimum '))
    c3 = int(input('maksimum '))
    for i in range(a3):
        losowy3 = randint(b3,c3)
        lista3.append(losowy3)
    print(lista3)

def zadanie4():
    lista4 = []
    lista4cala = []
    a4 = int(input('ile elementow '))
    b4 = int(input('minimum '))
    c4 = int(input('maksimum '))
    for u in range(a4):
        inp = randint(b4,c4)
        lista4cala.append(inp)
        i = inp - 1
        prime = True
        if i == 1 or i == 2:
            prime = True
        elif i > 2:
            while i > 2:
                if inp % i == 0:
                    prime = False
                i -= 1
        else:
            prime = False
        if prime == True:
            lista4.append(inp)
    print('cala lista --->',lista4cala)
    print('liczby pierwsze --->',lista4)

def zadanie5():
    lista5parz = []
    lista5nieparz = []
    a5 = int(input('ile elementow '))
    b5 = int(input('minimum '))
    c5 = int(input('maksimum '))
    for i in range(a5):
        losowy4 = randint(b5,c5)
        if losowy4 % 2 == 0:
            lista5parz.append(losowy4)
        else:
            lista5nieparz.append(losowy4)
    print('parzyste --->', lista5parz)
    print('nieparzyste --->', lista5nieparz)

def zadanie6():
    zdanie = input()
    licznikduzea = 0
    licznikmalea = 0
    print('lista --->',zdanie)
    if ('A' in zdanie):
        licznikduzea + 1
    if ('a' in zdanie):
        licznikmalea + 1
    print('duze A --->',licznikduzea)
    print('male a --->',licznikmalea)
