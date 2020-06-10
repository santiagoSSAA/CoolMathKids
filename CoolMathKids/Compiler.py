import sys
from plyplus import Grammar
from LogoCodeEmitter import LogoCodeEmitter
from PythonCodeEmitter import PythonCodeEmitter
import PythonCodeGenerator
import LogoCodeGenerator

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print()
        print("Error de entrada, escriba la llamada de la siguiente manera: ")
        print("python {} entrada.cmk salida.logo".format(sys.argv[0]))
        print()
    
    else:
        cmkFile = sys.argv[1]
        logoFile = sys.argv[2]
        inputCode = None
        arbol = None

        with open('gramatica.grm', 'r') as gramatica:
            with open(cmkFile, 'r') as inpt:
                inputCode = inpt.read()
                arbol = Grammar(gramatica, auto_filter_tokens=False).parse(inputCode)
                #print(arbol)
                #arbol.to_png_with_pydot(r'arbol.png')
                inpt.close()
            gramatica.close()
                
        with open("salida.py","w") as outpt_py:
            pythonCodeEmitter = PythonCodeEmitter(outpt_py)
            pythonCodeGenerator = PythonCodeGenerator.CodeGenerator(pythonCodeEmitter)
            pythonCodeGenerator.visit(arbol)
            outpt_py.flush()
            outpt_py.close()

        with open(logoFile, 'w') as outpt:     
            logoCodeEmitter = LogoCodeEmitter(outpt)
            logoCodeGenerator = LogoCodeGenerator.CodeGenerator(logoCodeEmitter)
            logoCodeGenerator.generate()
            outpt.close()
    pass