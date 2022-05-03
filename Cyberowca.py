from Zwierze import Zwierze
import BarszczSosnowskiego
from Owca import Owca


class Cyberowca(Zwierze):

    def __init__(self, x, y, swiat):
        super().__init__()
        self.sila = 11
        self.inicjatywa = 4
        self.polozenie_x = x
        self.polozenie_y = y
        self.swiat = swiat
        self.kolor = (238, 130, 238)

    def akcja(self):
        barszcz = self.znajdzBarszczSosnowskiego()
        if not barszcz:
            Owca.akcja(self)
        else:
            if self.polozenie_x != barszcz.getPolozenieX():
                if self.polozenie_x > barszcz.getPolozenieX():
                    super(Cyberowca, self).wykonajRuch(self.getPolozenieX() - 1, self.getPolozenieY())
                else:
                    super(Cyberowca, self).wykonajRuch(self.getPolozenieX() + 1, self.getPolozenieY())
            elif self.polozenie_y != barszcz.getPolozenieY():
                if self.polozenie_y > barszcz.getPolozenieY():
                    super(Cyberowca, self).wykonajRuch(self.getPolozenieX(), self.getPolozenieY() - 1)
                else:
                    super(Cyberowca, self).wykonajRuch(self.getPolozenieX(), self.getPolozenieY() + 1)

    def znajdzBarszczSosnowskiego(self):
        barszcze = []
        for i in range(self.swiat.getRozmiarPlanszy()[0]):
            for j in range(self.swiat.getRozmiarPlanszy()[1]):
                if isinstance(self.swiat.organizmy[i][j], BarszczSosnowskiego.BarszczSosnowskiego):
                    barszcze.append(
                        (self.swiat.organizmy[i][j], abs(self.polozenie_x - self.swiat.organizmy[i][j].getPolozenieX())
                         + abs(self.polozenie_y - self.swiat.organizmy[i][j].getPolozenieY()))
                    )
        barszcze.sort(key=lambda x: x[1])
        if barszcze:
            return barszcze[0][0]
        else:
            return []

    def kolizja(self, atakujacy, obronca):
        if isinstance(atakujacy, type(obronca)):
            super(Cyberowca, self).rozmnazanie(atakujacy, obronca)
            return
        if isinstance(obronca, BarszczSosnowskiego.BarszczSosnowskiego):
            x = atakujacy.getPolozenieX()
            y = atakujacy.getPolozenieY()
            x_obr = obronca.getPolozenieX()
            y_obr = obronca.getPolozenieY()
            atakujacy.swiat.usunZKolejki(x_obr, y_obr)
            atakujacy.swiat.organizmy[x_obr][y_obr] = None
            atakujacy.swiat.organizmy[x_obr][y_obr] = atakujacy
            atakujacy.swiat.organizmy[x_obr][y_obr].setPolozenieX(x_obr)
            atakujacy.swiat.organizmy[x_obr][y_obr].setPolozenieY(y_obr)
            atakujacy.swiat.organizmy[x][y] = None
            return
        else:
            super(Cyberowca, self).kolizja(atakujacy, obronca)
