from Zwierze import Zwierzefrom random import randintclass Zolw(Zwierze):	def __init__(self, x, y, swiat):		super().__init__()		self.sila = 2		self.inicjatywa = 1		self.polozenie_x = x		self.polozenie_y = y		self.swiat = swiat		self.kolor = (143, 188, 139)	def akcja(self):		a = randint(0, 3)		if a == 0:			super(Zolw, self).akcja()	def kolizja(self, atakujacy, obronca):		if isinstance(atakujacy, type(obronca)):			super(Zolw, self).rozmnazanie(atakujacy, obronca)			return		x = atakujacy.getPolozenieX()		y = atakujacy.getPolozenieY()		x_obr = obronca.getPolozenieX()		y_obr = obronca.getPolozenieY()		if atakujacy.getSila() >= 5:			atakujacy.swiat.usunZKolejki(x_obr, y_obr)			atakujacy.swiat.organizmy[x_obr][y_obr] = None			atakujacy.swiat.organizmy[x_obr][y_obr] = atakujacy			atakujacy.swiat.organizmy[x_obr][y_obr].setPolozenieX(x_obr)			atakujacy.swiat.organizmy[x_obr][y_obr].setPolozenieY(y_obr)			atakujacy.swiat.organizmy[x][y] = None			return