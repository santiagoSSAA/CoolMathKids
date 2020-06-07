class PythonCodeEmitter:
    def __init__(self, file):
        self.file = file
        pass
    
    def println(self, str):
        print(str, file=self.file)

    def print(self, str):
        print(str, end=" ", file=self.file)