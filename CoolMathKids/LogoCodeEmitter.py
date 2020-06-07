class LogoCodeEmitter(object):
    def __init__(self, file):
        self.file = file
        pass
    
    def println(self, str):
        print(str, file=self.file)

    def forward(self, unit):
        if isinstance(unit, int) or isinstance(unit, float):
            self.println("fd {}".format(unit))
        else:
            self.println("Error in Forward instruction: Unit {} is not a number or has a comma")
        pass

    def rotate(self, degree):
        if isinstance(degree, int) or isinstance(degree, float):
            self.println("rt {}".format(degree))
        else:
            self.println("Error in Rotate instruction: degree {} is not a number or has a comma")
        pass

    def penUp(self):
        self.println("pu")
        pass

    def penDown(self):
        self.println("pd")