# Sacar el vector resultante con varias fuerzas
from vectorFuerza import *

class ctrlVectorFuerza():
    cargarEvaluar = []
    cargas = [0, 0, 0]
    vectorResultante = [0, 0]
    angulo = 0
    magnitud = 0

    def __init__(self, carEvaluar, car) -> None:
        self.cargarEvaluar = carEvaluar
        self.cargas = car
        self.calVectorResultante()
        self.calMagnitud()
        self.calAngulo()

    def calVectorResultante(self):
        i = 0
        while (i < len(self.cargas)):
            aux = vectorFuerza([self.cargarEvaluar[0], self.cargas[i][0]],
                               [self.cargarEvaluar[1], self.cargas[i][1]])
            self.vectorResultante[0] += aux.componentes[0]
            self.vectorResultante[1] += aux.componentes[1]
            i += 1

    def calAngulo(self):
        self.angulo = numpy.arctan(
            self.vectorResultante[1]/self.vectorResultante[0])

    def calMagnitud(self):
        aux = (self.vectorResultante[0]**2) + (self.vectorResultante[1]**2)
        self.magnitud = numpy.sqrt(aux)

    def getMagnitud(self):
        return self.magnitud

    def getAngulo(self):
        return self.angulo * (180 / numpy.pi)

    def vectorUnitario(self):
        return [self.vectorResultante[0]/self.magnitud, self.vectorResultante[1]/self.magnitud]
    

    def __str__(self) -> str:
        return "Vector resultante: ({}) i + ({}) j [N]\nMagnitud: {} [N]\nAngulo respecto al eje x: {}°".format(self.vectorResultante[0], self.vectorResultante[1], self.magnitud, self.getAngulo())


# pruebas
# cargaPrueba = [[60, -20], 20 * (10**-3)]
# cargas = [[[-120, -90], 90 * (10**-3)], 
#           [[-70, 60], -60 * (10**-3)]]
# vectorResultante = ctrlVectorFuerza(cargaPrueba, cargas)
#print(vectorResultante)
