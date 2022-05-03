import pygame
from Swiat import Swiat


class HexSwiat(Swiat):

    def rysujSwiat(self, gra):
        self.gra = gra
        wymiar_planszy = pygame.display.get_surface().get_size()
        przycisk_y = wymiar_planszy[0] * 0.075
        calkowita_odl_x = 1
        calkowita_odl_y = 1
        for i in range(len(self.organizmy) - 1):
            calkowita_odl_x += 1.5
        for i in range(len(self.organizmy[0]) - 1):
            calkowita_odl_y += 0.75
        if wymiar_planszy[0] / 2 < wymiar_planszy[1] - przycisk_y:
            bok = wymiar_planszy[0] / calkowita_odl_x
        else:
            bok = (wymiar_planszy[1] - przycisk_y) / calkowita_odl_y
        x = 0
        y = 0
        for j in range(len(self.organizmy)):
            tmp = 0
            for i in range(len(self.organizmy[j])):
                if self.organizmy[i][j] is not None:
                    kolor = self.organizmy[i][j].getKolor()
                else:
                    kolor = (255, 255, 255)
                pygame.draw.polygon(gra.okno, kolor, [
                    (x + tmp + bok * 0.5, y),
                    (x + tmp + bok, y + bok * 0.25),
                    (x + tmp + bok, y + bok * 0.75),
                    (x + tmp + bok * 0.5, y + bok),
                    (x + tmp, y + bok * 0.75),
                    (x + tmp, y + bok * 0.25)
                ])
                tmp += bok
            x += bok * 0.5
            y += bok * 0.75
        pygame.display.flip()
