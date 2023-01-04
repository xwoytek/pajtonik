class wszst:


    def __init__(self,v,s,t,v0,vk,s0,t0,sk,tk,a,vsr,x0,xt,asr,deltav,deltat,adodelty,bdodelty,cdodelty,fn,fs,m,g,p,cd,area,c,objetosc,dc):
        self.s = s
        self.v = v
        self.t = t
        self.v0 = v0
        self.vk = vk
        self.s0 = s0
        self.t0 = t0
        self.sk = sk
        self.tk = tk
        self.a = a
        self.vsr = vsr
        self.x0 = x0
        self.xt = xt
        self.asr = asr
        self.deltav = deltav
        self.deltat = deltat
        self.adodelty = adodelty
        self.bdodelty = bdodelty
        self.cdodelty = cdodelty
        self.fn = fn
        self.fs = fs
        self.m = m
        self.g = g
        self.p = p
        self.cd = cd
        self.area = area
        self.c = c
        self.objetosc = objetosc
        self.dc = dc


        


    def kalkulujv(self):
        print(self.s / self.t)
    def kalkulujs(self):
        print(self.t * self.v)
    def kalkulujt(self):
        print(self.s / self.v)
    def kalkuluja(self):
        print(abs(self.v0 - self.vk)/self.t)
    def kalkulujvsr(self):
        print((self.v0 + self.vk)/(self.t0 - self.tk))
    def kalkulujxt(self):
        print(self.x0 + self.v * self.t)
    def kalkulujasr(self):
        print(abs(self.v0 - self.vk) / (self.t0 - self.tk))
    def kalkulujdeltav(self):
        print(abs(self.v0-self.vk))
    def kalkulujdeltat(self):
        print(abs(self.t0-self.tk))
    def kalkulujdelte(self):
        print(self.bdodelty-4*self.adodelty*self.cdodelty)
    def kalkulujft(self):
        print(self.fn*self.fs)
    def kalkulujfg(self):
        print(self.m*self.g)
    def kalkulujopor(self):
        print(self.p/2 * self.v**2 * self.cd * self.area)
    def kalkulujajnstajn(self):
        print(self.m*self.c**2)
    def kalkulujprawopascala(self):
        print(self.fn/self.area)
    def kalkulujpewpew(self):
        print(self.m/2*self.v**2)
    def kalkulujgestosc(self):
        print(self.m/self.objetosc)
    def kalkulujwypornosc(self):
        print(self.dc*self.objetosc*self.g)

