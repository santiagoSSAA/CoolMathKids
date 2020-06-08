class CodeGenerator:
    def __init__(self, codeEmitter):
        self.ce = codeEmitter
        self.condCounter = 0
        self.functionArguments = {}
        self.numero_identacion = 0
    
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
    
    # pendiente
    def funcion(self, tree):
        nombre = tree.tail[1]
        arguments = {}
        # En caso de querer ver el contenido
        #print("funcion*- {} -* {}".format(nombre,tree))
        
        # Recoger el numero de argumentos
        i = 3
        numArgs = 0
        while tree.tail[i] != ')':
            if tree.tail != ',':
                arg = tree.tail[i]
                argPos = numArgs
                arguments[arg] = argPos
                numArgs = numArgs + 1
            i += 1
        self.functionArguments[nombre] = arguments
        self.currentfuncion = nombre
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
            self.ce.println("{}return {}".format(identacion,body))
            self.numero_identacion -= 4
        #print(a)

    def graph(self,tree):
        funcioncall = tree.tail[2]
        inicio = tree.tail[4]
        final = tree.tail[6]
        #print(funcioncall, inicio, final)
        
        # ESCRIBIR LA FUNCION MAIN
        self.numero_identacion = 0
        identacion = ""
        for i in range(self.numero_identacion):
            identacion = identacion + " "
        self.ce.println("")
        self.ce.println("function = np.frompyfunc({}, 1, 1)".format(str(funcioncall)))

        # DEFINIMOS EL RANGO
        inicio = int(inicio.tail[0])
        final = int(final.tail[0])
        rango = [i for i in range(int(str(inicio)),int(str(final))+1)]
        #print(rango)
        #print(inicio.tail[0], final.tail[0])
        self.ce.println("print(function({}))".format(rango))

    # pendiente
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

    #pendiente
    def funcioncall(self,tree):
        name = tree.tail[0]
        args = [x for x in tree.tail[2:-1] if x != ',']
        #print(args)

    def parexpdos(self,tree):
        signo = tree.tail[0]
        pl = tree.tail[1]
        pr = tree.tail[-1]
        #print(tree.tail[2])
        exp = self.visit(tree.tail[2])
        #print(tree)
        #print(exp)
        #print("{} {} {} {}".format(signo, pl, exp, pr))
        return("{} {} {} {}".format(signo, pl, exp, pr))

    def condicional(self,tree):
        id_condicional = tree.tail[0]
        pl = tree.tail[1]
        pr = tree.tail[3]
        expresion_logica = self.visit(tree.tail[2])

        # ESTABLECEMOS LA IDENTACION
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
        #print(body_if)
        
        self.numero_identacion += 4
        identacion = ""
        for i in range(self.numero_identacion):
            identacion = identacion + " "

        contenido_if = self.visit(body_if)
        self.ce.println("{}return {}".format(identacion,contenido_if))

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

            if str(tree.tail[9].head) != "condicional":
                self.numero_identacion += 4

            body_else = self.visit(tree.tail[9])
            if body_else != None:
                identacion = ""
                for i in range(self.numero_identacion):
                    identacion = identacion + " "
                self.ce.println("{}return {}".format(identacion,body_else))
                self.numero_identacion -= 4
            #lll2 = tree.tail[8]
            #rll2 = tree.tail[-1]
            #print(tree.tail[9])
            #print("{} {} {} {}".format(else_expresion, lll2, body_else, rll2))


    def parexp(self,tree):
        #print("Parexpr *- {}".format(tree))
        exp = self.visit(tree.tail[1])
        return ("( {} )".format(exp))

    def expresionlogica(self,tree):
        #print(str(tree.tail[0]))
        primer_expresion = self.visit(tree.tail[0])
        #print(primer_expresion)
        signo = tree.tail[1]
        segunda_expresion = self.visit(tree.tail[2])
        return("{} {} {}".format(primer_expresion, signo, segunda_expresion))