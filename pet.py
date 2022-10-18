class Pet:
    def __init__(self, nom, typeanimal, age):
        self.__name = nom
        self.__typAnimal = typeanimal
        self.__age = age

    def setName(self, nom):
        self.__name = nom

    def getName(self):
        return self.__name

    def setTypeanimal(self, typeanimal):
        self.__typAnimal = typeanimal

    def getTypeanimal(self, typeanimal):
        return self.__typAnimal

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age
    def info(self):
        print("nom  type animal age\t\n",self.__name,
        self.__typAnimal,
        self.__age)
a = Pet("boby", "rapace", 3)
print(a.getAge())
a.info()
