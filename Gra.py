import pygame
import sys
from Przycisk import Przycisk
import pickle
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
from Czlowiek import Czlowiek


class Gra:

    def __init__(self, okno, swiat):
        self.okno = okno
        self.swiat = swiat

    def obslugaZdarzen(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)

    def graj(self):
        events = []
        last = pygame.time.get_ticks()
        wymiar_planszy = pygame.display.get_surface().get_size()
        przycisk_y = wymiar_planszy[0] * 0.075
        self.zapisz = Przycisk(0, wymiar_planszy[1] - przycisk_y, wymiar_planszy[0] / 3, przycisk_y, (100, 100, 255),
                               "Zapisz", przycisk_y / 2)
        self.nowa_tura = Przycisk(wymiar_planszy[0] / 3, wymiar_planszy[1] - przycisk_y, wymiar_planszy[0] / 3,
                                  przycisk_y, (255, 100, 255), "Nowa tura", przycisk_y / 2)
        self.wczytaj = Przycisk(wymiar_planszy[0] / 3 * 2, wymiar_planszy[1] - przycisk_y, wymiar_planszy[0] / 3,
                                przycisk_y, (100, 100, 50), "Wczytaj", przycisk_y / 2)
        self.wykonaj_ruch = Przycisk(0, wymiar_planszy[1] - przycisk_y, wymiar_planszy[0] / 2, przycisk_y,
                                           (124, 185, 232), "Wykonaj ruch", przycisk_y / 2)
        self.aktywuj_umiejetnosc = Przycisk(wymiar_planszy[0] / 2, wymiar_planszy[1] - przycisk_y,
                                            wymiar_planszy[0] / 2, przycisk_y,
                                     (255, 126, 0), "Aktywuj umiejetnosc", przycisk_y / 2)
        while True:
            for event in pygame.event.get():
                events.append(event)
            self.obslugaZdarzen(events)
            self.swiat.rysujSwiat(self)
            self.nowa_tura.rysujPrzycisk(self)
            self.zapisz.rysujPrzycisk(self)
            self.wczytaj.rysujPrzycisk(self)
            mysz = pygame.mouse.get_pos()
            nowa_tura = self.nowa_tura
            zapisz = self.zapisz
            wczytaj = self.wczytaj
            klik = pygame.mouse.get_pressed()
            if nowa_tura.x < mysz[0] < nowa_tura.x + nowa_tura.dlugoscx and\
                    nowa_tura.y < mysz[1] < nowa_tura.y + nowa_tura.dlugoscy:
                nowa_tura.zmienKolorPrzycisku()
                now = pygame.time.get_ticks()
                if klik[0] == 1 and now - last >= 200:
                    self.swiat.wykonajTure()
                    last = pygame.time.get_ticks()
            elif zapisz.x < mysz[0] < zapisz.x + zapisz.dlugoscx and zapisz.y < mysz[1] < zapisz.y + zapisz.dlugoscy:
                nowa_tura.standardowyKolorPrzycisku()
                wczytaj.standardowyKolorPrzycisku()
                zapisz.zmienKolorPrzycisku()
                now = pygame.time.get_ticks()
                if klik[0] == 1 and now - last >= 200:
                    Gra.zapisz(self)
                    last = pygame.time.get_ticks()
            elif wczytaj.x < mysz[0] < wczytaj.x + wczytaj.dlugoscx and\
                    wczytaj.y < mysz[1] < wczytaj.y + wczytaj.dlugoscy:
                nowa_tura.standardowyKolorPrzycisku()
                zapisz.standardowyKolorPrzycisku()
                wczytaj.zmienKolorPrzycisku()
                now = pygame.time.get_ticks()
                if klik[0] == 1 and now - last >= 200:
                    Gra.wczytaj(self)
                    last = pygame.time.get_ticks()
            elif 0 <= mysz[0] < wymiar_planszy[0] and 0 <= mysz[1] < wymiar_planszy[1] - nowa_tura.dlugoscy:
                nowa_tura.standardowyKolorPrzycisku()
                zapisz.standardowyKolorPrzycisku()
                wczytaj.standardowyKolorPrzycisku()
                now = pygame.time.get_ticks()
                if klik[0] == 1 and now - last >= 200:
                    self.menuDodaniaOrganizmu(mysz)
                    last = pygame.time.get_ticks()
            else:
                nowa_tura.standardowyKolorPrzycisku()
                zapisz.standardowyKolorPrzycisku()
                wczytaj.standardowyKolorPrzycisku()

    def zapisz(self):
        print("Podaj nazwę pliku, do którego chcesz zapisać")
        nazwa = input()
        nazwa += '.pkl'
        rozmiar = self.swiat.getRozmiarPlanszy()
        tmp = [[None for i in range(rozmiar[0])] for j in range(rozmiar[1])]
        for i in range(rozmiar[0]):
            for j in range(rozmiar[1]):
                if self.swiat.organizmy[i][j] is not None:
                    self.swiat.organizmy[i][j].swiat = None
                tmp[i][j] = self.swiat.organizmy[i][j]
        with open(nazwa, 'wb') as output:
            pickle.dump(tmp, output, pickle.HIGHEST_PROTOCOL)
        for i in range(rozmiar[0]):
            for j in range(rozmiar[1]):
                if self.swiat.organizmy[i][j] is not None:
                    self.swiat.organizmy[i][j].swiat = self.swiat

    def wczytaj(self):
        print("Podaj nazwę pliku, z którego chcesz wczytać")
        nazwa = input()
        nazwa += '.pkl'
        rozmiar = self.swiat.getRozmiarPlanszy()
        with open(nazwa, 'rb') as inp:
            tmp = pickle.load(inp)
        for i in range(rozmiar[0]):
            for j in range(rozmiar[1]):
                self.swiat.organizmy[i][j] = tmp[i][j]
                if self.swiat.organizmy[i][j] is not None:
                    self.swiat.organizmy[i][j].swiat = self.swiat

    def getSwiat(self):
        return self.swiat

    def getOkno(self):
        return self.okno

    def menuDodaniaOrganizmu(self, pozycja_myszy):
        last = pygame.time.get_ticks()
        events = []
        wymiar_planszy = pygame.display.get_surface().get_size()
        dodaj_rosline = Przycisk(0, wymiar_planszy[1] * 0.25, wymiar_planszy[0] / 2, wymiar_planszy[1] / 5,
                                 (100, 100, 50), "Dodaj rosline", wymiar_planszy[1] / 15)
        dodaj_zwierze = Przycisk(wymiar_planszy[0] / 2, wymiar_planszy[1] * 0.25, wymiar_planszy[0] / 2,
                                 wymiar_planszy[1] / 5, (0, 100, 50), "Dodaj zwierze", wymiar_planszy[1] / 15)
        while True:
            pygame.display.flip()
            for event in pygame.event.get():
                events.append(event)
            self.obslugaZdarzen(events)
            dodaj_rosline.rysujPrzycisk(self)
            dodaj_zwierze.rysujPrzycisk(self)
            mysz = pygame.mouse.get_pos()
            klik = pygame.mouse.get_pressed()
            if dodaj_rosline.x < mysz[0] < dodaj_rosline.x + dodaj_rosline.dlugoscx and \
                    dodaj_rosline.y < mysz[1] < dodaj_rosline.y + dodaj_rosline.dlugoscy:
                dodaj_rosline.zmienKolorPrzycisku()
                dodaj_zwierze.standardowyKolorPrzycisku()
                now = pygame.time.get_ticks()
                if klik[0] == 1 and now - last >= 200:
                    rosliny = (
                        ('Barszcz S.', (128, 128, 0), BarszczSosnowskiego),
                        ('Guarana', (255, 20, 147), Guarana),
                        ('Mlecz', (255, 215, 0), Mlecz),
                        ('Trawa', (0, 128, 0), Trawa),
                        ('W. Jagody', (25, 25, 112), WilczeJagody)
                    )
                    self.wybierzOrganizm(rosliny, pozycja_myszy)
                    last = pygame.time.get_ticks()
                    return
            elif dodaj_zwierze.x < mysz[0] < dodaj_zwierze.x + dodaj_zwierze.dlugoscx and \
                    dodaj_zwierze.y < mysz[1] < dodaj_zwierze.y + dodaj_zwierze.dlugoscy:
                dodaj_zwierze.zmienKolorPrzycisku()
                dodaj_rosline.standardowyKolorPrzycisku()
                now = pygame.time.get_ticks()
                if klik[0] == 1 and now - last >= 200:
                    zwierzeta = (
                        ('Antylopa', (205, 92, 92), Antylopa),
                        ('Cyberowca', (238, 130, 238), Cyberowca),
                        ('Lis', (255, 140, 0), Lis),
                        ('Owca', (238, 232, 170), Owca),
                        ('Wilk', (128, 128, 128), Wilk),
                        ('Zolw', (143, 188, 139), Zolw),
                        ('Czlowiek', (0, 0, 0), Czlowiek)
                    )
                    self.wybierzOrganizm(zwierzeta, pozycja_myszy)
                    last = pygame.time.get_ticks()
                    return
            else:
                dodaj_rosline.standardowyKolorPrzycisku()
                dodaj_zwierze.standardowyKolorPrzycisku()

    def wybierzOrganizm(self, organizmy, pozycja_myszy):
        wymiar_planszy = pygame.display.get_surface().get_size()
        przycisk_y = wymiar_planszy[0] * 0.075
        odleglosc_pola_x = wymiar_planszy[0] / self.swiat.rozmiar_planszy[0]
        odleglosc_pola_y = (wymiar_planszy[1] - przycisk_y) / self.swiat.rozmiar_planszy[1]
        pole = (
            (int(pozycja_myszy[0] / odleglosc_pola_x)),
            (int(pozycja_myszy[1] / odleglosc_pola_y))
        )
        last = pygame.time.get_ticks()
        events = []
        wymiar_planszy = pygame.display.get_surface().get_size()
        przyciski = []
        liczba_przyciskow = len(organizmy)
        i = 0
        for organizm in organizmy:
            przycisk = (Przycisk(i * wymiar_planszy[0] / liczba_przyciskow, wymiar_planszy[1] / 2,
                                wymiar_planszy[0] / liczba_przyciskow, wymiar_planszy[1] / liczba_przyciskow,
                                organizm[1], organizm[0], wymiar_planszy[1] / (liczba_przyciskow * 6)), organizm[2])
            przyciski.append(przycisk)
            i += 1
        while True:
            pygame.display.flip()
            for event in pygame.event.get():
                events.append(event)
            self.obslugaZdarzen(events)
            for przycisk in przyciski:
                przycisk[0].rysujPrzycisk(self)
            mysz = pygame.mouse.get_pos()
            klik = pygame.mouse.get_pressed()
            if przyciski[0][0].y < mysz[1] < przyciski[0][0].y + przyciski[0][0].dlugoscy:
                for przycisk in przyciski:
                    if przycisk[0].x < mysz[0] < przycisk[0].x + przycisk[0].dlugoscx:
                        przycisk[0].zmienKolorPrzycisku()
                        for p in przyciski:
                            if p is not przycisk:
                                p[0].standardowyKolorPrzycisku()
                        now = pygame.time.get_ticks()
                        if klik[0] == 1 and now - last >= 200:
                            self.swiat.dodajOrganizm(pole, przycisk[1])
                            return
            else:
                for p in przyciski:
                    p[0].standardowyKolorPrzycisku()
