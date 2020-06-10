import salida as g
import importlib
import math

class CodeGenerator:
    def __init__(self, codeEmitter):
        self.ce = codeEmitter
        pass

    def generate(self):
        # POSICIONAR TORTUGA EN POSICION HORIZONTAL
        self.degree = 0
        self.ce.rotate(90)

        importlib.reload(g)
        y = list(g.graficar())
        x = [i for i in range(1, len(y)+1)]

        for i in range(-1, len(x) - 1):
            pendiente = None
            coordenadas = None
            angulo = None
            if i == -1:
                pendiente = int((y[i+1])/(x[i+1]))
                #coordenadas = [0, 0, x[i+1], y[i+1]]
                angulo = math.atan(pendiente)
                angulo = (180*angulo)/math.pi
                angulo = int(angulo)
                #print("{} | {} | {}".format(pendiente, coordenadas, angulo))
                self.ce.penDown()
                self.ce.penUp
                self.ce.forward(30)

            else:
                pendiente = int((y[i+1] - y[i])/(x[i+1] - x[i]))
                #coordenadas = [x[i], y[i], x[i+1], y[i+1]]
                angulo = math.atan(pendiente)
                angulo = (180*angulo)/math.pi
                angulo = int(angulo)
                #print("{} | {} | {}".format(pendiente, coordenadas, angulo))
        pass