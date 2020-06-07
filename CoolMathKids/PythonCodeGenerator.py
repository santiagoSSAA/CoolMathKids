class CodeGenerator:
    def __init__(self, codeEmitter):
        self.ce = codeEmitter
        self.condCounter = 0
        self.functionArguments = {}
        self.functions = []
        self.currentfuncion = ""
        pass
    
    def visit(self, tree):
        method = getattr(self, tree.head, None)
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
        for x, i in zip(arguments.keys(), range(1,len(arguments.keys())+1)):
            self.ce.print("{},".format(x))
        self.ce.println("):")
        i = i + 2
        print(tree.tail[i])
        body = tree.tail[i]
        self.visit(body)

    def graph(self,tree):
        funcioncall = tree.tail[2]
        inicio = tree.tail[4]
        final = tree.tail[6]
        #print(funcioncall, inicio, final)
        pass
    
    # pendiente
    def variable(self, tree):
        name = tree.tail[0]
        pos = self.functionArguments[self.currentfuncion][name]
        pass

    def numero(self, tree):
        value = tree.tail[0]
        return value

    def expuno(self, tree):
        pass

    def expdos(self, tree):
        pass

    #pendiente
    def funcioncall(self,tree):
        name = tree.tail[0]
        args = [x for x in tree.tail[2:-1] if x != ',']
        #print(args)
        pass

    def parexpdos(self,tree):
        pass

    def condicional(self,tree):
        #print(tree.tail)
        return 2
        pass

    def parexp(self,tree):
        #print("Parexpr *- {}".format(tree))
        self.visit(tree.tail[1])
        pass

    def expresionlogica(self,tree):
        #print(tree.tail)
        pass