class Celda:
    __sig = None
    __item = None

    def __init__(self, item = None):
        self.__sig = None
        self.__item = item

    def setItem(self, item):
        self.__item = item
    
    def setSig(self, celda):
        self.__sig = celda

    def getItem(self):
        return self.__item
    
    def getSig(self):
        return self.__sig

class ListaEncadenadaPorContenido:
    __cant = None
    __ul = None
    __cabeza = None

    def __init__ (self):
        self.__cabeza = None
        self.__cant = -1
        self.__ul = None

    def vacio(self):
        return self.__cant == -1

    def chequear(self, x):
        if not self.vacio():
            aux = self.__cabeza
            bol = False
            bol1 = False
            while not bol:
                if aux.getItem().getNombre() == x.getNombre():
                    bol1 = True
                    bol = True
                if aux.getSig() == None:
                    bol = True
                if not bol1:
                    aux = aux.getSig()
            if bol1:
                ret=aux
            else:
                ret=False
        else:
            ret=False
        return ret

    def Insertar(self, x):
        chec = self.chequear(x)
        if chec == False:
            unaCelda = Celda(x)
            if self.__cabeza == None:
                self.__cabeza = unaCelda
                self.__ul = unaCelda
            else:
                if self.__cabeza.getItem().getArea() < x.getArea():
                    unaCelda.setSig(self.__cabeza)
                    self.__cabeza = unaCelda
                else:
                    aux = self.__cabeza
                    while aux.getSig() != None and aux.getSig().getItem().getArea() > x.getArea():
                        aux  = aux.getSig()
                    unaCelda.setSig(aux.getSig())
                    aux.setSig(unaCelda)
                    if unaCelda.getSig() == None:
                        self.__ul = unaCelda
            self.__cant += 1
            return unaCelda.getItem()
        else:
            chec.getItem().setArea(x.getArea())
            if chec != self.__cabeza:
                if self.__cabeza.getItem().getArea() < chec.getItem().getArea():
                    if self.__cabeza.getSig().getItem().getNombre()==chec.getItem().getNombre():
                        self.__cabeza.setSig(chec.getSig())
                    chec.setSig(self.__cabeza)
                    self.__cabeza = chec
                else:
                    aux = self.__cabeza
                    auxArea = aux.getItem().getArea()
                    checArea = chec.getItem().getArea()
                    while aux.getSig() != None and auxArea > checArea:                        
                        aux1 = aux
                        aux  = aux.getSig()
                        auxArea = aux.getItem().getArea()
                    aux1.setSig(chec)
                    
                    if aux.getItem().getNombre() != chec.getItem().getNombre():
                        aux.setSig(chec.getSig())
                        chec.setSig(aux)
                    if chec.getSig() == None:
                        self.__ul = chec


    def recorrer (self):
        aux = self.__cabeza
        bol = False
        while not bol:
            print('Nombre:{} Area:{}'.format(aux.getItem().getNombre(), aux.getItem().getArea()))
            if aux.getSig() == None:
                bol = True
            aux = aux.getSig()