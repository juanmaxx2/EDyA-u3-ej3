class Pais:
    __Nombre = None
    __Area = None

    def __init__(self, nombre, area):
        self.__Nombre = nombre
        self.__Area = area
    
    def __str__(self):
        return self.__Nombre + self.__Area

    def getNombre(self):
        return self.__Nombre
    
    def getArea(self):
        return self.__Area
    
    def setArea(self,x):
        self.__Area += x
    
    