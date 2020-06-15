import salida as g
import importlib
import math

class CodeGenerator:
    def __init__(self, codeEmitter):
        self.ce = codeEmitter
        self.distance = 40
        pass

    def generate(self):
        # DIBUJAR PLANO
        self.ce.println("setscrunch 0.5 0.5")

        self.ce.rotate(270)
        self.ce.penUp()
        self.ce.forward(1000)
        self.ce.rotate(270)
        self.ce.forward(400)
        self.ce.rotate(270)
        self.ce.penDown()

        # POSICIONAR TORTUGA EN POSICION HORIZONTAL
        self.degree = 0
        #self.ce.rotate(90)

        importlib.reload(g)
        y = list(g.graficar())
        x = [i for i in range(1, len(y)+1)]
        #print(y,x)

        self.ce.println("window")
        self.ce.forward(1400)
        self.ce.rotate(180)
        self.ce.forward(1800)
        self.ce.rotate(180)
        self.ce.forward(450)

        self.ce.rotate(90)
        self.ce.forward(150)
        self.ce.rotate(180)
        self.ce.forward(450)
        self.ce.rotate(180)
        self.ce.forward(300)
        self.ce.rotate(180)
        self.ce.rotate(90)

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
                #print("{} | {} | {}".format(pendiente, coordenadas, angulo))

            else:
                pendiente = int((y[i+1] - y[i])/(x[i+1] - x[i]))
                coordenadas = [x[i], y[i], x[i+1], y[i+1]]
                angulo = math.atan(pendiente)
                angulo = (180*angulo)/math.pi
                #print("{} | {} | {}".format(pendiente, coordenadas, angulo))
            
            # ESTABLECER EL ANGULO EN TERMINOS DE LOGO
            if angulo > 0:
                self.degree = - int(angulo)
            elif angulo == 0:
                self.degree = 0
            elif angulo < 0:
                self.degree = - int(angulo)

            #print(angulo)

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