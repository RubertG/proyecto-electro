import matplotlib.pyplot as plt
from ctrlCampoElec import *


def graficarCampoResultante(principal, posiciones):
    prinX = principal[0]
    prinY = principal[1]
    colores = ['b', 'y', 'm', 'k', 'g']
    i = 0

    plt.plot(prinX, prinY, 'ok', color="r",
             label="Carga de prueba")

    plt.axvline(prinX, color="k")
    plt.axhline(prinY, color="k")

    maxX = prinX
    minX = prinX
    maxY = prinY
    minY = prinY

    for pos in posiciones:
        plt.plot(pos[0][0], pos[0][1], 'ok', color=colores[i],
                 label="Q{} = {} [C]".format(i+2, pos[1]))
        if (maxX < pos[0][0]):
            maxX = pos[0][0]
        elif (minX > pos[0][0]):
            minX = pos[0][0]

        if (maxY < pos[0][1]):
            maxY = pos[0][1]
        elif (minY > pos[0][1]):
            minY = pos[0][1]
        i += 1

    fuerza = ctrlVectorCampo(principal, posiciones)
    fuerX = fuerza.vectorUnitario()[0]
    fuerY = fuerza.vectorUnitario()[1]

    if (fuerX < 0 ):
        fuerX *= (10**len(str(maxY)) - 6)
    else:
        fuerX *= (10**len(str(maxY)) - 5)
    if (fuerY < 0):
        fuerY *= (10**len(str(maxY)) - 6)
    else:
        fuerY *= (10**len(str(maxY)) - 5)

    plt.quiver(prinX, prinY, fuerX, fuerY, color='r', scale_units="xy",
               angles="xy", scale=1, label="Fuerza total")

    plt.legend(bbox_to_anchor=(0.37, 1))
    plt.xlim(minX - (10**len(str(maxY)) - 6), maxX + (10**len(str(maxY)) - 5))
    plt.ylim(minY - (10**len(str(maxY)) - 6), maxY + (10**len(str(maxY)) - 5))
    plt.grid(b=True, which='major')
    plt.title('Grafica vector resultante campo electrico')
    plt.show()


principal = [8 , 8 ]
posiciones = [[[-1 , 3 ], 0.8 * (10**3)]]
graficarCampoResultante(principal, posiciones)
