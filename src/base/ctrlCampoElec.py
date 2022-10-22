from vectorCampoE import *

class ctrlVectorCampo():
    cargarEvaluar = []
    cargas = []
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
            aux = vectorCampoE([self.cargarEvaluar, self.cargas[i][0]],
                               self.cargas[i][1])
            self.vectorResultante[0] += aux.componentes[0]
            self.vectorResultante[1] += aux.componentes[1]
            i += 1

    def calAngulo(self):
        self.angulo = numpy.arctan(
            self.vectorResultante[1]/self.vectorResultante[0])

    def calMagnitud(self):
        aux = (self.vectorResultante[0]**2) + (self.vectorResultante[1]**2)
        self.magnitud = numpy.sqrt(aux)

    def vectorUnitario(self):
        return [self.vectorResultante[0]/self.magnitud, self.vectorResultante[1]/self.magnitud]

    def getMagnitud(self):
        return self.magnitud

    def getAngulo(self):
        return self.angulo * (180 / numpy.pi)

    def __str__(self) -> str:
        return "Vector resultante: ({}) i + ({}) j [N/C]\nMagnitud: {} [N/C]\nAngulo respecto al eje x: {}°".format(self.vectorResultante[0], self.vectorResultante[1], self.magnitud, self.getAngulo())


# pruebas
# cargaPrueba = [80 * (10**3), 80 * (10**3)]
# cargas = [[[-10 * (10**3), 30 * (10**3)], 0.8 * (10**3)], 
#           [[-40 * (10**3), -60 * (10**3)], -2.4 * (10**3)]]
# vectorResultante = ctrlVectorCampo(cargaPrueba, cargas)
# print(vectorResultante)
