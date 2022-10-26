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

