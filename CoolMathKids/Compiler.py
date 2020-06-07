import sys
from plyplus import Grammar
from LogoCodeEmitter import LogoCodeEmitter
#from CodeGenerator import CodeGenerator
from PythonCodeEmitter import PythonCodeEmitter
from PythonCodeGenerator import CodeGenerator

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print()
        print("Error de entrada, escriba la llamada de la siguiente manera: ")
        print("python {} entrada.cmk salida.logo".format(sys.argv[0]))
        print()
    
    else:
        cmkFile = sys.argv[1]
        logoFile = sys.argv[2]

        with open('gramatica.grm', 'r') as gramatica:
            with open(cmkFile, 'r') as inpt:
                with open(logoFile, 'w') as outpt:
                    inputCode = inpt.read()
                    arbol = Grammar(gramatica, auto_filter_tokens=False).parse(inputCode)
                    #print(arbol)
                    #arbol.to_png_with_pydot(r'arbol.png')
                    #logoCodeEmitter = LogoCodeEmitter(outpt)
                    pythonCodeEmitter = PythonCodeEmitter(outpt)
                    pythonCodeGenerator = CodeGenerator(pythonCodeEmitter)
                    pythonCodeGenerator.visit(arbol)

    pass