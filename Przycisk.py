import pygame


class Przycisk:

    def __init__(self, x, y, dlugoscx, dlugoscy, kolor, tresc, rozmiar_czcionki):
        self.x = x
        self.y = y
        self.dlugoscx = dlugoscx
        self.dlugoscy = dlugoscy
        self.kolor = kolor
        self.tresc = tresc
        self.domyslny_kolor = kolor
        lst = list(self.kolor)
        lst[1] = int(lst[1] * 0.5)
        self.zmieniony_kolor = tuple(lst)
        self.rozmiar_czcionki = rozmiar_czcionki

    def rysujPrzycisk(self, gra):
        pygame.draw.rect(gra.okno, self.kolor,
                         pygame.Rect((self.x, self.y, self.dlugoscx, self.dlugoscy)))
        smallText = pygame.font.Font("freesansbold.ttf", int(self.rozmiar_czcionki))
        textSurf, textRect = self.text_objects(self.tresc, smallText)
        textRect.center = ((self.x + (self.dlugoscx / 2)), (self.y + (self.dlugoscy / 2)))
        gra.okno.blit(textSurf, textRect)

    def text_objects(self, text, font):
        textSurface = font.render(text, True, (0, 0, 0))
        return textSurface, textSurface.get_rect()

    def zmienKolorPrzycisku(self):
        self.kolor = self.zmieniony_kolor

    def standardowyKolorPrzycisku(self):
        self.kolor = self.domyslny_kolor
