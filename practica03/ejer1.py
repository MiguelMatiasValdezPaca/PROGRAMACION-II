import random

# Clase padre
class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0

    def reiniciaPartida(self):
        print("Nueva partida iniciada")
    
    def actualizaRecord(self):
        self.record += 1
        print("Record actualizado:", self.record)

    def quitaVida(self):
        self.numeroDeVidas -= 1
        print("Te quedan", self.numeroDeVidas, "vidas")
        
        if self.numeroDeVidas > 0:
            return True
        else:
            print("Game Over")
            return False


class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("Adivina un número entre 0 y 10")

        while True:
            intento = int(input("Ingresa número: "))

            if intento == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if intento < self.numeroAAdivinar:
                        print("El número es MAYOR")
                    else:
                        print("El número es MENOR")
                else:
                    break


class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()


Aplicacion.main()