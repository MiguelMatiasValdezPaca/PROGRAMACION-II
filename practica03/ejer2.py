import random

# Clase padre
class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0

    def reiniciaPartida(self):
        print("\nNueva partida")

    def actualizaRecord(self):
        self.record += 1
        print("Record:", self.record)

    def quitaVida(self):
        self.numeroDeVidas -= 1
        print("Vidas:", self.numeroDeVidas)
        return self.numeroDeVidas > 0


# Clase base intermedia
class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0

    def validaNumero(self, num):
        return 0 <= num <= 10

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        while True:
            intento = int(input("Número (0-10): "))

            if not self.validaNumero(intento):
                print("Número inválido")
                continue

            if intento == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if intento < self.numeroAAdivinar:
                        print("Es mayor")
                    else:
                        print("Es menor")
                else:
                    print("Game Over")
                    break


# Clase hija PAR
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, num):
        if 0 <= num <= 10:
            if num % 2 == 0:
                return True
            else:
                print("Error: debe ser PAR")
                return False
        return False


# Clase hija IMPAR
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, num):
        if 0 <= num <= 10:
            if num % 2 != 0:
                return True
            else:
                print("Error: debe ser IMPAR")
                return False
        return False


# Aplicación
class Aplicacion:
    @staticmethod
    def main():
        juego1 = JuegoAdivinaNumero(3)
        juego2 = JuegoAdivinaPar(3)
        juego3 = JuegoAdivinaImpar(3)

        juego1.juega()
        juego2.juega()
        juego3.juega()


Aplicacion.main()