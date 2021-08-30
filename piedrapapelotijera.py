import random

def piedrapapeltijera (player, cpu):

        options ={1:"piedra",2:"papel",3:"tijera"}

       
        if player != cpu:
            if player ==1 and cpu ==3:
                print (f'el JUGADOR saco: {options.get(1)} y la CPU: {options.get(3)}')
                return 1,f'gano el jugador con {options.get(1)}'
            if player ==1 and cpu ==2:
                print (f'el JUGADOR saco: {options.get(1)} y la CPU: {options.get(2)}')
                return 2,f'gano la cpu con {options.get(2)}'
            if player ==2 and cpu == 1:
                print (f'el JUGADOR saco: {options.get(2)} y la CPU: {options.get(1)}')
                return 1,f'gano el jugador con {options.get(2)}'
            if player ==2 and cpu ==3:
                print (f'el JUGADOR saco: {options.get(2)} y la CPU: {options.get(3)}')
                return 2,f'gano la cpu con {options.get(3)}'
            if player ==3 and cpu ==1:
                print (f'el JUGADOR saco: {options.get(3)} y la CPU: {options.get(1)}')
                return 2,f'gano la cpu con {options.get(1)}'
            if player ==3 and cpu ==2:
                print (f'el JUGADOR saco: {options.get(3)} y la CPU: {options.get(2)}')
                return 1,f'gano el jugador con {options.get(3)}'
        else:
            return 0,f'empataron con Jugador: {options.get(player)}  cpu: {options.get(cpu)}'
            
   

def run ():
    
    CountPlayer=0
    CountCpu=0
    CountTie=0
    
        
    while(True):
    
        print("""
        Juego de piedra papel o tijera:
        Escoge una de las opciones:
        1) piedra
        2) papel
        3) tijera
        4) Salir del juego""")
        option = int(input("ingresa una opcion: "))
        if option ==4:
            break
                   
        AleatoryNumber = random.randint(1,3)
        retur = piedrapapeltijera(option,AleatoryNumber)
        
        if retur[0] == 1:
            CountPlayer +=1
        elif retur[0] == 2:
            CountCpu +=1
        elif retur[0] ==0:
            CountTie +=1

        print(retur[1])
        print(f'VECES GANADAS: JUGADOR: {CountPlayer} CPU: {CountCpu} EMPATES: {CountTie}')
        
        
      
                   
if __name__ == '__main__':
    run()