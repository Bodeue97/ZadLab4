class Robaczek:
    xaxis = 0
    yaxis = 0
    krok = 0

    def __init__(self, x=0, y=0, step=1):
        self.xaxis=x
        self.yaxis=y
        self.krok=step

    def goUp(self, ile):
        self.yaxis+=(ile*self.krok)
    def goDown(self, ile):
        self.yaxis-=(ile*self.krok)
    def goRight(self, ile):
        self.xaxis +=(ile*self.krok)
    def goLeft(self, ile):
        self.xaxis -=(ile*self.krok)
    def whereAmI(self):
        print("Wspolrzedna x: " + str(self.xaxis) + " Wspolrzedna y: " + str(self.yaxis))