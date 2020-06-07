from plyplus import Grammar
from MIPSCodeEmitter import MIPSCodeEmitter
from CodeGenerator import CodeGenerator
import sys

if __name__ == '__main__':
    #print(sys.argv, type(sys.argv))

    """Confirmar que la expresión de inicialización del código está
    bien escrita. sys.argv contiene los argumentos llamados en la
    consola de código después de escribir la palabra Python. Por ejemplo,
    python helloworld.py , sys.argv será una lista que contiene una
    string que dice "helloworld.py", y así sucesivamente con los
    argumentos que hayan."""
    if len(sys.argv) != 3:
        """Si entra aquí, el código está mal escrito en la consola de 
        código-"""
        print("Example call: {} input.kl output.asm".format(sys.argv[0]))
    else:
        """si entra aquí, el código escrito en la consola estuvo bien
        escrito."""
        sourceFile = sys.argv[1]
        targetFile = sys.argv[2]
        """Se lee el archivo que contiene la gramática formal de
        kaleidoscope."""
        with open('Kaleidoscope.g', 'r') as grm:
            """Se lee el archivo que contiene el código de alto nivel"""
            with open(sourceFile, 'r') as sc:
                """Se escribe (o se crea si no existe) sobre el archivo
                que contendrá el código generado de bajo nivel por el
                compilador"""
                with open(targetFile, 'w') as oc:
                    """Se crea una variable que contiene todo el texto
                    del sourcefile (HLL)"""
                    scode = sc.read()
                    
                    ast = Grammar(grm, auto_filter_tokens=False).parse(scode)
                    #ast.to_png_with_pydot('ast.png')
                    #TDVisitor(ast)
                    #ce = MIPSCodeEmitter(oc)
                    #cg = CodeGenerator(ce, True)
                    #cg.visit(ast)
                    #print(ast)
