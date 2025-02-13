#Crear un programa que simule un juego de adivinanzas.
#Luego, debe pedir al usuario que adivine el número. El programa 
#El programa debe generar un número aleatorio entre 1 y 100.
#debe indicar si el número ingresado por el usuario es mayor o 
#menor que el número aleatorio. El juego termina cuando el usuario 
#adivina el número

import random


class AdivinaNumero(): # clase que contiene el codigo del juego
    def __init__(self,intentos):
        self.intentos = intentos
        self.numRandom = self.numeroRandom()
        

    def numeroRandom(self): # funsion para generar un numero random
        return random.randint(1,100)
    
    #funcion para inicializar los valores
    def reinicio(self):
        self.numeroRandom = self.numeroRandom()
        self.intentos = 3
        self.jugar()
    
    def menu(self): #funsion para crear un menu simple
        #mustra un menu para el jugador si decide salir o jugar de nuevo
        try:
            opcion = str(input("inserte opcion: \n[1]- para continuar\n[2]- para salir\n"))
            if opcion == "1":
                self.reinicio()
            
            elif opcion == "2":
                print("vuelve pronto")
                return
            
            else:
                print("Opcion invalidad")
                self.menu()
    
        except ValueError as e:
            print(f"Error: {e}")
    
    def jugar(self): #funcion que contiene la logica del juego
        #toda la logica funcional  y sostenible del juego
        try:
            while True:
                #guardamos en una variable el numero ingresado por el jugador
                numero = int(input("Ingrese un numero entre el 1 - 100: \n\n"))

                #comparamos si el numero es diferente al numero generado
                # y si el numero generado en mayor que el numero del jugador
                if self.numRandom != numero and self.numRandom > numero:
                    print(f"te quedan {self.intentos} intentos")
                    print(f"El numero es mayor")
                    print("________________________________\n")
                    
                
                elif self.numRandom != numero and self.numRandom < numero:
                    print(f"te quedan {self.intentos} intentos")
                    print(f"El numero es menor")
                    print("________________________________\n")
                
                
                else:
                    #si no se cumplen las otras condiciones el jugador gano
                    print(f"Ganastes el numero es {self.numRandom} y usted dijo {numero}\n")
                    self.menu()
                    return

                #por cada iteracion del while se resta en 1 a los numeros de intentos
                self.intentos -= 1

                #verificamos si los numeros de intentos llegaron a 0
                if self.intentos == 0:
                    print(f"Perdites te quedastes sin intentos, intentos: {self.intentos}, intentalo de nuevo")
                    print(f"El numero es {self.numRandom}")
                    print("________________________________\n")
                    self.menu()
                    return              

        except ValueError as e:
            print(f"Error: {e}")   
                   

if __name__ == "__main__":

    intentos = 3

    juego = AdivinaNumero(intentos)
    juego.jugar()

    
  
    