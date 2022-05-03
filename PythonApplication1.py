from Czlowiek import Czlowiek
from Lis import Lis
from Wilk import Wilk
from Owca import Owca
from Zolw import Zolw
from Antylopa import Antylopa
from Trawa import Trawa
from Mlecz import Mlecz
from Guarana import Guarana
from WilczeJagody import WilczeJagody
from BarszczSosnowskiego import BarszczSosnowskiego
from Cyberowca import Cyberowca
from StandardSwiat import StandardSwiat
from HexSwiat import HexSwiat
import pygame
from Gra import Gra


pygame.init()

sw = StandardSwiat((20, 20))

okno = pygame.display.set_mode((800, 800))

pygame.display.set_caption('Mateusz Muńko 175508')

sw.organizmy[10][10] = Czlowiek(10, 10, sw)
sw.organizmy[10][11] = Owca(10, 11, sw)
sw.organizmy[19][19] = Wilk(19, 19, sw)
sw.organizmy[1][0] = Wilk(1, 0, sw)
sw.organizmy[16][5] = Wilk(16, 5, sw)
sw.organizmy[14][19] = Owca(14, 19, sw)
sw.organizmy[3][12] = Owca(3, 12, sw)
sw.organizmy[5][3] = Lis(5, 3, sw)
sw.organizmy[15][9] = Lis(15, 9, sw)
sw.organizmy[7][6] = Zolw(7, 6, sw)
sw.organizmy[19][1] = Zolw(19, 1, sw)
sw.organizmy[10][15] = Antylopa(10, 15, sw)
sw.organizmy[4][4] = Antylopa(4, 4, sw)
sw.organizmy[16][2] = Trawa(16, 2, sw)
sw.organizmy[6][13] = Trawa(6, 13, sw)
sw.organizmy[17][5] = Mlecz(17, 5, sw)
sw.organizmy[9][14] = Mlecz(9, 14, sw)
sw.organizmy[1][18] = Guarana(1, 18, sw)
sw.organizmy[4][19] = Guarana(4, 19, sw)
sw.organizmy[3][13] = WilczeJagody(3, 13, sw)
sw.organizmy[6][9] = WilczeJagody(6, 9, sw)
sw.organizmy[12][13] = BarszczSosnowskiego(12, 13, sw)
sw.organizmy[7][0] = BarszczSosnowskiego(7, 0, sw)
sw.organizmy[1][2] = Cyberowca(1, 2, sw)

gra = Gra(okno, sw)

gra.graj()
