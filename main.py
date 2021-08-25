from estudiante import Estudiante

def run ():
    alumnos = []
    calificaciones = {}
    while (True):

        print("""
        Bienvenido al  programa para calcular notas de estudiantes.
          1) para ingresar los nombres de los alumnos
          2) para ingresar las notas
          3) para imprimir alumno con su promedio
          4) salir

            Digita tu opcion:
        """)

        entrie = int(input())

        if entrie == 1:
            print(" ingresa la cantidad de alumnos: ")
            cant = int(input())
            
            for i in range(cant):
                
                name = input(f'ingresa el nombre del estudiante {i+1}: ')
                newperson = Estudiante(name)
                alumnos.append(newperson)

        if entrie == 2:

            for i in alumnos:
                print (f'ingrese las notas de {i.name}')
                nota1 = int(input("ingresa nota1: "))
                nota2 = int(input("ingresa nota2: "))
                nota3 = int(input("ingresa nota3: "))
                nota4 = int(input("ingresa nota4: "))
                nota5 = int(input("ingresa nota5: "))

                name = i.name
                notafinal = i.promedio(nota1,nota2,nota3,nota4,nota5)

                calificaciones[name] = notafinal

                
                      
        if entrie == 3:
            for alumno, nota in calificaciones.items():
                print (alumno + ' tuvo un promedio de :  ' + str(nota))
                   
                
        if entrie ==4:
            break

    
        
    

if __name__ == '__main__':
    run()