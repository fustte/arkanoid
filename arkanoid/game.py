import pygame as pg

from . import ANCHO, ALTO
from .escenas import MejoresJugadores, Partida, Portada


class Arkanoid:

    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))

        # portada = Portada(self.pantalla)
        # partida = Partida(self.pantalla)
        # records = MejoresJugadores(self.pantalla)

        # self.escenas = [
        #     portada,
        #     partida,
        #     records,
        # ]

        self.escenas = [
            Portada(self.pantalla),
            Partida(self.pantalla),
            MejoresJugadores(self.pantalla),
        ]

    def jugar(self):
        """
        Bucle principal
        """
        for escena in self.escenas:
            acabar_juego = escena.bucle_principal()
            if acabar_juego:
                print('La escena me pide que acabe el juego')
                break

        pg.quit()

if __name__ == '__main__':
    print('Arrancamos el juego desde game.py que tiene Arkanoid')
    juego = Arkanoid()
    juego.jugar()