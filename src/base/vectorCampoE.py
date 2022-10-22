import numpy

class vectorCampoE():
    posicion = []
    componentes = []
    carga = 0
    direccion = [1, 1]
    distancia = 0
    angulo = 0
    magnitud = 0
    distanciaX = 0
    distanciaY = 0

    def __init__(self, pos, car):
        self.posicion = pos
        self.carga = car
        self.calDistanciasXY()
        self.calAngulo()
        self.calDistacia()
        self.calMagnitud()
        self.calDireccion()
        self.calComponentes()

    def calDistanciasXY(self):
        if(self.posicion[0][0] < 0 and self.posicion[1][0] < 0):
            self.distanciaX = abs(
                abs(self.posicion[0][0]) - abs(self.posicion[1][0]))
        elif(self.posicion[0][0] < 0 or self.posicion[1][0] < 0):
            self.distanciaX = abs(
                abs(self.posicion[0][0]) + abs(self.posicion[1][0]))
        else:
            self.distanciaX = abs(
                abs(self.posicion[0][0]) - abs(self.posicion[1][0]))

        if(self.posicion[0][1] < 0 and self.posicion[1][1] < 0):
            self.distanciaY = abs(
                abs(self.posicion[0][1]) - abs(self.posicion[1][1]))
        elif(self.posicion[0][1] < 0 or self.posicion[1][1] < 0):
            self.distanciaY = abs(
                abs(self.posicion[0][1]) + abs(self.posicion[1][1]))
        else:
            self.distanciaY = abs(
                abs(self.posicion[0][1]) - abs(self.posicion[1][1]))

    def calAngulo(self):
        if(self.distanciaX == 0):
            self.angulo = (numpy.pi / 2)
        elif(self.distanciaY == 0):
            self.angulo = 0
        else:
            self.angulo = numpy.arctan(self.distanciaY/self.distanciaX)

    def calDistacia(self):
        self.distancia = (self.distanciaX**2) + (self.distanciaY**2)

    def calMagnitud(self):
        ke = 8.9875*(10**9)
        self.magnitud = ke * (abs(self.carga) / self.distancia)

    def calDireccion(self):
        if(self.posicion[0][0] > self.posicion[1][0]):
            self.direccion[0] = -1
        if(self.posicion[0][1] > self.posicion[1][1]):
            self.direccion[1] = -1
        if(self.carga > 0):
            self.direccion[0] *= -1
            self.direccion[1] *= -1

    def calComponentes(self):
        if(self.angulo == numpy.pi/2):
            self.componentes = [
                0, (self.magnitud * numpy.sin(self.angulo)) * self.direccion[1]]
        else:
            self.componentes = [
                (self.magnitud * numpy.cos(self.angulo)) * self.direccion[0], (self.magnitud * numpy.sin(self.angulo)) * self.direccion[1]]
            
    def getAngulo(self):
        return self.angulo * (180 / numpy.pi)

    def __str__(self) -> str:
        return 'Coordenadas: [{}, {}], [{}, {}]\nAngulo: {:.4f}°\nMagnitud: {} [N/C]\nComponentes: ({}i) + ({}j) [N/C]'.format(self.posicion[0][0], self.posicion[0][1], self.posicion[1][0], self.posicion[1][1], self.getAngulo(), self.magnitud, self.componentes[0], self.componentes[1])


# # pruebas
# prueba = vectorCampoE(
#     [[80, 80], [-40, -60]], -2.4*(10**3))
# #print(prueba)
