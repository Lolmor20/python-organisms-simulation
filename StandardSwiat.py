import pygame
from Swiat import Swiat


class StandardSwiat(Swiat):

    def rysujSwiat(self, gra):
        self.gra = gra
        wymiar_planszy = pygame.display.get_surface().get_size()
        kwadrat_x = wymiar_planszy[0] / len(self.organizmy)
        przycisk_y = wymiar_planszy[0] * 0.075
        kwadrat_y = (wymiar_planszy[1] - przycisk_y) / len(self.organizmy[1])
        for i in range(len(self.organizmy)):
            for j in range(len(self.organizmy[i])):
                if self.organizmy[i][j] is None:
                    kolor = (255, 255, 255)
                else:
                    kolor = self.organizmy[i][j].getKolor()
                pygame.draw.rect(gra.okno, kolor, pygame.Rect(i * kwadrat_x, j * kwadrat_y, kwadrat_x, kwadrat_y))
        pygame.display.flip()
