from abc import ABC, abstractmethod


class Swiat(ABC):

    def __init__(self, rozmiar_planszy):
        self.rozmiar_planszy = rozmiar_planszy
        self.organizmy = [[None for i in range(rozmiar_planszy[1])] for j in range(rozmiar_planszy[0])]
        self.kolejnosc = []

    @abstractmethod
    def rysujSwiat(self, gra):
        pass

    def wykonajTure(self):
        self.kolejnosc = []
        for i in range(self.rozmiar_planszy[0]):
            for j in range(self.rozmiar_planszy[1]):
                if self.organizmy[i][j] is not None:
                    self.kolejnosc.append(self.organizmy[i][j])
        self.kolejnosc.sort(key=lambda organizm: organizm.getInicjatywa(), reverse=True)
        for i in self.kolejnosc:
            if i is not None:
                i.akcja()
                i.setWiek(i.getWiek() + 1)

    def usunZKolejki(self, x, y):
        for i in range(len(self.kolejnosc)):
            if self.kolejnosc[i] is not None and self.kolejnosc[i].getPolozenieX() == x\
                    and self.kolejnosc[i].getPolozenieY() == y:
                self.kolejnosc[i] = None

    def getRozmiarPlanszy(self):
        return self.rozmiar_planszy

    def dodajOrganizm(self, pole, typ):
        self.organizmy[pole[0]][pole[1]] = typ(pole[0], pole[1], self)
