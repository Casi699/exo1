class table:
    def __init__(self, prix, nbtable):
        self.__prixfab = prix
        self.__stock = nbtable
        self.reference = "QUALITE SUP"
        self.tabmatiere = "AAAAAAAA"
        self.long = 10
        self.larg = 15
        self.poids = 34
        self.prix_vent = 15000

    def setPrixfab(self, p):
        self.__prixfab = p

    def getPrixfab(self):
        return self.__prixfab

    def setNbstock(self, stock):
        self.__stock = stock

    def getNbstock(self):
        return self.__stock

    def Gain(self):
        g = self.__stock*self.prix_vent
        print("gain prevu par rapprot au stock est:", g)

    def getInfo(self):
        print("PRIX FRABRIC**STOCK**REFRENCE**MATIERE TABLE**LONG**LARG**POIDS**PRIX VENTE\t\n",self.__prixfab, self.__stock,self.reference,self.tabmatiere,
             self.long, self.larg,self.poids,self.prix_vent)

a = table(22222, 23)
a.getInfo()
a.Gain()
print(a.getPrixfab())
