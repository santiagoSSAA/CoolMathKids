class CodeGenerator:
    def __init__(self, codeEmitter):
        self.ce = codeEmitter
        self.condCounter = 0
        self.functionArguments = {}
        self.numero_identacion = 0
        pass
    
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
        pass

    def start(self, tree):
        codigo = tree.tail[0]
        self.visit(codigo)
        #self.ce.println("main")
        pass

    def codigo(self, tree):
        # visitar funcion
        for funcion in tree.tail[:-1]:
            self.visit(funcion)
        # visitar funcion graph
        graph = tree.tail[-1]
        self.visit(graph)
        #self.ce.println("algo")
        pass
    
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
        print(body)
        self.visit(body)
        #print(a)

    def graph(self,tree):
        funcioncall = tree.tail[2]
        inicio = tree.tail[4]
        final = tree.tail[6]
        #print(funcioncall, inicio, final)
        pass
    
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
        pass

    def expdos(self, tree):
        #print(tree.tail)
        primer_expresion = self.visit(tree.tail[0])
        signo = tree.tail[1]
        segunda_expresion = self.visit(tree.tail[2])
        #print("{} {} {}".format(primer_expresion, signo, segunda_expresion))
        return("{} {} {}".format(primer_expresion, signo, segunda_expresion))
        pass

    #pendiente
    def funcioncall(self,tree):
        name = tree.tail[0]
        args = [x for x in tree.tail[2:-1] if x != ',']
        #print(args)
        pass

    def parexpdos(self,tree):
        signo = tree.tail[0]
        pl = tree.tail[1]
        pr = tree.tail[-1]
        #print(tree.tail[2])
        exp = self.visit(tree.tail[2])
        #print("{} {} {} {}".format(signo, pl, exp, pr))
        return("{} {} {} {}".format(signo, pl, exp, pr))
        pass

    def condicional(self,tree):
        id_condicional = tree.tail[0]
        pl = tree.tail[1]
        pr = tree.tail[3]
        expresion_logica = self.visit(tree.tail[2])
        #print("{} {} {} {}:".format(id_condicional, pl, expresion_logica, pr))
        lll = tree.tail[4]
        rll = tree.tail[6] 
        body_if = self.visit(tree.tail[5])
        #print("{} {} {}".format(lll, body_if, rll))
        if "else" in tree.tail:
            else_expresion = tree.tail[7]
            lll2 = tree.tail[8]
            rll2 = tree.tail[-1]
            body_else = self.visit(tree.tail[9])
            #print(tree.tail[9])
            #print("{} {} {} {}".format(else_expresion, lll2, body_else, rll2))

        pass

    def parexp(self,tree):
        #print("Parexpr *- {}".format(tree))
        exp = self.visit(tree.tail[1])
        return ("( {} )".format(exp))
        pass

    def expresionlogica(self,tree):
        primer_expresion = self.visit(tree.tail[0])
        signo = tree.tail[1]
        segunda_expresion = self.visit(tree.tail[2])
        return("{} {} {}".format(primer_expresion, signo, segunda_expresion))
        pass