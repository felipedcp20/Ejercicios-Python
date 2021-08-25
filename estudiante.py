class Estudiante:

    def __init__(self,name):
        self.name = name

    def promedio(self,not1,not2,not3,not4,not5):
        suma = not1+not2+not3+not4+not5
        promedio = suma/5
        return  promedio
        