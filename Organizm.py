from abc import ABC, abstractmethod


class Organizm(ABC):

    def __init__(self):
        self.wiek = 0

    @abstractmethod
    def kolizja(self, atakujacy, obronca):
        pass

    @abstractmethod
    def akcja(self):
        pass

    def getSila(self):
        return self.sila

    def getWiek(self):
        return self.wiek

    def getPolozenieX(self):
        return self.polozenie_x

    def getPolozenieY(self):
        return self.polozenie_y

    def getKolor(self):
        return self.kolor

    def getInicjatywa(self):
        return self.inicjatywa
    
    def setSila(self, sila):
        self.sila = sila

    def setPolozenieX(self, x):
        self.polozenie_x = x

    def setPolozenieY(self, y):
        self.polozenie_y = y

    def setWiek(self, wiek):
        self.wiek = wiek

    def szukajWolnychPol(self, organizm, wolne_pola):
        x = organizm.getPolozenieX()
        y = organizm.getPolozenieY()
        i = -1
        plansza = organizm.swiat.getRozmiarPlanszy()
        while i < 2:
            if 0 <= x + 1 < plansza[0] and 0 <= y + i < plansza[1] and organizm.swiat.organizmy[x + 1][y + i] is None\
                    and (x + 1, y + i) not in wolne_pola:
                wolne_pola.append((x + 1, y + i))
            if 0 <= x - 1 < plansza[0] and 0 <= y - 1 < plansza[1] and organizm.swiat.organizmy[x][y - 1] is None and\
                    (x, y - 1) not in wolne_pola:
                wolne_pola.append((x - 1, y - 1))
            if 0 <= x < plansza[0] and 0 <= y - 1 < plansza[1] and organizm.swiat.organizmy[x][y - 1] is None and\
                    (x, y + 1) not in wolne_pola:
                wolne_pola.append((x, y - 1))
            if 0 <= x < plansza[0] and 0 <= y + 1 < plansza[1] and organizm.swiat.organizmy[x][y + 1] is None and\
                    (x, y + i) not in wolne_pola:
                wolne_pola.append((x, y + 1))
            i += 1
