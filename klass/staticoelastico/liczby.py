class pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery:
    
    @staticmethod
    def kalkulujv(s,t):
        print(s/t)
    @staticmethod
    def kalkulujs(t,v):
        print(t*v)
    @staticmethod
    def kalkulujt(s,v):
        print(s/v)
    @staticmethod
    def kalkuluja(v0,vk,t):
        print(abs(v0-vk)/t)
    @staticmethod
    def kalkulujvsr(v0,vk,t0,tk):
        print((v0 + vk)/(t0 - tk))
    @staticmethod
    def kalkulujxt(x0,v,t):
        print(x0 + v * t)
    @staticmethod
    def kalkulujasr(v0,vk,t0,tk):
        print(abs(v0 - vk) / (t0 - tk))
    @staticmethod
    def kalkulujdeltav(v0,vk):
        print(abs(v0-vk))
    @staticmethod
    def kalkulujdeltat(t0,tk):
        print(abs(t0-tk))
    @staticmethod
    def kalkulujdelte(adodelty,bdodelty,cdodelty):
        print(bdodelty-4*adodelty*cdodelty)
    @staticmethod
    def kalkulujft(fn,fs):
        print(fn*fs)
    @staticmethod
    def kalkulujfg(m,g):
        print(m*g)
    @staticmethod
    def kalkulujopor(p,v,cd,area):
        print(p/2 * v**2 * cd * area)
    @staticmethod
    def kalkulujajnstajn(m,c):
        print(m*c**2)
    @staticmethod
    def kalkulujprawopascala(fn,area):
        print(fn/area)
    @staticmethod
    def kalkulujpewpew(m,v):
        print(m/2*v**2)
    @staticmethod
    def kalkulujgestosc(m,objetosc):
        print(m/objetosc)
    @staticmethod
    def kalkulujwypornosc(dc,objetosc,g):
        print(dc*objetosc*g)
    @staticmethod
    def kalkulujdlugoscfali(v,f):
        print(v/f)
    @staticmethod
    def kalkulujmocmechaniczna(w,t):
        print(w/t)
    @staticmethod
    def kalkulujpedciala(m,v):
        print(m*v)
    @staticmethod
    def kalkulujnatezenieprondu(q,t):
        print(q/t)
    @staticmethod
    def kalkulujoporelektryk(u,i):
        print(u/i)
    @staticmethod
    def kalkulujczestotliwoscdrgan(t):
        print(1/t)
    @staticmethod
    def kalkulujpracamechaniczna(f,s):
        print(f*s)
    @staticmethod
    def kalkulujcieplo(cw,m,t):
        print(cw*m*t)







#DRUGI PLIK=============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================(nie chciało mi się robić dwóch plików, jak ktoś to czyta to pozdro i powiedz mi 'imperializm')

print('Co obliczasz \n ',
'1 - prędkość \n ',
'2 - drogę \n ',
'3 - czas \n ',
'4 - przyśpieszenie \n ',
'5 - prędkość średnią \n ',
'6 - wykres położenia od czasu \n ',
'7 - przyśpieszenie średnie \n ',
'8 - zmianę prędkości \n ',
'9 - zmianę czasu \n ',
'10 - deltę \n ',
'11 - siłę tarcia \n ',
'12 - siłę grawitacji \n ',
'13 - opór areodynamiczny \n ',
'14 - energię w spoczynku  \n ',
'15 - ciśnienie \n ',
'16 - energię kinetyczną  \n ',
'17 - gęstość \n ',
'18 - siła wyporu',
'19 - długość fali \n ',
'20 - moc mechaniczną \n ',
'21 - pęd ciała \n ',
'22 - natężenie prądu \n ',
'23 - opór elektryczny \n ',
'24 - częstotliwość drgań \n ',
'25 - praca mechaniczna \n ',
'26 - cieplo \n ',)

Ouagadougou = int(input())
if Ouagadougou == 1:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujv(float(input('dej s ')),float(input('dej t ')))
if Ouagadougou == 2:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujs(float(input('dej t ')),float(input('dej v ')))
if Ouagadougou == 3:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujt(float(input('dej s ')),float(input('dej v ')))
if Ouagadougou == 4:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkuluja(float(input('dej v0 ')),float(input('dej vk ')),float(input('dej t ')))
if Ouagadougou == 5:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujvsr(float(input('dej v0 ')),float(input('dej vk ')),float(input('dej t0 ')),float(input('dej tk ')))
if Ouagadougou == 6:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujxt(float(input('dej x0 ')),float(input('dej v ')),float(input('dej t ')))
if Ouagadougou == 7:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujasr(float(input('dej v0 ')),float(input('dej vk ')),float(input('dej t0 ')),float(input('dej tk ')))
if Ouagadougou == 8:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujdeltav(float(input('dej v0 ')),float(input('dej vk ')))
if Ouagadougou == 9:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujdeltat(float(input('dej t0 ')),float(input('dej tk ')))
if Ouagadougou == 10:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujdelte(float(input('dej a ')),float(input('dej b ')),float(input('dej c ')))
if Ouagadougou == 11:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujft(float(input('dej fn ')),float(input('dej fs ')))
if Ouagadougou == 12:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujfg(float(input('dej m ')),float(input('dej g ')))
if Ouagadougou == 13:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujopor(float(input('dej ρ ')),float(input('dej v ')),float(input('dej cd ')),float(input('dej p ')))
if Ouagadougou == 14:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujajnstajn(float(input('dej m ')),299792458)
if Ouagadougou == 15:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujprawopascala(float(input('dej fn ')),float(input('dej p ')))
if Ouagadougou == 16:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujpewpew(float(input('dej m ')),float(input('dej v ')))
if Ouagadougou == 17:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujgestosc(float(input('dej m ')),float(input('dej V ')))
if Ouagadougou == 18:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujwypornosc(float(input('dej ρ ')),float(input('dej V ')),float(input('dej g ')))
if Ouagadougou == 19:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujdlugoscfali(float(input('dej v ')),float(input('dej f ')))
if Ouagadougou == 20:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujmocmechaniczna(float(input('dej w ')),float(input('dej t ')))
if Ouagadougou == 21:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujpedciala(float(input('dej m ')),float(input('dej v ')))
if Ouagadougou == 22:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujnatezenieprondu(float(input('dej Q ')),float(input('dej t ')))
if Ouagadougou == 23:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujoporelektryk(float(input('dej u ')),float(input('dej I ')))
if Ouagadougou == 24:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujczestotliwoscdrgan(float(input('dej T ')))
if Ouagadougou == 25:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujpracamechaniczna(float(input('dej f ')),float(input('dej s ')))
if Ouagadougou == 26:
    pozdrodlaosobktoremowilymiabympisalnazwyklaszduzejlitery.kalkulujcieplo(float(input('dej cw ')),float(input('dej m ')),float(input('dej T ')))