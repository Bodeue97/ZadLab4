class CiagiArytm:
    a1 = 0
    rozn = 0
    ile = 0
    an = 0
    wyrazyCiagu = [a1]
    for x in range (ile):
        an = a1+rozn
        wyrazyCiagu.append(an)
        a1 = an


    def wyswietlElementy(self):
        print(self.wyrazyCiagu)
    def pobierzElem(self, *elementy):

        pobraneElementy = []
        pobraneElementy.append([x for x in elementy])
        return pobraneElementy
    def pobierzParametry(self, a1, rozn, ile):
        self.a1 = a1
        self.rozn=rozn
        self.ile = ile
    def sumaEl(self):

        suma=0
        for x in self.wyrazyCiagu:
            suma +=x
    def






