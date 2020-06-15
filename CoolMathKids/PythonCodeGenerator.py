import numpy as np
class CodeGenerator:
    def __init__(self, codeEmitter):
        self.ce = codeEmitter
        self.functionArguments = {}
        self.numero_identacion = 0
        self.intrincate = False
        self.nombre_funcion = None
    
    def visit(self, tree):
        method = False
        try:
            method = getattr(self, tree.head, None)
        except AttributeError as e:
            print(tree)
            print(e)
        
        if method:
            return method(tree)
        else:
            print("Method {} is not defined".format(method))

    def start(self, tree):
        codigo = tree.tail[0]
        self.ce.println("import numpy as np")
        self.ce.println("import math")
        self.ce.println("")
        self.visit(codigo)
        #self.ce.println("main")

    def codigo(self, tree):
        # visitar funcion
        for funcion in tree.tail[:-1]:
            self.visit(funcion)
        # visitar funcion graph
        graph = tree.tail[-1]
        self.visit(graph)
        #self.ce.println("algo")
    
    def funcion(self, tree):
        nombre = tree.tail[1]
        arguments = {}
        # En caso de querer ver el contenido
        #print("funcion*- {} -* {}".format(nombre,tree))
        
        # Recoger el numero de argumentos
        i = 3
        numArgs = 0
        while tree.tail[i] != ')':
            if tree.tail[i] != ',':
                arg = tree.tail[i]
                argPos = numArgs
                arguments[arg] = argPos
                numArgs = numArgs + 1
            i += 1
        self.functionArguments[nombre] = arguments
        self.nombre_funcion = nombre
        self.ce.print("def {}(".format(nombre))

        # Recorrer el contenido de las funciones
        for x in arguments.keys():
            self.ce.print("{}".format(x.tail[-1]))
        self.ce.println("):")
        i = i + 2
        body = tree.tail[i]
        if str(body.head) == "condicional":
            self.visit(body)
        else:
            body = self.visit(body)
            #print(body)
            body = str(body)
            self.numero_identacion += 4
            identacion = ""
            for i in range(self.numero_identacion):
                identacion = identacion + " "
            #print(body)
            if str(body) != "None":
                self.ce.println("{}return {}".format(identacion,body))
            self.numero_identacion -= 4
        #print(a)

    def graph(self,tree):
        funcioncall = tree.tail[2]
        inicio = tree.tail[4]
        final = tree.tail[6]
        n_puntos = tree.tail[8]
        #print(funcioncall, inicio, final)
        
        # ESCRIBIR LA FUNCION MAIN
        self.numero_identacion = 0
        identacion = ""
        for i in range(self.numero_identacion):
            identacion = identacion + " "
        self.ce.println("")
        #self.ce.println("function = np.frompyfunc({}, 1, 1)".format(str(funcioncall)))
        dominio = "function = np.frompyfunc({}, 1, 1)".format(str(funcioncall))

        # DEFINIMOS EL RANGO
        inicio = int(inicio.tail[0])
        final = int(final.tail[0])
        n_puntos = int(n_puntos.tail[0])
        rango1 = list(np.linspace(inicio,final,n_puntos))
        rango = []
        for i in rango1:
            rango.append(float("{:.3f}".format(float(i))))
        
        # CREAMOS LA FUNCION PARA GRAFICAR
        self.ce.println("def graficar():")
        self.ce.println("    {}".format(dominio))
        self.ce.println("    return function({})".format(rango))
        
        
        #print(rango)
        #print(inicio.tail[0], final.tail[0])
        #self.ce.println("print(function({}))".format(rango))

    def variable(self, tree):
        name = tree.tail[0]
        return name

    def numero(self, tree):
        value = tree.tail[0]
        return value

    def expuno(self, tree):
        #print(tree.tail)
        primer_expresion = self.visit(tree.tail[0])
        signo = tree.tail[1]
        segunda_expresion = self.visit(tree.tail[2])
        #print("{} {} {}".format(primer_expresion, signo, segunda_expresion))
        return("{} {} {}".format(primer_expresion, signo, segunda_expresion))

    def expdos(self, tree):
        #print(tree.tail)
        primer_expresion = self.visit(tree.tail[0])
        signo = tree.tail[1]
        if str(signo) == "^":
            signo = "**"
        segunda_expresion = self.visit(tree.tail[2])
        #print("{} {} {}".format(primer_expresion, signo, segunda_expresion))
        return("{} {} {}".format(primer_expresion, signo, segunda_expresion))

    def funcioncall(self,tree):
        functions = ["sqrt", "log", "sin", "cos", "asin", "acos", "factorial", "exp"]
        name = tree.tail[0]
        arg = None
        if str(tree.tail[-2].head) == "funcioncall":
            self.intrincate = True
        elif str(tree.tail[-2].head) in ["variable", "numero", "expuno","expdos"]:
            arg = self.visit(tree.tail[-2])
            namef = tree.tail[0]
            if self.nombre_funcion == namef:
                exp = "{}({})".format(namef,arg)
                return exp
            else:
                exp = "math.{}({})".format(namef,arg)
                return exp 
        if (self.intrincate == True):
            arg = self.visit(tree.tail[-2])
            if self.nombre_funcion == tree.tail[0]:
                exp = "{}({})".format(tree.tail[0],arg)
                return exp
            else:
                exp = "math.{}({})".format(tree.tail[0],arg)
                return exp
        else:
            arg = self.visit(tree.tail[-2])
            if name in functions:
                self.numero_identacion += 4
                identacion = ""
                for i in range(self.numero_identacion):
                    identacion = identacion + " "
                #print(arg)
                if self.nombre_funcion == name:
                    self.ce.println("{}return {}({})".format(identacion,name,arg))
                else:
                    self.ce.println("{}return math.{}({})".format(identacion,name,arg))
                self.numero_identacion -= 4       

    def parexpdos(self,tree):
        #print(tree.tail)
        if "-" in tree.tail or "+" in tree.tail:
            signo = tree.tail[0]
            pl = tree.tail[1]
            pr = tree.tail[-1]
            #print(tree.tail[2])
            exp = self.visit(tree.tail[2])
            #print(tree)
            #print(exp)
            #print("{} {} {} {}".format(signo, pl, exp, pr))
            return("({} {} {} {})".format(signo, pl, exp, pr))
        
        else:
            pl = tree.tail[0]
            pr = tree.tail[-1]
            #print(tree.tail[1])
            self.intrincate = True
            exp = self.visit(tree.tail[1])
            #print("{} {} {}".format(pl, exp, pr))
            return("{} {} {}".format(pl, exp, pr))

    def condicional(self,tree):
        id_condicional = tree.tail[0]
        pl = tree.tail[1]
        pr = tree.tail[3]
        expresion_logica = self.visit(tree.tail[2])

        # ESTABLECEMOS LA IDENTACION
        if self.intrincate == False:
            self.numero_identacion += 4
        
        identacion = ""
        for i in range(self.numero_identacion):
            identacion = identacion + " "

        #print("{}hola".format(identacion))

        # ESCRIBIMOS EL CONDICIONAL
        self.ce.println("{}{} {} {} {}:".format(identacion, id_condicional, pl, expresion_logica, pr))
        #print("{} {} {} {}:".format(id_condicional, pl, expresion_logica, pr))
        
        # ENTRAMOS EN EL CONDICIONAL
        body_if = tree.tail[5]
        #print(body_if.head)
        
        if str(body_if.head) not in ["condicional", "funcioncall"]:
            self.numero_identacion += 4
            identacion = ""
            for i in range(self.numero_identacion):
                identacion = identacion + " "

        contenido_if = self.visit(body_if)
        if str(contenido_if) != "None":
            self.ce.println("{}return {}".format(identacion,contenido_if))

        if str(body_if.head) not in ["condicional", "funcioncall"]:
            self.numero_identacion -= 4

        #lll = tree.tail[4]
        #rll = tree.tail[6] 
        #print("{} {} {}".format(lll, body_if, rll))
        
        # ENTRAMOS EN EL ELSE (SI EXISTE)
        if "else" in tree.tail:
            identacion = ""
            for i in range(self.numero_identacion):
                identacion = identacion + " "
            else_expresion = tree.tail[7]

            self.ce.println("{}{}:".format(identacion,else_expresion))

            if str(tree.tail[9].head) not in ["condicional", "funcioncall"]:
                self.numero_identacion += 4

            body_else = self.visit(tree.tail[9])
            if body_else != None:
                identacion = ""
                for i in range(self.numero_identacion):
                    identacion = identacion + " "
                self.ce.println("{}return {}".format(identacion,body_else))
            
            if str(tree.tail[9].head) not in ["condicional", "funcioncall"]:
                self.numero_identacion -= 4
            #lll2 = tree.tail[8]
            #rll2 = tree.tail[-1]
            #print(tree.tail[9])
            #print("{} {} {} {}".format(else_expresion, lll2, body_else, rll2))

    def parexp(self,tree):
        #print("Parexpr *- {}".format(tree))
        exp = self.visit(tree.tail[1])
        #print(exp)
        return ("( {} )".format(exp))

    def expresionlogica(self,tree):
        #print(str(tree.tail[0]))
        primer_expresion = self.visit(tree.tail[0])
        #print(primer_expresion)
        signo = tree.tail[1]
        segunda_expresion = self.visit(tree.tail[2])
        return("{} {} {}".format(primer_expresion, signo, segunda_expresion))