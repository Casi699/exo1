print("********************PERSONNE**************************")
class Personne:
    def __init__(self, nom, prenom, cin):
        self.nom = str(nom)
        self.prenom = str(prenom)
        self.cin = str(cin)

    def ToString(self):
        print("NOM******PRENOM********CIN\t\n",self.nom," ",self.prenom," ",self.cin)



g = Personne("keita", "moussa", "444")
g.ToString()
print("*****************VACCIN*****************************")

class Vaccin(Personne):
    def __init__(self, cod, nom, duree):
        self.__code = cod
        self.__nom = nom
        self.__duree = duree

    def const_recopie(self, cod, nom, duree):
        self.__code = cod
        self.__nom = nom
        self.__duree = duree

    def ToString(self):
        super().ToString
        print("code**nom**duree\t\n", self.__code,
              self.__nom,
              self.__duree)

v = Vaccin("fv45", "variole", 5)
v.ToString()
v.const_recopie(44, "DDD", 888)
v.ToString()

print("**********************VACCINE************************")
class vaccine(Personne):
    def __init__(self,nom,prenom,cin,codevaccin,datevaccin):
        super().__init__(nom,prenom,cin)
        self.__codevacc=codevaccin
        self.__datevacc= datevaccin
        
    def getCodevacc(self):
        return self.__codevacc
    def setCodevacc(self,codvacc):
        self.__codevacc=codvacc

    def getDatevacc(self):
        return self.__datevacc
    def setDatevacc(self,datevacc):
        self.__datevacc=datevacc

    def ToString(self):
        super().ToString()
        print("code vaccin date vaccin\t\n",self.__codevacc," ",self.__datevacc,)
        #print("\n",self.__datevacc)
        #print("**CODE VACCINATION**DATE VACCINATION\t\n",self.__codevacc,self.__datevacc)


x=vaccine("berthe","casi",'3',"dd03","28/09/2021")
x.ToString()
print("**********************************************")
