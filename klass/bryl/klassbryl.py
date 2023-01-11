from math import pi
class wszst:
 

    def __init__(self,a,b,c,r,h,pp,pb):
        self.a = a
        self.b = b
        self.c = c
        self.r = r
        self.h = h
        self.pp = pp
        self.pb = pb



        


    def objszescian(self):
        print(self.a**3)

    def objprostopadloscian(self):
        print(self.a*self.b*self.c)

    def objgraniastoslup(self):
        print(self.pp*self.h)

    def objostroslup(self):
        print(1/3 * self.pp * self.h)

    def objwalec(self):
        print(pi*self.r**2*self.h)

    def objkula(self):
        print(4/3*pi*self.r**3)

    def poleszescian(self):
        print(6*self.a**2)

    def poleprostopadloscian(self):
        print(2*self.a*self.b+2*self.a*self.c+2*self.b*self.c)

    def polegraniastoslup(self):
        print(2*self.pp+self.pb)

    def poleostroslup(self):
        print(self.pp+self.pb)

    def polewalec(self):
        print(pi*2*self.r**2+2*pi*self.r*self.h)
        
    def polekula(self):
        print(4*pi*self.r**2)