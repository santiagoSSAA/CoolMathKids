import salida as g
import importlib
import math

class CodeGenerator:
    def __init__(self, codeEmitter):
        self.ce = codeEmitter
        self.distance = 5
        pass

    def generate(self):
        # POSICIONAR TORTUGA EN POSICION HORIZONTAL
        self.degree = 0
        self.ce.rotate(90)

        importlib.reload(g)
        y = list(g.graficar())
        x = [i for i in range(1, len(y)+1)]
        #print(y,x)

        for i in range(-1, len(x) - 1):
            self.ce.println("setpensize 5")
            self.ce.penDown()
            pendiente = None
            coordenadas = None
            angulo = None
            if i == -1:
                pendiente = int((y[i+1])/(x[i+1]))
                coordenadas = [0, 0, x[i+1], y[i+1]]
                angulo = math.atan(pendiente)
                angulo = (180*angulo)/math.pi
                print("{} | {} | {}".format(pendiente, coordenadas, angulo))

            else:
                pendiente = int((y[i+1] - y[i])/(x[i+1] - x[i]))
                coordenadas = [x[i], y[i], x[i+1], y[i+1]]
                angulo = math.atan(pendiente)
                angulo = (180*angulo)/math.pi
                print("{} | {} | {}".format(pendiente, coordenadas, angulo))
            
            # ESTABLECER EL ANGULO EN TERMINOS DE LOGO
            if angulo > 0:
                self.degree = - int(angulo)
            elif angulo == 0:
                self.degree = 0
            elif angulo < 0:
                self.degree = - int(angulo)

            print(angulo)

            # DIBUJAR EL PUNTO
            self.ce.forward(1)
            self.ce.penUp()
            # DESPLAZAMIENTO
            self.ce.rotate(self.degree)
            self.ce.println("setpensize 1")
            self.ce.penDown()
            self.ce.forward(self.distance)
            # RECUPERAR EL SENTIDO HORIZONTAL
            self.ce.rotate((-1) * self.degree)
            # RETORNAR EL ANGULO A 0
            self.degree = 0

            # PONER ULTIMO PUNTO
            self.ce.println("setpensize 5")
            self.ce.forward(1)
            self.ce.println("setpensize 1")
            
            
            
        pass