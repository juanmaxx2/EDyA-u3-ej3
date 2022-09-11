from listaEncadenadaPorContenido import ListaEncadenadaPorContenido
from pais import Pais
import csv 

if __name__ == '__main__':
    unaLista = ListaEncadenadaPorContenido()
    archivo = open('IncendiosForestales.csv')
    reader = csv.reader(archivo, delimiter = ';')
    bol=True
    for fila in reader:
        if bol:
            bol = False
        else:
            unPais = Pais(fila[3], float(fila[6]))
            unaLista.Insertar(unPais)
    unaLista.recorrer()